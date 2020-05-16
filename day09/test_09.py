import pytest
from day09 import IntCode
from asyncio import run, Queue


@pytest.mark.asyncio
async def test_quine():
    output = Queue()

    program = IntCode(
        "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99", Queue(), output
    )

    await program.process()

    final_out = [await output.get() for _ in range(output.qsize())]

    assert final_out == [
        109,
        1,
        204,
        -1,
        1001,
        100,
        1,
        100,
        1008,
        100,
        16,
        101,
        1006,
        101,
        0,
        99,
    ]


@pytest.mark.asyncio
async def test_large_num():
    output = Queue()

    program = IntCode("104,1125899906842624,99", Queue(), output)

    await program.process()

    final_out = [await output.get() for _ in range(output.qsize())]

    assert final_out == [1125899906842624]


@pytest.mark.asyncio
async def test_first_part():
    iq = Queue()
    await iq.put(1)
    oq = Queue()

    with open("day09/input09.txt") as f:
        program = IntCode(f.read(), iq, oq)

        await program.process()

        final_out = [await oq.get() for _ in range(oq.qsize())]

        assert final_out == [3280416268]


@pytest.mark.asyncio
async def test_second_part():
    iq = Queue()
    await iq.put(2)
    oq = Queue()

    with open("day09/input09.txt") as f:
        program = IntCode(f.read(), iq, oq)

        await program.process()

        final_out = [await oq.get() for _ in range(oq.qsize())]

        assert final_out == [80210]
