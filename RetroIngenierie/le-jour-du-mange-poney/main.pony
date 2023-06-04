//404CTF{v1Rtu4L_P0ny: fuNCt10n$-g0e$_bRr}
//Le mot de passe pour valider le binaire est sans le 404CTF{...}

//J'ai appris le langage en faisant le chall, donc pardon pour les abérations éventuelles. 

use "collections"

actor Main
    new create(env : Env) =>
        let vm = VM(env)

class VM
    let prgm : Array[U8 val] val
    let stack : List[U64]
    var regs : Array[U64] ref

    var mem : Array[U8] ref
    var pc : U64
    var inst : U8

    new create(env : Env) =>
        prgm = [28; 0; 243; 255; 25; 4; 12; 0; 12; 28; 0; 4; 25; 4; 12; 0; 103; 25; 4; 11; 0; 65; 25; 4; 10; 0; 154; 25; 4; 9; 0; 137; 25; 4; 8; 0; 194; 25; 4; 7; 0; 211; 25; 4; 6; 0; 174; 25; 4; 5; 0; 86; 25; 4; 4; 0; 120; 25; 4; 3; 0; 228; 20; 0; 242; 170; 8; 9; 8; 16; 29; 8; 8; 18; 1; 100; 1; 8; 26; 1; 33; 1; 201; 20; 0; 242; 9; 1; 10; 29; 1; 1; 13; 1; 2; 26; 1; 112; 1; 201; 20; 0; 242; 9; 8; 17; 29; 8; 8; 10; 8; 44; 26; 8; 111; 1; 201; 20; 0; 242; 9; 3; 9; 29; 3; 3; 100; 3; 6; 26; 3; 66; 1; 201; 20; 0; 242; 9; 1; 14; 29; 1; 1; 140; 6; 1; 26; 6; 114; 1; 201; 20; 0; 242; 9; 6; 15; 29; 6; 6; 130; 6; 1; 100; 6; 8; 26; 6; 216; 1; 201; 20; 0; 242; 9; 2; 11; 29; 2; 2; 130; 2; 6; 100; 2; 1; 26; 2; 71; 1; 201; 20; 0; 242; 9; 1; 13; 29; 1; 1; 100; 1; 6; 26; 1; 82; 1; 201; 20; 0; 242; 9; 1; 12; 29; 1; 1; 130; 1; 6; 26; 1; 172; 1; 201; 20; 0; 242; 9; 2; 8; 29; 2; 2; 130; 2; 3; 26; 2; 146; 1; 201; 27; 100; 8; 8; 28; 1; 205; 14; 0; 32; 22; 0; 1; 201; 29; 0; 0; 28; 2; 159; 9; 1; 140; 15; 1; 100; 13; 1; 42; 126; 0; 1; 1; 201; 9; 0; 1; 29; 0; 0; 9; 1; 2; 29; 1; 1; 28; 2; 142; 26; 0; 105; 1; 201; 26; 1; 85; 1; 201; 9; 0; 3; 9; 1; 4; 9; 2; 5; 9; 3; 6; 29; 0; 0; 29; 1; 1; 29; 2; 2; 29; 3; 3; 28; 2; 37; 22; 0; 1; 201; 9; 0; 7; 29; 0; 0; 28; 2; 159; 9; 1; 91; 15; 1; 100; 13; 1; 20; 126; 0; 1; 1; 201; 100; 0; 0; 28; 0; 4; 9; 0; 18; 29; 0; 0; 28; 2; 159; 9; 1; 135; 15; 1; 100; 13; 1; 72; 126; 0; 1; 1; 201; 28; 2; 170; 9; 0; 20; 9; 1; 21; 29; 0; 0; 29; 1; 1; 28; 3; 66; 9; 2; 200; 13; 2; 68; 26; 0; 206; 1; 201; 126; 1; 2; 1; 201; 9; 0; 22; 29; 0; 0; 28; 2; 159; 9; 1; 13; 15; 1; 100; 13; 1; 32; 126; 0; 1; 1; 201; 9; 0; 23; 29; 0; 0; 28; 1; 223; 28; 3; 137; 20; 1; 219; 27; 28; 1; 245; 255; 29; 1; 0; 21; 1; 1; 218; 13; 0; 1; 20; 1; 205; 27; 28; 2; 100; 255; 18; 1; 170; 1; 100; 0; 1; 9; 1; 4; 15; 1; 100; 13; 1; 95; 126; 0; 1; 1; 201; 27; 100; 0; 0; 19; 0; 78; 13; 0; 1; 19; 0; 111; 13; 0; 1; 19; 0; 110; 13; 0; 1; 19; 0; 32; 13; 0; 1; 19; 0; 59; 13; 0; 1; 19; 0; 40; 13; 0; 1; 19; 0; 0; 100; 0; 0; 254; 0; 27; 90; 5; 0; 100; 5; 1; 26; 5; 1; 2; 96; 90; 5; 2; 100; 5; 3; 26; 5; 120; 2; 96; 90; 5; 1; 100; 5; 3; 26; 5; 57; 2; 96; 90; 5; 0; 130; 5; 2; 26; 5; 168; 2; 96; 90; 5; 0; 110; 5; 3; 26; 5; 68; 2; 96; 9; 0; 0; 27; 9; 0; 1; 27; 100; 0; 0; 19; 0; 89; 13; 0; 1; 19; 0; 97; 13; 0; 1; 19; 0; 121; 13; 0; 1; 19; 0; 32; 13; 0; 1; 19; 0; 33; 13; 0; 1; 19; 0; 0; 100; 0; 0; 254; 0; 27; 17; 26; 130; 1; 4; 18; 2; 160; 2; 4; 100; 0; 2; 100; 0; 1; 27; 170; 0; 150; 0; 0; 18; 1; 130; 0; 1; 27; 28; 2; 174; 27; 28; 2; 178; 27; 28; 2; 182; 27; 28; 2; 186; 27; 28; 2; 190; 27; 28; 2; 194; 27; 28; 2; 198; 27; 28; 2; 202; 27; 28; 2; 206; 27; 28; 2; 210; 27; 28; 2; 214; 27; 28; 2; 218; 27; 28; 2; 222; 27; 28; 2; 226; 27; 28; 2; 230; 27; 28; 2; 234; 27; 28; 2; 238; 27; 28; 2; 242; 27; 28; 2; 246; 27; 28; 2; 250; 27; 28; 2; 254; 27; 28; 3; 2; 27; 28; 3; 6; 27; 28; 3; 10; 27; 28; 3; 14; 27; 28; 3; 18; 27; 28; 3; 22; 27; 28; 3; 26; 27; 28; 3; 30; 27; 28; 3; 34; 27; 28; 3; 38; 27; 28; 3; 42; 27; 28; 3; 46; 27; 28; 3; 50; 27; 28; 3; 54; 27; 28; 3; 58; 27; 28; 3; 62; 27; 28; 3; 83; 27; 170; 0; 15; 0; 2; 130; 0; 1; 15; 1; 2; 18; 2; 130; 1; 2; 27; 28; 3; 87; 27; 28; 3; 91; 27; 28; 3; 95; 27; 28; 3; 99; 27; 28; 3; 103; 27; 28; 3; 107; 27; 28; 3; 111; 27; 28; 3; 115; 27; 28; 3; 119; 27; 9; 0; 19; 29; 0; 0; 126; 0; 4; 1; 201; 9; 3; 240; 19; 3; 134; 27; 9; 3; 240; 9; 0; 24; 9; 1; 26; 29; 0; 0; 29; 1; 1; 29; 3; 3; 130; 1; 0; 140; 1; 3; 26; 1; 70; 1; 201; 15; 0; 2; 9; 1; 29; 29; 1; 1; 130; 0; 1; 14; 0; 100; 26; 0; 204; 1; 201; 9; 0; 28; 29; 0; 0; 9; 1; 31; 29; 1; 1; 15; 0; 3; 140; 0; 1; 26; 0; 171; 1; 201; 9; 0; 24; 9; 8; 8; 100; 1; 1; 21; 8; 3; 237; 14; 8; 1; 29; 2; 0; 130; 1; 2; 13; 0; 1; 20; 3; 218; 9; 0; 6; 15; 0; 100; 13; 0; 77; 126; 0; 1; 1; 201; 9; 0; 25; 9; 1; 30; 29; 0; 0; 29; 1; 1; 15; 1; 2; 130; 0; 1; 26; 0; 212; 1; 201; 9; 0; 27; 9; 1; 31; 29; 0; 0; 29; 1; 1; 15; 0; 7; 15; 1; 2; 140; 0; 1; 26; 0; 24; 1; 201; 9; 0; 29; 9; 1; 28; 29; 0; 0; 29; 1; 1; 140; 0; 1; 26; 0; 3; 1; 201; 9; 0; 29; 9; 1; 30; 29; 0; 0; 29; 1; 1; 140; 0; 1; 26; 0; 16; 1; 201; 27]
        stack = List[U64]()
        regs = [0; 0; 0; 0; 0; 0; 0; 0; 0]
        mem = Array[U8].init(0, 65536)
        pc = 0
        inst = 0

        var cpt : U64
        cpt = 0
        try
            for byte in env.args.apply(1)?.values() do
                    mem.update(cpt.usize(), byte.u8())?
                cpt = cpt + 1
            end
        end
        if cpt == 0 then
            env.out.print("Usage : ./my_little_pony [MOT DE PASSE]")
            return
        end
        
        launch(env)

    fun ref launch(env : Env) =>
        while pc < prgm.size().u64() do
            try
                inst = prgm.apply(pc.usize())?
                //env.out.print(pc.string() + " : " + inst.string())
            end

            if inst == 9 then
                try
                    handle_mov_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 90 then
                try
                    handle_mov(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 10 then
                try
                    handle_xor_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 100 then
                try
                    handle_xor(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 11 then
                try
                    handle_and_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 110 then
                try
                    handle_and(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 12 then
                try
                    handle_or_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 120 then
                try
                    handle_or(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 13 then
                try
                    handle_add_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 130 then
                try
                    handle_add(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 14 then
                try
                    handle_sub_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 140 then
                try
                    handle_sub(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 15 then
                try
                    handle_mul_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 150 then
                try
                    handle_mul(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 16 then
                try
                    handle_div_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 160 then
                try
                    handle_div(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 17 then
                try
                    handle_push_imm(prgm.apply(pc.usize() + 1)?)
                end
                pc = pc + 2
            elseif inst == 170 then
                try
                    handle_push(prgm.apply(pc.usize() + 1)?)
                end
                pc = pc + 2
            elseif inst == 18 then
                try
                    handle_pop(prgm.apply(pc.usize() + 1)?)
                end
                pc = pc + 2
            elseif inst == 19 then
                try
                    handle_mov_to_mem_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 190 then
                try
                    handle_mov_to_mem(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 20 then
                try
                    handle_jmp_abs(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
            elseif inst == 21 then
                try
                    handle_jz_abs(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?, prgm.apply(pc.usize() + 3)?)
                end
            elseif inst == 22 then
                try
                    handle_jnz_abs(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?, prgm.apply(pc.usize() + 3)?)
                end
            elseif inst == 23 then
                try
                    handle_jge_abs_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?, prgm.apply(pc.usize() + 3)?, prgm.apply(pc.usize() + 4)?)
                end
            elseif inst == 24 then
                try
                    handle_jle_abs_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?, prgm.apply(pc.usize() + 3)?, prgm.apply(pc.usize() + 4)?)
                end
            elseif inst == 25 then
                try
                    handle_je_abs_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?, prgm.apply(pc.usize() + 3)?, prgm.apply(pc.usize() + 4)?)
                end
            elseif inst == 26 then
                try
                    handle_jne_abs_imm(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?, prgm.apply(pc.usize() + 3)?, prgm.apply(pc.usize() + 4)?)
                end
            elseif inst == 126 then
                try
                    handle_jne_abs(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?, prgm.apply(pc.usize() + 3)?, prgm.apply(pc.usize() + 4)?)
                end
            elseif inst == 27 then
                handle_ret()
            elseif inst == 28 then
                try
                    handle_call(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
            elseif inst == 29 then
                try
                    handle_read_mem(prgm.apply(pc.usize() + 1)?, prgm.apply(pc.usize() + 2)?)
                end
                pc = pc + 3
            elseif inst == 254 then
                try
                    handle_print_string(prgm.apply(pc.usize() + 1)?, env.out)
                end
                pc = pc + 2
            elseif inst == 255 then
                return
            end
        end

    fun ref handle_mov_imm(reg : U8, imm : U8) =>
        try
            regs.update(reg.usize(), imm.u64())?
        end

    fun ref handle_mov(reg1 : U8, reg2 : U8) =>
        try
            regs.update(reg1.usize(), regs.apply(reg2.usize())?)?
        end 

    fun ref handle_mov_to_mem_imm(add : U8, imm : U8) =>
        try
            mem.update(regs.apply(add.usize())?.usize(), imm)?
        end

    fun ref handle_mov_to_mem(add : U8, reg : U8) =>
        try
            mem.update(regs.apply(add.usize())?.usize(), regs.apply(reg.usize())?.u8())?
        end

    fun ref handle_read_mem(reg : U8, add : U8) =>
        try
            regs.update(reg.usize(), mem.apply(regs.apply(add.usize())?.usize())?.u64())?
        end

    fun ref handle_xor_imm(reg : U8, imm : U8) =>
        try
            regs.update(reg.usize(), regs.apply(reg.usize())?.op_xor(imm.u64()))?
        end

    fun ref handle_xor(reg1 : U8, reg2 : U8) =>
        try
            regs.update(reg1.usize(), regs.apply(reg1.usize())?.op_xor(regs.apply(reg2.usize())?))?
        end 
    
    fun ref handle_and_imm(reg : U8, imm : U8) =>
        try
            regs.update(reg.usize(), regs.apply(reg.usize())?.op_and(imm.u64()))?
        end

    fun ref handle_and(reg1 : U8, reg2 : U8) =>
        try
            regs.update(reg1.usize(), regs.apply(reg1.usize())?.op_and(regs.apply(reg2.usize())?))?
        end 

    fun ref handle_or_imm(reg : U8, imm : U8) =>
        try
            regs.update(reg.usize(), regs.apply(reg.usize())?.op_or(imm.u64()))?
        end

    fun ref handle_or(reg1 : U8, reg2 : U8) =>
        try
            regs.update(reg1.usize(), regs.apply(reg1.usize())?.op_or(regs.apply(reg2.usize())?))?
        end 

    fun ref handle_add_imm(reg : U8, imm : U8) =>
        try
            regs.update(reg.usize(), regs.apply(reg.usize())?.add(imm.u64()))?
        end

    fun ref handle_add(reg1 : U8, reg2 : U8) =>
        try
            regs.update(reg1.usize(), regs.apply(reg1.usize())?.add(regs.apply(reg2.usize())?))?
        end 

    fun ref handle_sub_imm(reg : U8, imm : U8) =>
        try
            regs.update(reg.usize(), regs.apply(reg.usize())?.sub(imm.u64()))?
        end

    fun ref handle_sub(reg1 : U8, reg2 : U8) =>
        try
            regs.update(reg1.usize(), regs.apply(reg1.usize())?.sub(regs.apply(reg2.usize())?))?
        end 

    fun ref handle_mul_imm(reg : U8, imm : U8) =>
        try
            regs.update(reg.usize(), regs.apply(reg.usize())?.mul(imm.u64()))?
        end

    fun ref handle_mul(reg1 : U8, reg2 : U8) =>
        try
            regs.update(reg1.usize(), regs.apply(reg1.usize())?.mul(regs.apply(reg2.usize())?))?
        end 

    fun ref handle_div_imm(reg : U8, imm : U8) =>
        try
            regs.update(reg.usize(), regs.apply(reg.usize())?.div(imm.u64()))?
        end

    fun ref handle_div(reg1 : U8, reg2 : U8) =>
        try
            regs.update(reg1.usize(), regs.apply(reg1.usize())?.div(regs.apply(reg2.usize())?))?
        end 
    
    fun ref handle_push_imm(imm : U8) =>
        try
            stack.push(imm.u64())
            regs.update(4, regs.apply(4)? + 1)?
        end

    fun ref handle_push(reg : U8) =>
        try
            stack.push(regs.apply(reg.usize())?)
            regs.update(4, regs.apply(4)? + 1)?
        end

    fun ref handle_pop(reg : U8) =>
        try
            regs.update(reg.usize(), stack.pop()?)?
            regs.update(4, regs.apply(4)? - 1)?
        end

    fun ref handle_jmp_abs(addrH : U8, addrL : U8) =>
        pc = addrL.u64() + (256 * addrH.u64())

    fun ref handle_jz_abs(reg : U8, addrH : U8, addrL : U8) =>
        try
            if regs.apply(reg.usize())? == 0 then
                pc = addrL.u64() + (256 * addrH.u64())
            else
                pc = pc + 4
            end
        end
    
    fun ref handle_jnz_abs(reg : U8, addrH : U8, addrL : U8) =>
        try
            if regs.apply(reg.usize())? != 0 then
                pc = addrL.u64() + (256 * addrH.u64())
            else
                pc = pc + 4
            end
        end

    fun ref handle_jge_abs_imm(reg : U8, cmp : U8, addrH : U8, addrL : U8) =>
        try
            if regs.apply(reg.usize())? >= cmp.u64() then
                pc = addrL.u64() + (256 * addrH.u64())
            else
                pc = pc + 5
            end
        end

    fun ref handle_jle_abs_imm(reg : U8, cmp : U8, addrH : U8, addrL : U8) =>
        try
            if regs.apply(reg.usize())? <= cmp.u64() then
                pc = addrL.u64() + (256 * addrH.u64())
            else
                pc = pc + 5
            end
        end

    fun ref handle_je_abs_imm(reg : U8, cmp : U8, addrH : U8, addrL : U8) =>
        try
            if regs.apply(reg.usize())? == cmp.u64() then
                pc = addrL.u64() + (256 * addrH.u64())
            else
                pc = pc + 5
            end
        end

    fun ref handle_jne_abs_imm(reg : U8, cmp : U8, addrH : U8, addrL : U8) =>
        try
            if regs.apply(reg.usize())? != cmp.u64() then
                pc = addrL.u64() + (256 * addrH.u64())
            else
                pc = pc + 5
            end
        end

    fun ref handle_jne_abs(reg1 : U8, reg2 : U8, addrH : U8, addrL : U8) =>
        try
            if regs.apply(reg1.usize())? != regs.apply(reg2.usize())? then
                pc = addrL.u64() + (256 * addrH.u64())
            else
                pc = pc + 5
            end
        end

    fun ref handle_ret() =>
        try
            pc = stack.pop()?
            regs.update(4, regs.apply(4)? - 1)?
        end

    fun ref handle_call(addrH : U8, addrL : U8) =>
        try
            stack.push(pc + 3)
            regs.update(4, regs.apply(4)? + 1)?
            pc = addrL.u64() + (256 * addrH.u64())
        end

    fun ref handle_print_string(add_reg : U8, out : OutStream) =>
        try
            var cpt : U64
            var byte : U8
            cpt = 0
            byte = mem.apply((regs.apply(add_reg.usize())?.u64()+cpt).usize())?
            while byte != 0 do
                out.write([byte])
                cpt = cpt + 1
                byte = mem.apply((regs.apply(add_reg.usize())?.u64()+cpt).usize())?
            end
            out.write("\n")
        end