from typing import List, Tuple


def parse_opcode(opcode: List[int], idx: int = 0) -> None:
    if opcode[idx] == 99:
        return
    elif opcode[idx] == 1:
        opcode[opcode[idx + 3]] = opcode[opcode[idx + 1]] + opcode[opcode[idx + 2]]
    elif opcode[idx] == 2:
        opcode[opcode[idx + 3]] = opcode[opcode[idx + 1]] * opcode[opcode[idx + 2]]
    return parse_opcode(opcode, idx + 4)


def evaluate_opcode(opcode: List[int], arg0: int, arg1: int) -> int:
    lst = [v for v in opcode]
    lst[1] = arg0
    lst[2] = arg1
    parse_opcode(lst)
    return lst[0]


def back_eval_opcode(opcode: List[int], expected_out: int) -> Tuple[int, int]:
    for arg0 in range(100):
        for arg1 in range(100):
            if evaluate_opcode(opcode, arg0, arg1) == expected_out:
                return arg0, arg1
    return -1, -1


if __name__ == "__main__":
    with open("day02/input.txt", "r") as f:
        txt = f.read()

    code = [int(num) for num in txt.split(",")]
    output = evaluate_opcode(code, 12, 2)
    print(output)

    n, v = back_eval_opcode(code, 19690720)
    print(100 * n + v)
