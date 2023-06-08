from myhdl import *

test_pwd = 'I_want_my_coffee'
real_flag = "I'm_n0t_4Dd1ct^^"
flag = test_pwd
print(len(flag))


@block
def acc_flag(input, output, write, enable, empty, clk):
    """
    A 16 bytes accumulator
    :param input: input to write
    :param output: output of the value
    :param write: if the output is writing in
    :param enable: if the device in enable
    :param empty: if the accumulator is empty
    :param clk: clock
    :return:
    """
    data = [Signal(intbv(ord(l))) for l in flag]
    pos = Signal(modbv(0, 0, 16))

    @always(clk.posedge)
    def core():
        output.next = data[pos]
        if enable:
            if write:
                data[pos].next = input
            else:
                data[pos].next = 0
            pos.next = pos + 1
        empty.next = all(x == 0 for x in data)

    return core


@block
def acc(input, output, write, enable, empty, full, clk):
    """
    A 16 bytes accumulator
    :param input: input to write
    :param output: output of the value
    :param write: if the output is writing in
    :param enable: if the device in enable
    :param empty: if the accumulator is empty
    :param clk: clock
    :return:
    """
    data_out = [Signal(intbv(0)) for _ in range(16)]
    pos = Signal(modbv(0, 0, 16))

    @always(clk.posedge)
    def core():
        output.next = data_out[pos]
        if enable:
            if write:
                data_out[(pos - 2) % 16].next = input
            else:
                data_out[(pos - 2) % 16].next = 0
            pos.next = pos + 1

    @always(clk.negedge)
    def flag_update():
        empty.next = all(x == 0 for x in data_out)
        full.next = all(x != 0 for x in data_out)
        print(f'{[int(i) for i in data_out]}')

    return core, flag_update


@block
def dff(input, output1, output2, clk):
    """
    FlipFlop
    :param input: Input of registry
    :param output: Value of registry
    :param sel: 3 bit selector to write one bit of output
    :param clk: clock
    :return:
    """
    memory = Signal(0)

    @always(clk.posedge)
    def core():
        output2.next = memory
        output1.next = input
        memory.next = input

    return core


@block
def add(a, b, z):
    @always_comb
    def core():
        z.next = a + b

    return core


@block
def xor(a, b, z):
    @always_comb
    def core():
        z.next = a ^ b

    return core


@block
def NOT(i, not_i):
    @always_comb
    def core():
        not_i.next = not i

    return core


@block
def system():
    clk = Signal(bool(0))
    enable = Signal(bool(1))
    check_f = Signal(bool(0))
    bus = [Signal(0) for _ in range(5)]

    acc_in_inst = acc_flag(Signal(bool(0)), bus[0], check_f, enable, Signal(bool(0)), clk)
    acc_out_inst = acc(bus[4], Signal(intbv(0)), enable, enable, Signal(bool(0)), check_f, clk)
    dff_inst = dff(bus[0], bus[1], bus[2], clk)
    xor_inst = xor(bus[1], bus[2], bus[3])
    add_inst = add(bus[2], bus[3], bus[4])
    NOT_inst = NOT(check_f, enable)

    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @always(clk.posedge)
    def stimulus():
        print(check_f, now())

    return clkgen, stimulus, acc_in_inst, acc_out_inst, dff_inst, xor_inst, add_inst, NOT_inst


simInst = system()
simInst.config_sim(trace=True)
simInst.run_sim(600)
