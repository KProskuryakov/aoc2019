import pytest
from day07 import IntCode, pipe_process
from asyncio import run


@pytest.mark.asyncio
async def test_dummy():
    result = await pipe_process(
        "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0", range(5)
    )
    assert result == (43210, (4, 3, 2, 1, 0),)


@pytest.mark.asyncio
async def test_first_part():
    with open("day07/input07.txt") as f:
        result = await pipe_process(f.read(), range(5))
        assert result == (116680, (3, 2, 4, 1, 0))


@pytest.mark.asyncio
async def test_second_dummy():
    result = await pipe_process(
        "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5",
        range(5, 10),
    )
    assert result == (139629729, (9, 8, 7, 6, 5),)


@pytest.mark.asyncio
async def test_second_part():
    with open("day07/input07.txt") as f:
        result = await pipe_process(f.read(), range(5, 10))
        assert result == (89603079, (7, 6, 5, 8, 9))
