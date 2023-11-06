# GIT

#  여러 번의 수정을 거쳐 완성본을 만들 때, 우리는 나중에 필요해질 상황을 염려해 중간 작업물들도 모두 저장해둔다. 하지만 이런 상황에서는 자료는 보존되지만, 파일의 어떤 내용이 수정됐는지 알 수 없고 중간 내용을 보고 싶어도 어떤 파일을 봐야 하는지 헷갈려 결국 모두 확인해야 하는 경험을 한 적이 있다. 이런 일을 방지하려면 **‘버전 관리’**를 해야 한다.
#  버전 관리란 파일의 변화를 시간에 따라 기록했다가 나중에 특정 시점의 버전을 다시 꺼내올 수 있는 시스템이다. 이런 버전 관리를 할 수 있는 것이 **Git**이다.

#  버전 관리를 하면 크게 두 가지의 장점이 있다.
# 첫 번째로는 ‘완성본이 만들어지기까지’의 지난 과정을 확인 가능하다.
# 두 번째로는 문제가 발생했을 때 이전 버전으로 돌아갈 수 있다.

#  깃(Git)은 이런 수정한 내역들을 하나의 버전으로 저장할 수 있게 해주고, 협업할 때에도 쓰인다.
# 보통 개발할 때에는 각 기능을 여러 개발자가 분담해서 개발 진행한다. 이렇게 여러 개발자가 만든 코드들을 깃을 이용해 동시에 합칠 수 있다.

#  그래서 개발자가 꼭 갖춰야 하는 역량으로는 자료구조, 알고리즘, 객체 지향 프로그래밍 등 많지만 그중에 Git도 있다.

#  깃은 **[리누스 토발즈(Linus Torvalds)](https://ko.wikipedia.org/wiki/%EB%A6%AC%EB%88%84%EC%8A%A4_%ED%86%A0%EB%A5%B4%EB%B0%9C%EC%8A%A4)**라는, 리눅스(Linux)라고 하는 운영 체제를 만든 사람이 만들었다. 리누스 토발즈는 리눅스를 만든 이후에 BitKeeper라고 하는 툴(Tool)로 리눅스의 각 버전들(ver1, ver2, ver3 ...)을 관리하고 있었다. 그런데 리눅스 커뮤니티의 개발자 한 명이 BitKeeper의 내부 동작 원리를 분석하려고 했던 일을 계기로 리눅스 커뮤니티와 BitKeeper 측의 사이가 틀어지게 되었다. 이때문에 리눅스 커뮤니티 측에 대해서 BitKeeper는 유료화되었고, 리누스 토발즈는 BitKeeper를 대신할 다른 버전 관리 시스템을 찾아보기 시작했는데, 자신의 마음에 드는 버전 관리 툴을 찾지 못했다. 그래서 리누스 토발즈는 본인이 직접 버전 관리 프로그램을 만들어버렸다. 이렇게 만들어진 버전 관리 프로그램이 바로 깃이다.

# 깃은 당시에 아래와 같은 목표를 갖고 설계 및 제작되었다.

# - 빠른 속도
# - 단순한 디자인
# - 비선형적 개발 지원(수천 개의 브랜치를 병행할 수 있음)
# - 완전 분산형 시스템
# - 리눅스와 같은 거대한 프로젝트도 속도 저하의 문제없이 관리할 수 있는 시스템

# 깃은 버전 관리(Version Control), 협업(Cooperation)에 필요한 여러 요소들이 고려되었기 때문에, 사용성이 굉장히 좋은 프로그램이 될 수 있었다.

# "깃은 당신의 마음에 따라 그 어떤 것으로도 해석될 수 있다.

# 1. **[유닉스 커맨드](https://www.codeit.kr/courses/unix-command-line/topics/unix-commands)**에서 사용되는 명령어 이름을 제외한 랜덤한 알파벳 3글자의 조합
# 2. 멍청하고 단순한(이런 특성을 지닌 아무 단어로 해석되어도 좋다는 의미)
# 3. global information tracker의 약자
# 4. goddamn idiotic truckload of sh*t 이라는 욕설의 약자"

# 이렇게 깃이라는 이름은 처음 만들어질 때부터 다양한 의미로 해석될 가능성을 갖고 탄생했다. 뭔가 리누스 토발즈의 독특함이 느껴지는 부분인데, 혹시 이 기록을 직접 살펴보고 싶을 땐 **[이 링크](https://github.com/git/git/commit/e83c5163316f89bfbde7d9ab23ca2e25604af290)**를 클릭해보자.

# 깃은 버전 관리와 동시 협업에 특화되어 있지만 한 가지 기능이 더 있다. 바로 자신의 작업물을 다른 컴퓨터에 보낼 수 있는 것이다.