# ISSUE 74

- [ndb796/python-for-coding-test - issue74](https://github.com/ndb796/python-for-coding-test/issues/74)

> 여기서 알아둘 점은 왼쪽부터 (i - 3)번째 식량창고에 대해서는 고려할 필요가 없다. 왜냐하면 한 칸 이상 떨어진 식량창고는 항상 털 수 있기 때문이다. -p.222.

(i - 3)번째 식량창고가 한 칸 이상 떨어져있기 때문에 항상 털 수 있다고 설명하셨는데, 그렇지 않습니다.

```text
 0   1   2   3   4   5   6
[x] [o] [?] [?] [C] [ ] [ ]
```

위 그림에서,

- `x`는 털지 않은 창고, `o`는 턴 창고,
- `C`는 현위치, `?`는 이번에 루프에서 확인할 창고(i - 1), (i - 2)입니다.

따라서 위 그림에서 `i == 4`입니다. 만약 현재 인덱스인 `4`에서 (i - 2)를 털기로 마음먹었다면, (i -3)은 털지 못하는 창고가 돼버립니다.

그렇다면 (i - 3)번째 식량창고에 대해서는 고려하지 않았는데, 왜 정답이 맞는 건지 한참을 고민했습니다.  그 이유는 아래 코드에서 찾을 수 있었습니다.

```python
for i in range(2, n):
	d[i] = max(d[i - 1], d[i - 2] + array[i])
```

루프에서 고려하는 것은 "현재 위치의 앞의 창고(i - 1)를 터는 게 더 많이 버는가, 아니면 앞앞의 창고(i - 2)를 터는 것이 더 많이 버는가"가 아닙니다.

위 루프는 DP테이블을 기준으로 `d[i - 1]`의 값이 큰지, `d[i - 2] + array[i]`의 값이 큰지를 비교하여 `d[i]`의 값을 결정하고 있습니다. DP 테이블 `d`의 각 칸에는 "이 칸까지 도달하는 데 있어 가장 최선의 창고를 선택한 값"이 들어있기 때문에, 현재 개미 전사가 위치한 칸과 (i - 2)칸을 더한 게 더 많은 식량을 터는 길인지, 아니면 이번 칸은 스킵하고 (i - 1)칸을 선택하는 게 더 많은 식량을 터는 길인지를 비교해보는 겁니다.

결국 (i - 3)번째 식량창고에 대해서 고려하지 않는 게 아니라 `d[i - 3]`의 값을 고려하지 않는다고 보는 게 옳고, `d[i - 3]`을 검토하지 않는 이유는 (제가 위에 그린 도표를 기준으로 설명하자면)`d[0]`부터 `d[3]`까지 오면서 선택할 수 있는 최선의 값이 각 칸에 들어있고, 개미 전사는 `d[4]`를 털기 전에, "`d[2]`의 값에 `d[4]`의 값을 더해서 가져올 지", 아니면 "`d[4]`의 값을 취하지 않는 손해를 불구하고라도 `d[3]`을 가져갈 지"를 선택해야 하기 때문입니다.

너무 길게 썼으니 한 줄 요약하자면 "d[i - 3]을 고려하지 않는 이유는 d[i - 2]와 d[i - 1]는 해당 칸에 도달하기 까지 가장 많이 털 수 있는 식량의 수가 기록돼 있기 때문이다."입니다.

설명이 잘 됐는지 모르겠네요. 이 글을 남기기까지 여러 번 정리를 해봤는데, 이 설명이 맞는 것 같아 이슈를 남겨봅니다. 혹시 제가 틀렸다면 번거로우시겠지만 설명을 부탁드리겠습니다.