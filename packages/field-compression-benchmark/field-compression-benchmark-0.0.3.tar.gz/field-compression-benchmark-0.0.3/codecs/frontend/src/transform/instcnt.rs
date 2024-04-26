pub struct InstructionCounterInjecter {
    instruction_counter: walrus::GlobalId,
}

impl InstructionCounterInjecter {
    pub fn inject_into_module(module: &mut walrus::Module) -> walrus::GlobalId {
        let (instruction_counter, _import) =
            module.add_import_global("fcbench", "instruction-counter", walrus::ValType::I64, true);

        for (_, func) in module.funcs.iter_local_mut() {
            let entry = func.entry_block();

            walrus::ir::dfs_pre_order_mut(
                &mut Self {
                    instruction_counter,
                },
                func,
                entry,
            );
        }

        instruction_counter
    }

    const fn instruction_needs_counter_update(instr: &walrus::ir::Instr) -> bool {
        #[allow(clippy::match_same_arms)]
        match instr {
            walrus::ir::Instr::Block(_)
            | walrus::ir::Instr::Loop(_)
            | walrus::ir::Instr::Br(_)
            | walrus::ir::Instr::BrIf(_)
            | walrus::ir::Instr::IfElse(_)
            | walrus::ir::Instr::BrTable(_)
            | walrus::ir::Instr::Return(_) => true,
            // calls must return control flow to continue,
            //  so no counter-saving is necessary
            walrus::ir::Instr::Call(_) | walrus::ir::Instr::CallIndirect(_) => false,
            // unreachable control flow doesn't need to care
            //  about instruction counting
            walrus::ir::Instr::Unreachable(_) => false,
            // no control flow occurs
            walrus::ir::Instr::LocalGet(_)
            | walrus::ir::Instr::LocalSet(_)
            | walrus::ir::Instr::LocalTee(_)
            | walrus::ir::Instr::GlobalGet(_)
            | walrus::ir::Instr::GlobalSet(_)
            | walrus::ir::Instr::Const(_)
            | walrus::ir::Instr::Binop(_)
            | walrus::ir::Instr::Unop(_)
            | walrus::ir::Instr::Select(_)
            | walrus::ir::Instr::Drop(_)
            | walrus::ir::Instr::MemorySize(_)
            | walrus::ir::Instr::MemoryGrow(_)
            | walrus::ir::Instr::MemoryInit(_)
            | walrus::ir::Instr::DataDrop(_)
            | walrus::ir::Instr::MemoryCopy(_)
            | walrus::ir::Instr::MemoryFill(_)
            | walrus::ir::Instr::Load(_)
            | walrus::ir::Instr::Store(_)
            | walrus::ir::Instr::AtomicRmw(_)
            | walrus::ir::Instr::Cmpxchg(_)
            | walrus::ir::Instr::AtomicNotify(_)
            | walrus::ir::Instr::AtomicWait(_)
            | walrus::ir::Instr::AtomicFence(..)
            | walrus::ir::Instr::TableGet(_)
            | walrus::ir::Instr::TableSet(_)
            | walrus::ir::Instr::TableGrow(_)
            | walrus::ir::Instr::TableSize(_)
            | walrus::ir::Instr::TableFill(_)
            | walrus::ir::Instr::RefNull(_)
            | walrus::ir::Instr::RefIsNull(_)
            | walrus::ir::Instr::RefFunc(_)
            | walrus::ir::Instr::V128Bitselect(_)
            | walrus::ir::Instr::I8x16Swizzle(_)
            | walrus::ir::Instr::I8x16Shuffle(_)
            | walrus::ir::Instr::LoadSimd(_)
            | walrus::ir::Instr::TableInit(_)
            | walrus::ir::Instr::ElemDrop(_)
            | walrus::ir::Instr::TableCopy(_) => false,
        }
    }

    fn generate_instruction_counter_update(
        &self,
        delta: i64,
    ) -> impl IntoIterator<Item = (walrus::ir::Instr, walrus::ir::InstrLocId)> {
        [
            (
                walrus::ir::Instr::GlobalGet(walrus::ir::GlobalGet {
                    global: self.instruction_counter,
                }),
                walrus::ir::InstrLocId::default(),
            ),
            (
                walrus::ir::Instr::Const(walrus::ir::Const {
                    value: walrus::ir::Value::I64(delta),
                }),
                walrus::ir::InstrLocId::default(),
            ),
            (
                walrus::ir::Instr::Binop(walrus::ir::Binop {
                    op: walrus::ir::BinaryOp::I64Add,
                }),
                walrus::ir::InstrLocId::default(),
            ),
            (
                walrus::ir::Instr::GlobalSet(walrus::ir::GlobalSet {
                    global: self.instruction_counter,
                }),
                walrus::ir::InstrLocId::default(),
            ),
        ]
    }
}

impl walrus::ir::VisitorMut for InstructionCounterInjecter {
    fn start_instr_seq_mut(&mut self, instr_seq: &mut walrus::ir::InstrSeq) {
        let mut i = 0;

        let mut counter: i64 = 0;

        while let Some((instr, _)) = instr_seq.get(i) {
            counter += 1;

            if Self::instruction_needs_counter_update(instr) {
                for new_instr in self.generate_instruction_counter_update(counter) {
                    instr_seq.insert(i, new_instr);
                    i += 1;
                }

                counter = 0;
            }

            i += 1;
        }

        if counter > 0 {
            instr_seq.extend(self.generate_instruction_counter_update(counter));
        }
    }
}
