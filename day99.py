# '숫자 야구' 게임을 만들려고 합니다. 이 프로그램은 과정이 많기 때문에, 여러 파트로 나눠서 문제를 해결해 나갈 건데요. 먼저 이 레슨에서 프로그램 전체에 대해 설명해 드리겠습니다.

# 규칙
# 컴퓨터는 0과 9 사이의 서로 다른 숫자 3개를 무작위로 뽑습니다. 예를 들어서 컴퓨터가 5, 2, 3을 뽑을 수도 있고 6, 7, 4를 뽑을 수도 있는 거죠. 사용자는 숫자 3개를 입력해 컴퓨터가 뽑은 숫자들의 값과 위치를 맞춰야 합니다. 컴퓨터는 사용자가 입력한 숫자 3개에 대해서, 아래의 규칙대로 스트라이크(S)와 볼(B)의 개수를 알려 주는데요. 숫자의 값과 위치가 모두 일치하면 스트라이크(S)이고, 숫자의 값은 일치하지만 위치가 틀렸으면 볼(B)입니다. 예를 들어 컴퓨터가 1, 2, 3을 뽑았을 때, 사용자가 1, 3, 5를 입력하면, 1S(1의 값과 위치가 일치) 1B(3의 값만 일치)입니다. 기회에는 제한이 없지만, 몇 번의 시도 끝에 맞췄는지는 기록됩니다. 3S(숫자 3개의 값과 위치를 모두 맞춘 경우)가 나오면 게임이 끝납니다.

# 게임 진행 방식
# 0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.가 출력됩니다.
# 숫자 3개를 하나씩 차례대로 입력하세요.가 출력됩니다.
# 1번째 숫자를 입력하세요:가 출력되고, 사용자로부터 입력을 받습니다. 마찬가지로 2번째 숫자를 입력하세요:와 3번째 숫자를 입력하세요:가 출력되고, 사용자로부터 각각 입력을 받습니다. 만약 사용자가 중복되는 숫자를 입력하거나 범위에서 벗어나는 숫자를 입력하면, 사용자로부터 다시 입력 받습니다.
# 사용자가 올바르게 숫자 3개를 입력하면, 규칙에 따라 *S *B가 출력됩니다.
# 3S가 아닌 경우, 2번부터 다시 진행합니다.
# 사용자가 3S를 달성하면, 축하합니다. *번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.가 출력됩니다. 그리고 게임은 종료됩니다.
# 게임 진행 예시
# 0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.

# 숫자 3개를 하나씩 차례대로 입력하세요.
# 1번째 숫자를 입력하세요: 2
# 2번째 숫자를 입력하세요: 2
# 중복되는 숫자 입니다. 다시 입력하세요.
# 2번째 숫자를 입력하세요: 11
# 범위를 벗어나는 숫자입니다. 다시 입력하세요.
# 2번째 숫자를 입력하세요: 3
# 3번째 숫자를 입력하세요: 8
# 1S 1B

# 숫자 3개를 하나씩 차례대로 입력하세요.
# 1번째 숫자를 입력하세요: 8
# 2번째 숫자를 입력하세요: 2
# 3번째 숫자를 입력하세요: 0
# 1S 2B

# 숫자 3개를 하나씩 차례대로 입력하세요.
# 1번째 숫자를 입력하세요: 2
# 2번째 숫자를 입력하세요: 8
# 3번째 숫자를 입력하세요: 0
# 3S 0B

# 축하합니다. 3번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.