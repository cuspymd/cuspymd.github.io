---
layout: post
title:  "A Complete Exploratory Data Analysis and Visualization for Text Data"
---
[A Complete Exploratory Data Analysis and Visualization for Text Data](https://towardsdatascience.com/a-complete-exploratory-data-analysis-and-visualization-for-text-data-29fb1b96fb6a)

텍스트 데이터에 대한 탐색적 데이터 분석과 Visualization에 대한 미디엄 글.
예제도 많고 꽤 정성들여 쓴 글이다. 하지만 예제 코드의 실행 방법에 대해서는 나와 있지 않아, 코드를 실행하려면 꽤 애를 먹는다.
예제에 쓰인 텍스트 데이터도 캐글 데이터라서 [캐글 사이트]에 로그인한 후 파일을 다운로드받아야 한다.

# Plotly

텍스트 데이터 분석에 문외한이라 위 글에 나오는 많은 모듈이 생소한데,
그 중에서 차트를 그릴 때 사용하는 [plotly]라는 모듈은 꽤 흥미롭다.
데이터에 대한 단순 차트 이미지를 생성해주는 게 아니라 마우스 동작에 반응하는 인터렉티브 차트를 만들어 준다.
예를 들어 아래처럼.

{% raw %}
<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width="100%" height="500" src="https://plot.ly/~cuspymd/28.embed"></iframe>
{% endraw %}


단순히 호버링에만 반응하는 게 아니라 줌인, 줌아웃 이나 그외 여러 동작이 가능하다.

장점이 있으면 단점도 있는 법. 온라인으로만 동작하는 큰 단점이 있다.
실제로 예제 코드를 돌릴 때는 자신의 plotly 계정과 api key 를 코드 상에 입력해줘야 한다.

데이터에 대해 플롯 그리는 함수를 호출하면 실제 데이터가 plotly 서버에 전달되고,
데이터와 플롯 차트가 plotly 서버 내 자신의 계정에 저장되는 방식인 것 같다.
그리고 자신 계정의 링크를 공유하면 되는 데,
실제 데이터가 서버로 날아가기 때문에 회사 내에서는 절대 쓸 수 없는 모듈.
참 좋은데 써먹을 방법이 없다.

아래는 위 글의 코드를 colab 에서 바로 실행 가능하도록 옮겨놓은 것이다.
하지만 막상 실행을 위해서는 위의 캐글 데이터를 다운받아 업로드해야 하며
노트북 중간 부분에 코멘트되어 있는 plotly 계정 입력 부분을 코멘트 해제한 후 자신의 계정 정보를 입력해야 한다.
어우 쉽지 않아ㅡ.ㅡ;;

[colab 예제 코드](https://colab.research.google.com/drive/1NGFhFdTi-MQIr1-ZXbRZ0ce5vAS9_LpI)

> 위 글 후반부의 `Finding characteristic terms and their associations` 이하 부분은 `nlp` 가 제대로 로딩되지 않는 문제가 있어서 생략했다. 쿨럭쿨럭;;

[캐글 사이트]: https://www.kaggle.com/nicapotato/womens-ecommerce-clothing-reviews
[plotly]: https://plot.ly
