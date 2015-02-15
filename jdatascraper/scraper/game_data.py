# -*- coding: utf-8 -*-

test_game_data = u'''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja"><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>J. League Data Site</title>
<meta http-equiv="content-style-type" content="text/css" />
<meta http-equiv="content-script-type" content="text/javascript" />
<meta name="copyright" content="Copyright &copy; J. League Data Site. All Rights Reserved." />
<link rel="icon" href="/favicon.ico" type="image/x-icon" />
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="stylesheet" type="text/css" href="/css/smoothness/jquery-ui-1.10.0.custom.min.css" />
<link rel="stylesheet" type="text/css" href="/css/style.css" media="all" />
<link rel="stylesheet" type="text/css" href="/css/custom.css" media="all" />
<script type="text/javascript" src="/js/message.ja.js"></script>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-48437066-1', {'cookieName': '_ds', 'cookieDomain': 'data.j-league.or.jp'});
  ga('send', 'pageview');

</script>
<script type="text/javascript" src="/js/rollover.js?type=_o" charset="utf-8"></script>
<script type="text/javascript" src="/js/jquery-1.9.0.js"></script>
<script type="text/javascript" src="/js/jquery-migrate-1.0.0.min.js"></script>
<script type="text/javascript" src="/js/jquery-ui-1.10.0.custom.min.js"></script>
<script type="text/javascript" src="/js/jquery.ui.datepicker-ja.js"></script>
<script type="text/javascript" src="/js/jquery.form.js"></script>
<script type="text/javascript" src="/js/spin.min.js"></script>
<script type="text/javascript" src="/js/jquery-app.js"></script>
<script type="text/javascript" src="/js/jquery.tablesorter.js"></script>
<script type="text/javascript" src="/js/jquery.ah-placeholder.js"></script>
<script type="text/javascript" src="/js/common.js"></script>
<style type="text/css">
.errors {
	color: #c00;

	font-size:1.2em;
}

#loginForm p {
	text-align: center;
}

#loginForm table {
	width: 360px;
	margin: 0 auto;
}

#loginForm th,#loginForm td {
	padding: 2px 4px;
	vertical-align: top;
}

#loginForm th {
	text-align: right;
}

#loginForm td input {
	width: 96%;
}

#loginForm td #persistent-badge {
	width: auto;
	font-size:70%;
}

#loginForm td.errors li {
	font-size: small;
}
</style>
</head>
<body class="ja h-mb0 search">
<div id="wrapper"><!-- #BeginLibraryItem "/Library/header.lbi" -->
<div id="header">
	<div id="header-area">
		<h1 id="logo">
			<a href="/SFTP01/" title="J. League Data Site" class="img-bg">J.League Data Site</a>
		</h1>
		<div id="hnav">
			<ul class="">
				<li id="hnav-official-site">
					<a href="http://www.j-league.or.jp/" target="_blank"></a>
				</li>
				<li id="hnav-login"><a href="#" title=""></a></li>
						<li id="hnav-ja" class="hnav-base"><a href="/?lang=ja" title="Japanese">Japanese</a></li>
				<li id="hnav-en" class="hnav-base"><a href="/?lang=en" title="English">English</a></li>
			</ul>
			</div>
	</div>
	<div id="gnav-area">
		<ul id="gnav">
			<li id="gnav00"><a href="/SFTP01/" title="HOME" class="png-bg">HOME</a></li>
			<li id="gnav01"><a href="/SFMS01/" title="日程・結果" class="png-bg">日程・結果</a></li>
			<li id="gnav02"><a href="/SFRT01/" title="順位表" class="png-bg">順位表</a></li>
			<li id="gnav03"><a href="/SFIN01/" title="お知らせ" class="png-bg">お知らせ</a></li>
			<li id="gnav04"><a href="/SFTD01/" title="通算データ" class="png-bg">通算データ</a></li>
			<li id="gnav05"><a href="/SFPR01/" title="出場記録" class="png-bg">出場記録</a></li>
			<li id="gnav06"><a href="/SFIX02/" title="選手・監督・審判" class="png-bg">選手・監督・審判</a></li>
			</ul>
	</div>
</div><div id="container">
<div id="contents" class="one-column">
			<div id="contents" class="one-column">
			<form action="#" method="get">
				<!-- 印刷エリア -->
					<div class="print-area">
						<!-- 戻るボタンエリア -->
						<div class="btn-back float-l">
						<p class="btn-base h20 radius-2 col-2 bd-gray"><a href="javascript:history.back()"><span class="icon-back png-bg">戻る</span></a></p>
						</div>
						<!-- Play by Play（リンク） -->
						<!-- 印刷ページへ(リンク)-->
						<p class="btn-base h22 radius-1 col-1"><a href="#" id="print_button"><span class="icon-print png-bg">印刷ページへ</span></a></p>
					</div>
					<!-- タイトルエリア -->
					<div class="t-base-area">
						<h2 class="t-base">公式記録</h2>
						<p class="t-txt">２０１４Ｊリーグ　ディビジョン１
								&nbsp;第１節第１日</p>
					</div>

					<div class="t-base-area print-title">
						<h2 class="t-base">公式記録</h2>
						<p class="t-txt">２０１４Ｊリーグ　ディビジョン１
								&nbsp;第１節第１日</p>
					</div>
					<!-- ヘッダコメントエリア -->
					<div class="score-board-area">
							<div class="score-board-box">
								<!-- A1　試合結果情報エリア　Start -->
								<div class="score-board-main">
									<div class="score-board-t">
										<div class="score-board-b">
											<table>
												<tr>
													<th id="team-name-l" class="team-name" rowspan="2">
														<a href="http://www.jleague.jp/club/cosaka/profile/">セレッソ大阪</a>
															</th>
													<td class="score" rowspan="2">0</td>
													<td class="time">
														<dl>
																<dd class="left-area">0</dd>
																<dt class="png-bg">前半</dt>
																<dd class="right-area">0</dd>
															</dl>
															<dl>
																<dd class="left-area">0</dd>
																<dt class="png-bg">後半</dt>
																<dd class="right-area">1</dd>
															</dl>
															</td>
													<td class="score" rowspan="2">1</td>
													<th id="team-name-r" class="team-name" rowspan="2">
														<a href="http://www.jleague.jp/club/hiroshima/profile/">サンフレッチェ広島</a>
															</th>
												</tr>
											</table>
										</div>
									</div>
								</div>
								<!-- A1　試合結果情報エリア　End -->
								<!-- A2　得点イベント情報エリア　Start -->
										<div class="score-board-pk mb10">
											<div class="score-board-pk-t">
												<div class="score-board-pk-b">
													<table>
														<tr>
															<td class="left-area">
																<table>
																	</table>
															</td>
															<th>得点</th>
															<td class="right-area">
																<table>
																	<tr>
																			<td>
																				71'　　　</td>
																			<td>
																				塩谷　司</td>
																		</tr>
																	</table>
															</td>
														</tr>
													</table>
												</div>
											</div>
										</div>
										<!-- A2　得点イベント情報エリア　End -->
									<!-- A4　キック数情報エリア　Start -->
									<div class="score-board-other">
										<dl class="score-board-base">
											<dd class="left-area"><div class="left-score">12</div></dd>
											<dt>SH</dt>
											<dd class="right-area"><div class="right-score">10</div></dd>
										</dl>
										<dl class="score-board-base">
											<dd class="left-area"><div class="left-score">4</div></dd>
											<dt>CK</dt>
											<dd class="right-area"><div class="right-score">2</div></dd>
										</dl>
										<dl class="score-board-base">
											<dd class="left-area"><div class="left-score">17</div></dd>
											<dt>FK</dt>
											<dd class="right-area"><div class="right-score">13</div></dd>
										</dl>
									</div>
									<!-- A4　キック数情報エリア　End -->
								</div>
						</div>
						<div class="two-column-table-area two-column-table-area840">
								<div class="two-column-table-box two-column-table-box-type01">
									<div class="two-column-table-box-l">
										<!-- A5　先発メンバー情報エリア　Start -->
										<h3 class="two-column-table-t-base">セレッソ大阪</h3>
										<h4 class="two-column-table-st-base">先発</h4>
										<div class="two-column-table-title">
											<table>
												<tbody>
													<tr>
														<th class="position">POSITION</th>
														<th class="number">NUMBER</th>
														<th class="name">NAME</th>
														<th class="time">TIME</th>
													</tr>
												</tbody>
											</table>
										</div>
										<div class="two-column-table-base">
											<table>
												<tbody>
													<tr>
															<td class="position"><span>GK</span></td>
															<td class="number">21</td>
															<td class="name">
																キム　ジンヒョン</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>DF</span></td>
															<td class="number">4</td>
															<td class="name">
																藤本　康太</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>DF</span></td>
															<td class="number">14</td>
															<td class="name">
																丸橋　祐介</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>DF</span></td>
															<td class="number">17</td>
															<td class="name">
																酒本　憲幸</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>DF</span></td>
															<td class="number">23</td>
															<td class="name">
																山下　達也</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">2</td>
															<td class="name">
																扇原　貴宏</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">5</td>
															<td class="name">
																長谷川　アーリアジャスール</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">6</td>
															<td class="name">
																山口　蛍</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">13</td>
															<td class="name">
																南野　拓実</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>FW</span></td>
															<td class="number">8</td>
															<td class="name">
																柿谷　曜一朗</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>FW</span></td>
															<td class="number">10</td>
															<td class="name">
																フォルラン</td>
															<td class="time"></td>
														</tr>
													</tbody>
											</table>
										</div>
										<!-- A5　先発メンバー情報エリア　End -->
									</div>

									<div class="two-column-table-box-r">
										<!-- A5　先発メンバー情報エリア　Start -->
										<h3 class="two-column-table-t-base">サンフレッチェ広島</h3>
										<h4 class="two-column-table-st-base">先発</h4>
										<div class="two-column-table-title">
											<table>
												<tbody>
													<tr>
														<th class="position">POSITION</th>
														<th class="number">NUMBER</th>
														<th class="name">NAME</th>
														<th class="time">TIME</th>
													</tr>
												</tbody>
											</table>
										</div>
										<div class="two-column-table-base">
											<table>
												<tbody>
													<tr>
															<td class="position"><span>GK</span></td>
															<td class="number">1</td>
															<td class="name">
																林　卓人</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>DF</span></td>
															<td class="number">33</td>
															<td class="name">
																塩谷　司</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>DF</span></td>
															<td class="number">5</td>
															<td class="name">
																千葉　和彦</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>DF</span></td>
															<td class="number">4</td>
															<td class="name">
																水本　裕貴</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">2</td>
															<td class="name">
																ファン　ソッコ</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">6</td>
															<td class="name">
																青山　敏弘</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">30</td>
															<td class="name">
																柴﨑　晃誠</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">16</td>
															<td class="name">
																山岸　智</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">9</td>
															<td class="name">
																石原　直樹</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">24</td>
															<td class="name">
																野津田　岳人</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>FW</span></td>
															<td class="number">11</td>
															<td class="name">
																佐藤　寿人</td>
															<td class="time"></td>
														</tr>
													</tbody>
											</table>
										</div>
										<!-- A5　先発メンバー情報エリア　End -->
									</div>
								</div>

								<div class="two-column-table-box two-column-table-box-type01">
									<div class="two-column-table-box-l">
										<!-- A6　控えメンバー情報エリア　Start -->
										<h4 class="two-column-table-st-base">控え</h4>
										<div class="two-column-table-base">
											<table>
												<tbody>
													<tr>
															<td class="position"><span>GK</span></td>
															<td class="number">1</td>
															<td class="name">
																武田　博行</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>DF</span></td>
															<td class="number">3</td>
															<td class="name">
																染谷　悠太</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>DF</span></td>
															<td class="number">7</td>
															<td class="name">
																新井場　徹</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">30</td>
															<td class="name">
																ゴイコ　カチャル</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">11</td>
															<td class="name">
																楠神　順平</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>FW</span></td>
															<td class="number">9</td>
															<td class="name">
																永井　龍</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>FW</span></td>
															<td class="number">20</td>
															<td class="name">
																杉本　健勇</td>
															<td class="time"></td>
														</tr>
													</tbody>
											</table>
										</div>
										<!-- A6　控えメンバー情報エリア　End -->
									</div>
									<div class="two-column-table-box-r">
										<!-- A6　控えメンバー情報エリア　Start -->
										<h4 class="two-column-table-st-base">控え</h4>
										<div class="two-column-table-base">
											<table>
												<tbody>
													<tr>
															<td class="position"><span>GK</span></td>
															<td class="number">13</td>
															<td class="name">
																増田　卓也</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>DF</span></td>
															<td class="number">17</td>
															<td class="name">
																パク　ヒョンジン</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">28</td>
															<td class="name">
																丸谷　拓也</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">25</td>
															<td class="name">
																茶島　雄介</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">36</td>
															<td class="name">
																川辺　駿</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>MF</span></td>
															<td class="number">37</td>
															<td class="name">
																宮原　和也</td>
															<td class="time"></td>
														</tr>
													<tr>
															<td class="position"><span>FW</span></td>
															<td class="number">29</td>
															<td class="name">
																浅野　拓磨</td>
															<td class="time"></td>
														</tr>
													</tbody>
											</table>
										</div>
										<!-- A6　控えメンバー情報エリア　End -->
									</div>
								</div>
								<div class="two-column-table-box two-column-table-box-type01">
									<div class="two-column-table-box-l">
										<!-- A7　交代イベント情報エリア　Start -->
											<h4 class="two-column-table-st-base">交代</h4>
											<div class="two-column-table-base">
												<table>
													<tbody>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="change">

																		▽
																		</td>
																<td class="name">
																	フォルラン</td>
																<td class="time">81'</td>
															</tr>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="change">

																		▲
																		</td>
																<td class="name">
																	杉本　健勇</td>
																<td class="time"></td>
															</tr>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="change">

																		▽
																		</td>
																<td class="name">
																	扇原　貴宏</td>
																<td class="time">85'</td>
															</tr>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="change">

																		▲
																		</td>
																<td class="name">
																	ゴイコ　カチャル</td>
																<td class="time"></td>
															</tr>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="change">

																		▽
																		</td>
																<td class="name">
																	長谷川　アーリアジャスール</td>
																<td class="time">90'+3</td>
															</tr>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="change">

																		▲
																		</td>
																<td class="name">
																	楠神　順平</td>
																<td class="time"></td>
															</tr>
														</tbody>
												</table>
											</div>
											<!-- A7　交代イベント情報エリア　End -->
										</div>
									<div class="two-column-table-box-r">
										<!-- A7　交代イベント情報エリア　Start -->
											<h4 class="two-column-table-st-base">交代</h4>
											<div class="two-column-table-base">
												<table>
													<tbody>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="change">

																		▽
																		</td>
																<td class="name">
																	ファン　ソッコ</td>
																<td class="time">61'</td>
															</tr>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="change">

																		▲
																		</td>
																<td class="name">
																	パク　ヒョンジン</td>
																<td class="time"></td>
															</tr>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="change">

																		▽
																		</td>
																<td class="name">
																	佐藤　寿人</td>
																<td class="time">65'</td>
															</tr>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="change">

																		▲
																		</td>
																<td class="name">
																	浅野　拓磨</td>
																<td class="time"></td>
															</tr>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="change">

																		▽
																		</td>
																<td class="name">
																	山岸　智</td>
																<td class="time">87'</td>
															</tr>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="change">

																		▲
																		</td>
																<td class="name">
																	宮原　和也</td>
																<td class="time"></td>
															</tr>
														</tbody>
												</table>
											</div>
											<!-- A7　交代イベント情報エリア　End -->
										</div>
								</div>

								<div class="two-column-table-box two-column-table-box-type01">
									<div class="two-column-table-box-l">
										<!-- A8　警告イベント情報エリア　Start -->
											<h4 class="two-column-table-st-base">警告</h4>
											<div class="two-column-table-base">
												<table>
													<tbody>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="number">&nbsp;</td>
																<td class="name">
																	山下　達也</td>
																<td class="time">38'</td>
															</tr>
														</tbody>
												</table>
											</div>
											<!-- A8　警告イベント情報エリア　End -->
										</div>
									<div class="two-column-table-box-r">
										<!-- A8　警告イベント情報エリア　Start -->
											<h4 class="two-column-table-st-base">警告</h4>
											<div class="two-column-table-base">
												<table>
													<tbody>
														<tr>
																<td class="position">&nbsp;</td>
																<td class="number">&nbsp;</td>
																<td class="name">
																	柴﨑　晃誠</td>
																<td class="time">61'</td>
															</tr>
														</tbody>
												</table>
											</div>
											<!-- A8　警告イベント情報エリア　End -->
										</div>
								</div>

								<div class="two-column-table-box two-column-table-box-type01">
									<div class="two-column-table-box-l">
										</div>
									<div class="two-column-table-box-r">
										</div>
								</div>

								<div class="two-column-table-box two-column-table-box-type01">
									<div class="two-column-table-box-l">
										<!-- A10　監督情報エリア　Start -->
											<h4 class="two-column-table-st-base">
												監督</h4>
											<div class="two-column-table-base">
												<table>
													<tbody>
														<tr>
															<td class="position">&nbsp;</td>
															<td class="number">&nbsp;</td>
															<td class="name">
																ランコ　ポポヴィッチ</td>
														</tr>
													</tbody>
												</table>
											</div>
										<!-- A10　監督情報エリア　End -->
										</div>
									<div class="two-column-table-box-r">
										<!-- A10　監督情報エリア　Start -->
											<h4 class="two-column-table-st-base">
												監督</h4>
											<div class="two-column-table-base">
												<table>
													<tbody>
														<tr>
															<td class="position">&nbsp;</td>
															<td class="number">&nbsp;</td>
															<td class="name">
																森保　一</td>
														</tr>
													</tbody>
												</table>
											</div>
										<!-- A10　監督情報エリア　End -->
										</div>
								</div>
							</div>
						<!-- IN・OUTマーク凡例 -->
						<p class="two-column-table-txt">▲：IN　▽：OUT</p>
						<!-- A12　試合情報エリア　Start -->
					<div class="two-column-table-bottom">
						<table>
							<thead>
								<tr>
									<th>日付</th>
									<th>キックオフ時刻</th>
									<th>スタジアム</th>
									<th>入場者数</th>
									<th>天候</th>
									<th>気温</th>
									<th>湿度</th>
								</tr>
							</thead>
							<tbody>
								<tr>
									<td>2014/03/01</td>
									<td>
										14:04</td>
									<td>
										ヤンマースタジアム長居</td>
									<td>
										37,079<!-- 日本語のみ表示 -->
														人</td>
									<td>
										雨</td>
									<td>
										12.3<img src="/images/common/icon_cel2.gif" class="img-base"><img src="/images/common/icon_cel.png" class="img-base-print">
												</td>
									<td>
										60%</td>
								</tr>
							</tbody>
						</table>
						<div class="clearbox">
							<dl>
								<dt>主審</dt>
								<dd>
									家本　政明</dd>
							</dl>
							<dl>
								<dt>副審</dt>
								<dd>
									岡野　宇広
												,
											村井　良輔</dd>
							</dl>
							<dl class="mr0">
							<dt>第4の審判員</dt>
								<dd>
									前田　拓哉</dd>
							</dl>
							</div>
					</div>
					<!-- A12　試合情報エリア　End -->
					<!-- フッターコメントエリア -->
					<!-- 戻るボタンエリア -->
					<div class="btn-back">
						<p class="btn-base h20 radius-2 col-2 bd-gray"><a href="javascript:history.back()"><span class="icon-back png-bg">戻る</span></a></p>
					</div>
				</form>
		</div>
	</div>
	</div>
<div id="footer">
		<div id="footer-bnr-area">
			<style>

				#footer-bnr-area ul{
					margin-bottom: 10px;
				}

				#footer-bnr-area ul.col-3 li{
					width:225px;
					padding: 0 30px;
				}

				#footer-bnr-area ul.col-2 li{
					width:367.5px;
					padding: 0 30px;
				}

				#footer-bnr-area ul.col-1 li{
					width: 795px;
					padding: 0 30px;
				}

			</style>
			</div>
		<div id="footer-sponsor-area-index">
			</div>
		<div id="footer-bottom-area">
			<div id="footer-bottom-area">
				<div id="pagetop-area">
					<p id="pagetop"><a href="#wrapper" title="HOME">HOME</a></p>
				</div>
				<div id="footer-area">
					<div id="footer-box">
						<h3 id="footer-box-title"><a href="/SFTP01/">HOME</a></h3>
						<div id="fnav-area">
							<dl>
								<dt><a href="/SFMS01/">日程・結果</a></dt>
								<dd><a href="/SFMS01/">試合日程・試合結果</a></dd>
							</dl>
							<dl>
							    <dt><a href="/SFRT01/">順位表</a></dt>
								<dd><a href="/SFRT01/">順位表</a></dd>
								<dd><a href="/SFRT03/">年間順位表</a></dd>
								<dd><a href="/SFRT05/">節別動向</a></dd>
									<dd><a href="/SFRT06/">戦績表</a></dd>
									<dd><a href="/SFRT07/">反則ポイント</a></dd>
									<dd><a href="/SFRT08/">チーム別集計結果</a></dd>
								<dd><a href="/SFRT09/">得点順位表</a></dd>
							</dl>
							<dl>
							    <dt><a href="/SFIN01/">お知らせ</a></dt>
								<dd><a href="/SFIN01/">選手登録追加抹消のお知らせ</a></dd>
								<dd><a href="/SFIN02/">役員・スタッフ登録追加抹消のお知らせ</a></dd>
								<dd><a href="/SFIN03/">出場停止選手のお知らせ</a></dd>
								<dd><a href="/SFIN04/">公式記録訂正のお知らせ</a></dd>
								</dl>
							<dl>
							    <dt><a href="/SFTD11/">通算データ</a></dt>
								<dd><a href="/SFTD01/">通算勝敗表</a></dd>
									<dd><a href="/SFTD02/">スタジアム別通算勝敗表</a></dd>
									<dd><a href="/SFTD03/">天候別勝敗表</a></dd>
									<dd><a href="/SFTD04/">対戦データ一覧</a></dd>
									<dd><a href="/SFTD05/">状況別勝敗表</a></dd>
									<dd><a href="/SFTD06/">時間帯別得失点</a></dd>
									<dd><a href="/SFTD07/">通算出場試合数ランキング</a></dd>
									<dd><a href="/SFTD08/">通算得点ランキング</a></dd>
									<dd><a href="/SFTD09/">ハットトリック一覧</a></dd>
								<dd><a href="/SFTD11/">入場者一覧</a></dd>
								<dd><a href="/SFTD12/">年度別入場者推移</a></dd>
									<dd><a href="/SFTD14/">クラブ別入場者数</a></dd>
									<dd><a href="/SFTD15/">記念ゴール</a></dd>
								</dl>
							<dl>
								    <dt><a href="/SFPR01/">出場記録</a></dt>
									<dd><a href="/SFPR01/">選手出場記録</a></dd>
									<dd><a href="/SFPR02/">警告・退場・出場停止</a></dd>
								</dl>
							<dl>
							    <dt><a href="/SFIX02/">選手・監督・審判</a></dt>
								<dd><a href="/SFIX02/">登録選手一覧</a></dd>
								<dd><a href="/SFIX05/">役員・チームスタッフ一覧</a></dd>
								<dd><a href="/SFIX08/">Jリーグ担当主審/副審リスト</a></dd>
									</dl>
							</div>
						<p id="copyright">© JAPAN PROFESSIONAL FOOTBALL LEAGUEJ.LEAGUE MEDIA PROMOTION,INC.J. LEAGUE PHOTOS,INC.J.LEAGUE ENTERPRISE,INC.ALL RIGHTS RESERVED. </p>
					</div>
				</div>
			</div>
		</div>
	</div><!-- #EndLibraryItem --></div>
<div id="spin"></div>
<!--[if lt IE 8]>
<script type="text/javascript" src="/js/DD_belatedPNG.js"></script>
<script type="text/javascript">
	DD_belatedPNG.fix('img, .png-bg');
</script>
<![endif]-->
<script type="text/javascript">
$(function() {

	var selectDate = function (){
		$.loadAsDialog({
			url: '/selectCurrentDate'
		}, {
			width : 220,
			height : 250,
			title : '日付選択',
			buttons: {},
			open: function() {
				$dialog = $(this);
				$("#datepicker", this).datepicker({
					dateFormat : 'yy/mm/dd',
					onSelect : function(date, datepicker){
						$.json({
							url: '/setupCurrentDate',
							data : {'currentDate' : date},
							complete : function(XMLHttpRequest, textStatus){
								//
								//
								$.repost(null, true, false);
								//
							}
						});
					}
				});
			},

			close: function() {
				$.json({
					url: '/setupCurrentDate',
					data : {'currentDate' : '2015/02/11 00:00'},
					complete : function(XMLHttpRequest, textStatus){
						document.location.reload(true);
					}
				});
			}
		});
	};

	//

	//
	$('#hnav-login a').click(function() {
		login();
	});


	$('#hnav-login-en a').click(function() {
		login();
	});


	function login() {
		//
		if(location.protocol != 'https:') {
			$.repost({login:true}, true, false);
			return;
		}
		//

		$.loadAsDialog({
			url: '/initLogin'
		}, {
			width : 400,
			height : 170,
			title : 'ログイン',
			buttons: {},
			open: function() {
				$this = $(this);
				$('input[name=login]', this).click(function() {
					$.json({
						url : '/login',
						data : {
							username: $('input[name=username]', $this).val(),
							password: $('input[name=password]', $this).val(),
							persistentBadge: $('input[name=persistentBadge]', $this).prop('checked')
						}
					}).done(function(data) {
						if (data.error) {
							var message = '<ul class="errors">';
							if (data.messages) {
								var len = data.messages.length;
								for (var i = 0; i < len; i++) {
									message += '<li>' + data.messages[i] + '</li>';
								}
							}
							message += '</ul>';
							$('td.errors', $this).html(message);
							return false;
						}
						if (data.user.reviewer) {
							$this.dialog('close');
							selectDate();
						} else {
							//
							//
							$.repost(null, true, false);
							//
						}

					});
					return false;
				});
				$('input[name=cancel]', this).click(function() {
					$this.dialog('close');
				});
			}
		});
		return false;
	}
	//

	//
	$.extend({
		repost: function(params, https, newWindow) {
			var paramsKeys = new Array();
			params = params || {};
			for (var k in params) {
				paramsKeys.push(k);
			}
			var prefix = (https) ? 'https://data.j-league.or.jp' : '';
			var target = (newWindow) ? 'target="_blank"' : '';
			var form = $('<form action=' + prefix + '/SFMS02/ method="GET" ' + target + ' />');
			//
			if ($.inArray("match_card_id",paramsKeys) == -1) {	form.append('<input type="hidden" name="match_card_id" value="15671" />'); }//
			params = params || {};
			for (var k in params) {
				var param = params[k];
				param = (param instanceof Array) ? param : [param];
				var len = param.length;
				for (var i = 0; i < len; i++) {
					form.append('<input type="hidden" name="' + k + '" value="' + param[i] + '" />');
				}
			}
			$('body').append(form);
			form.submit();
			form.remove();
		},
		openPrintPage: function(params) {
			$.repost($.extend({
				print : true
			}, params), false, true);
		}
	});
	//
	$("#print_button").click(function(e){
		 /* 別ウィンドウに print パラメータを付与して再度リクエストを送る */
		  $.openPrintPage();
		  return false;
	});

	//
});
</script>
</body>
</html>
'''

test_data_2014 = u'''
[
{
"teams": [
"名古屋グランパス",
"清水エスパルス"
],
"away_director": "アフシン　ゴトビ",
"home_start_member": "楢﨑　正剛,田鍋　陵太,大武　峻,田中　マルクス闘莉王,本多　勇喜,枝村　匠馬,ダニルソン,磯村　亮太,小川　佳純,玉田　圭司,ケネディ",
"away_shoot": 12,
"home_director": "西野　朗",
"away_team": "清水エスパルス",
"weather": "屋内",
"series_number": 1,
"temperature": 15.6,
"away_score": 3,
"away_start_member": "櫛引　政敏,吉田　豊,平岡　康裕,カルフィン　ヨン　ア　ピン,河井　陽介,杉山　浩太,竹内　涼,大前　元紀,高木　俊幸,ノヴァコヴィッチ,長沢　駿",
"home_score": 2,
"home_shoot": 10,
"game_id": "15670",
"home_team": "名古屋グランパス",
"game_start_at": "2014/03/01 14:04",
"referee": "廣瀬　格"
},
{
"teams": [
"セレッソ大阪",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "キム　ジンヒョン,藤本　康太,丸橋　祐介,酒本　憲幸,山下　達也,扇原　貴宏,長谷川　アーリアジャスール,山口　蛍,南野　拓実,柿谷　曜一朗,フォルラン",
"away_shoot": 10,
"home_director": "ランコ　ポポヴィッチ",
"away_team": "サンフレッチェ広島",
"weather": "雨",
"series_number": 1,
"temperature": 12.3,
"away_score": 1,
"away_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,ファン　ソッコ,青山　敏弘,柴﨑　晃誠,山岸　智,石原　直樹,野津田　岳人,佐藤　寿人",
"home_score": 0,
"home_shoot": 12,
"game_id": "15671",
"home_team": "セレッソ大阪",
"game_start_at": "2014/03/01 14:04",
"referee": "家本　政明"
},
{
"teams": [
"ベガルタ仙台",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,石川　直樹,二見　宏志,富田　晋伍,角田　誠,太田　吉彰,梁　勇基,マグリンチィ,ウイルソン",
"away_shoot": 11,
"home_director": "グラハム　アーノルド",
"away_team": "アルビレックス新潟",
"weather": "曇",
"series_number": 1,
"temperature": 10.6,
"away_score": 2,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,金　珍洙,レオ　シルバ,成岡　翔,田中　亜土夢,岡本　英也,田中　達也,川又　堅碁",
"home_score": 1,
"home_shoot": 9,
"game_id": "15668",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/03/01 14:05",
"referee": "山本　雄大"
},
{
"teams": [
"ヴァンフォーレ甲府",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "岡　大生,青山　直晃,山本　英臣,佐々木　翔,福田　健介,新井　涼平,マルキーニョス　パラナ,阿部　翔平,下田　北斗,ジウシーニョ,クリスティアーノ",
"away_shoot": 14,
"home_director": "城福　浩",
"away_team": "鹿島アントラーズ",
"weather": "曇",
"series_number": 1,
"temperature": 9.1,
"away_score": 4,
"away_start_member": "曽ヶ端　準,伊東　幸敏,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,豊川　雄太,土居　聖真,ダヴィ",
"home_score": 0,
"home_shoot": 12,
"game_id": "15669",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/03/01 14:05",
"referee": "飯田　淳平"
},
{
"teams": [
"サガン鳥栖",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,呂　成海,安田　理大,早坂　良太,谷口　博之,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 3,
"home_director": "尹　晶煥",
"away_team": "徳島ヴォルティス",
"weather": "曇",
"series_number": 1,
"temperature": 13.9,
"away_score": 0,
"away_start_member": "長谷川　徹,小暮　大器,橋内　優也,千代反田　充,アレックス,濱田　武,窪田　良,衛藤　裕,大﨑　淳矢,ドウグラス,津田　知宏",
"home_score": 5,
"home_shoot": 13,
"game_id": "15672",
"home_team": "サガン鳥栖",
"game_start_at": "2014/03/01 14:05",
"referee": "今村　義朗"
},
{
"teams": [
"柏レイソル",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "菅野　孝憲,増嶋　竜也,近藤　直也,鈴木　大輔,高山　薫,ハン　グギョン,大谷　秀和,橋本　和,レアンドロ　ドミンゲス,レアンドロ,工藤　壮人",
"away_shoot": 14,
"home_director": "ネルシーニョ",
"away_team": "ＦＣ東京",
"weather": "曇のち雨",
"series_number": 1,
"temperature": 8.1,
"away_score": 1,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,加賀　健一,太田　宏介,高橋　秀人,東　慶悟,三田　啓貴,渡邉　千真,エドゥー,武藤　嘉紀",
"home_score": 1,
"home_shoot": 12,
"game_id": "15673",
"home_team": "柏レイソル",
"game_start_at": "2014/03/01 15:03",
"referee": "佐藤　隆治"
},
{
"teams": [
"ガンバ大阪",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "東口　順昭,加地　亮,岩下　敬輔,丹羽　大輝,藤春　廣輝,内田　達也,今野　泰幸,倉田　秋,二川　孝広,佐藤　晃大,遠藤　保仁",
"away_shoot": 15,
"home_director": "長谷川　健太",
"away_team": "浦和レッズ",
"weather": "雨",
"series_number": 1,
"temperature": 8.3,
"away_score": 1,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,柏木　陽介,宇賀神　友弥,梅崎　司,原口　元気,興梠　慎三",
"home_score": 0,
"home_shoot": 7,
"game_id": "15674",
"home_team": "ガンバ大阪",
"game_start_at": "2014/03/01 19:04",
"referee": "西村　雄一"
},
{
"teams": [
"横浜Ｆ・マリノス",
"大宮アルディージャ"
],
"away_director": "大熊　清",
"home_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,富澤　清太郎,藤本　淳吾,中村　俊輔,齋藤　学,伊藤　翔",
"away_shoot": 8,
"home_director": "樋口　靖洋",
"away_team": "大宮アルディージャ",
"weather": "雨",
"series_number": 1,
"temperature": 7,
"away_score": 0,
"away_start_member": "清水　慶記,今井　智基,菊地　光将,高橋　祥平,村上　和弘,片岡　洋介,金澤　慎,渡邉　大剛,家長　昭博,曺　永哲,ラドンチッチ",
"home_score": 2,
"home_shoot": 14,
"game_id": "15675",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/03/02 13:04",
"referee": "松尾　一"
},
{
"teams": [
"東京ヴェルディ",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "佐藤　優也,安西　幸輝,吉野　恭平,金　鐘必,舘野　俊祐,田村　直也,中後　雅喜,前田　直輝,高木　大輔,菅嶋　弘希,平本　一樹",
"away_shoot": 14,
"home_director": "三浦　泰年",
"away_team": "松本山雅ＦＣ",
"weather": "曇時々雨",
"series_number": 1,
"temperature": 5.8,
"away_score": 3,
"away_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,岩沼　俊介,多々良　敦斗,岩上　祐三,喜山　康平,鐡戸　裕史,船山　貴之,サビア",
"home_score": 1,
"home_shoot": 11,
"game_id": "15975",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/03/02 13:04",
"referee": "井上　知大"
},
{
"teams": [
"ＦＣ岐阜",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "川口　能活,杉山　新,木谷　公亮,阿部　正紀,三都主　アレサンドロ,水野　泰輔,宮沢　正史,美尾　敦,髙地　系治,難波　宏明,ナザリト",
"away_shoot": 13,
"home_director": "ラモス　瑠偉",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 1,
"temperature": 16,
"away_score": 1,
"away_start_member": "瀬口　拓弥,藤田　浩平,藤井　航大,野口　遼太,沼田　圭悟,持留　新作,岡村　和哉,山本　翔平,アンドレア,我那覇　和樹,高木　和正",
"home_score": 3,
"home_shoot": 11,
"game_id": "15976",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/03/02 13:05",
"referee": "窪田　陽輔"
},
{
"teams": [
"ジュビロ磐田",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "藤ヶ谷　陽介,駒野　友一,菅沼　駿哉,伊野波　雅彦,宮崎　智彦,藤田　義明,フェルジナンド,松井　大輔,山田　大記,ポポ,前田　遼一",
"away_shoot": 5,
"home_director": "シャムスカ",
"away_team": "コンサドーレ札幌",
"weather": "雨",
"series_number": 1,
"temperature": 10.1,
"away_score": 1,
"away_start_member": "金山　隼樹,上原　慎也,小山内　貴哉,櫛引　一紀,松本　怜大,宮澤　裕樹,上原　拓郎,砂川　誠,内村　圭宏,菊岡　拓朗,石井　謙伍",
"home_score": 0,
"home_shoot": 17,
"game_id": "15977",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/03/02 14:03",
"referee": "木村　博之"
},
{
"teams": [
"横浜ＦＣ",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "南　雄太,小池　純輝,ドウグラス,野上　結貴,中島　崇典,寺田　紳一,松下　年宏,小野瀬　康介,内田　智也,飯尾　一慶,パク　ソンホ",
"away_shoot": 2,
"home_director": "山口　素弘",
"away_team": "愛媛ＦＣ",
"weather": "雨",
"series_number": 1,
"temperature": 5.6,
"away_score": 0,
"away_start_member": "児玉　剛,関根　永悟,村上　佑介,林堂　眞,西岡　大輝,三原　向平,渡邊　一仁,吉村　圭司,原川　力,堀米　勇輝,西田　剛",
"home_score": 0,
"home_shoot": 8,
"game_id": "15979",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/03/02 15:03",
"referee": "高山　啓義"
},
{
"teams": [
"水戸ホーリーホック",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "本間　幸司,田向　泰輝,新里　亮,金　聖基,田中　雄大,吉田　眞紀人,内田　航平,西岡　謙太,船谷　圭祐,馬場　賢治,三島　康平",
"away_shoot": 14,
"home_director": "柱谷　哲二",
"away_team": "大分トリニータ",
"weather": "曇時々雨",
"series_number": 1,
"temperature": 5.6,
"away_score": 1,
"away_start_member": "武田　洋平,若狭　大志,高木　和道,阪田　章裕,チェ　ジョンハン,伊藤　大介,末吉　隼也,西　弘則,田中　輝希,木村　祐志,後藤　優介",
"home_score": 2,
"home_shoot": 10,
"game_id": "15978",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/03/02 15:04",
"referee": "榎本　一慶"
},
{
"teams": [
"ファジアーノ岡山",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "中林　洋次,後藤　圭太,竹田　忠嗣,近藤　徹志,仙石　廉,千明　聖典,鎌田　翔雅,田所　諒,林　容平,妹尾　隆佑,押谷　祐樹",
"away_shoot": 12,
"home_director": "影山　雅永",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 1,
"temperature": 11.8,
"away_score": 0,
"away_start_member": "水谷　雄一,木村　勝太,平出　涼,御厨　貴文,内田　健太,大西　容平,キム　ヨングン,ソ　ヨンドク,白崎　凌兵,中島　翔哉,苔口　卓也",
"home_score": 0,
"home_shoot": 10,
"game_id": "15980",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/03/02 15:04",
"referee": "吉田　哲朗"
},
{
"teams": [
"ギラヴァンツ北九州",
"京都サンガF.C."
],
"away_director": "バドゥ",
"home_start_member": "大谷　幸輝,宮本　亨,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"away_shoot": 8,
"home_director": "柱谷　幸一",
"away_team": "京都サンガF.C.",
"weather": "曇",
"series_number": 1,
"temperature": 10.2,
"away_score": 3,
"away_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,駒井　善成,ジャイロ,工藤　浩平,山瀬　功治,アレッサンドロ,大黒　将志",
"home_score": 1,
"home_shoot": 13,
"game_id": "15981",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/03/02 15:05",
"referee": "三上　正一郎"
},
{
"teams": [
"ロアッソ熊本",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "畑　実,園田　拓也,篠原　弘次郎,矢野　大輔,片山　奨典,橋本　拳人,養父　雄仁,中山　雄登,齊藤　和樹,仲間　隼斗,巻　誠一郎",
"away_shoot": 11,
"home_director": "小野　剛",
"away_team": "アビスパ福岡",
"weather": "曇",
"series_number": 1,
"temperature": 13.6,
"away_score": 1,
"away_start_member": "神山　竜一,パク　ゴン,堤　俊輔,阿部　巧,三島　勇太,中原　秀人,平井　将生,森村　昂太,城後　寿,坂田　大輔,プノセバッチ",
"home_score": 2,
"home_shoot": 7,
"game_id": "15982",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/03/02 15:05",
"referee": "吉田　寿光"
},
{
"teams": [
"川崎フロンターレ",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "西部　洋平,田中　裕介,ジェシ,井川　祐輔,登里　享平,大島　僚太,パウリーニョ,中村　憲剛,小林　悠,レナト,大久保　嘉人",
"away_shoot": 14,
"home_director": "風間　八宏",
"away_team": "ヴィッセル神戸",
"weather": "雨",
"series_number": 1,
"temperature": 8.6,
"away_score": 2,
"away_start_member": "山本　海人,高橋　峻希,岩波　拓也,増川　隆洋,茂木　弘人,シンプリシオ,チョン　ウヨン,森岡　亮太,ペドロ　ジュニオール,小川　慶治朗,マルキーニョス",
"home_score": 2,
"home_shoot": 17,
"game_id": "15676",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/03/02 16:03",
"referee": "東城　穣"
},
{
"teams": [
"ジェフユナイテッド千葉",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "岡本　昌弘,天野　貴史,大岩　一貴,山口　智,中村　太亮,山口　慶,佐藤　健太郎,田中　佑昌,山中　亮輔,谷澤　達也,ケンペス",
"away_shoot": 11,
"home_director": "鈴木　淳",
"away_team": "栃木ＳＣ",
"weather": "雨",
"series_number": 1,
"temperature": 6.4,
"away_score": 2,
"away_start_member": "鈴木　智幸,山形　辰徳,チャ　ヨンファン,ドゥドゥ,イ　ミンス,西澤　代志也,小野寺　達也,杉本　真,廣瀬　浩二,瀬沼　優司,近藤　祐介",
"home_score": 0,
"home_shoot": 10,
"game_id": "15983",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/03/02 16:03",
"referee": "岡部　拓人"
},
{
"teams": [
"湘南ベルマーレ",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,宇佐美　宏和,菊地　俊介,永木　亮太,菊池　大介,梶川　諒太,ウェリントン,武富　孝介",
"away_shoot": 13,
"home_director": "曺　貴裁",
"away_team": "モンテディオ山形",
"weather": "雨",
"series_number": 1,
"temperature": 5.7,
"away_score": 0,
"away_start_member": "清水　健太,山田　拓巳,當間　建文,イ　ジュヨン,舩津　徹也,宮阪　政樹,ロメロ　フランク,山﨑　雅人,ディエゴ,中島　裕希,萬代　宏樹",
"home_score": 1,
"home_shoot": 7,
"game_id": "15984",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/03/02 16:04",
"referee": "村上　伸次"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "大久保　択生,下田　光平,山口　貴弘,古部　健太,神崎　大輔,前田　悠佑,三原　雅俊,野田　紘史,奥埜　博亮,東　浩史,小松　塁",
"away_shoot": 6,
"home_director": "高木　琢也",
"away_team": "ザスパクサツ群馬",
"weather": "曇",
"series_number": 1,
"temperature": 11.9,
"away_score": 0,
"away_start_member": "北　一真,夛田　凌輔,小柳　達司,クォン　ハンジン,瀬川　和樹,黄　誠秀,坂井　洋平,加藤　弘堅,永田　亮太,平繁　龍一,ダニエル　ロビーニョ",
"home_score": 2,
"home_shoot": 9,
"game_id": "15985",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/03/02 16:04",
"referee": "上田　益也"
},
{
"teams": [
"サンフレッチェ広島",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,ミキッチ,青山　敏弘,森﨑　和幸,山岸　智,石原　直樹,野津田　岳人,佐藤　寿人",
"away_shoot": 5,
"home_director": "森保　一",
"away_team": "川崎フロンターレ",
"weather": "晴",
"series_number": 2,
"temperature": 8.1,
"away_score": 1,
"away_start_member": "西部　洋平,田中　裕介,ジェシ,井川　祐輔,登里　享平,稲本　潤一,山本　真希,中村　憲剛,小林　悠,レナト,大久保　嘉人",
"home_score": 2,
"home_shoot": 17,
"game_id": "15677",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/03/08 12:34",
"referee": "村上　伸次"
},
{
"teams": [
"アルビレックス新潟",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "守田　達弥,松原　健,大井　健太郎,大野　和成,金　珍洙,レオ　シルバ,成岡　翔,田中　亜土夢,岡本　英也,田中　達也,川又　堅碁",
"away_shoot": 9,
"home_director": "柳下　正明",
"away_team": "ガンバ大阪",
"weather": "曇時々晴",
"series_number": 2,
"temperature": 4.2,
"away_score": 2,
"away_start_member": "東口　順昭,加地　亮,岩下　敬輔,丹羽　大輝,藤春　廣輝,内田　達也,今野　泰幸,米倉　恒貴,遠藤　保仁,佐藤　晃大,倉田　秋",
"home_score": 0,
"home_shoot": 15,
"game_id": "15678",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/03/08 13:02",
"referee": "岡部　拓人"
},
{
"teams": [
"徳島ヴォルティス",
"セレッソ大阪"
],
"away_director": "ランコ　ポポヴィッチ",
"home_start_member": "松井　謙弥,小暮　大器,橋内　優也,千代反田　充,アレックス,濱田　武,斉藤　大介,衛藤　裕,大﨑　淳矢,ドウグラス,津田　知宏",
"away_shoot": 8,
"home_director": "小林　伸二",
"away_team": "セレッソ大阪",
"weather": "晴",
"series_number": 2,
"temperature": 8.2,
"away_score": 2,
"away_start_member": "キム　ジンヒョン,新井場　徹,丸橋　祐介,山下　達也,ゴイコ　カチャル,扇原　貴宏,長谷川　アーリアジャスール,山口　蛍,南野　拓実,柿谷　曜一朗,杉本　健勇",
"home_score": 0,
"home_shoot": 5,
"game_id": "15679",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/03/08 14:06",
"referee": "松尾　一"
},
{
"teams": [
"ＦＣ東京",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,加賀　健一,太田　宏介,高橋　秀人,三田　啓貴,東　慶悟,渡邉　千真,エドゥー,武藤　嘉紀",
"away_shoot": 9,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "ヴァンフォーレ甲府",
"weather": "晴",
"series_number": 2,
"temperature": 7.9,
"away_score": 1,
"away_start_member": "岡　大生,青山　直晃,山本　英臣,佐々木　翔,福田　健介,新井　涼平,マルキーニョス　パラナ,阿部　翔平,下田　北斗,盛田　剛平,クリスティアーノ",
"home_score": 1,
"home_shoot": 8,
"game_id": "15681",
"home_team": "ＦＣ東京",
"game_start_at": "2014/03/08 15:03",
"referee": "高山　啓義"
},
{
"teams": [
"大宮アルディージャ",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "清水　慶記,今井　智基,菊地　光将,高橋　祥平,村上　和弘,片岡　洋介,金澤　慎,家長　昭博,渡邉　大剛,ズラタン,ラドンチッチ",
"away_shoot": 9,
"home_director": "大熊　清",
"away_team": "名古屋グランパス",
"weather": "晴",
"series_number": 2,
"temperature": 10.3,
"away_score": 2,
"away_start_member": "楢﨑　正剛,田鍋　陵太,大武　峻,田中　マルクス闘莉王,本多　勇喜,枝村　匠馬,磯村　亮太,ダニルソン,小川　佳純,玉田　圭司,ケネディ",
"home_score": 1,
"home_shoot": 4,
"game_id": "15680",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/03/08 15:04",
"referee": "飯田　淳平"
},
{
"teams": [
"清水エスパルス",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "櫛引　政敏,吉田　豊,平岡　康裕,杉山　浩太,カルフィン　ヨン　ア　ピン,ヤコヴィッチ,村松　大輔,大前　元紀,高木　俊幸,ノヴァコヴィッチ,長沢　駿",
"away_shoot": 10,
"home_director": "アフシン　ゴトビ",
"away_team": "横浜Ｆ・マリノス",
"weather": "晴",
"series_number": 2,
"temperature": 10.9,
"away_score": 1,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,富澤　清太郎,藤本　淳吾,中村　俊輔,齋藤　学,伊藤　翔",
"home_score": 0,
"home_shoot": 5,
"game_id": "15682",
"home_team": "清水エスパルス",
"game_start_at": "2014/03/08 15:04",
"referee": "中村　太"
},
{
"teams": [
"ヴィッセル神戸",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "山本　海人,高橋　峻希,増川　隆洋,岩波　拓也,茂木　弘人,チョン　ウヨン,シンプリシオ,森岡　亮太,マルキーニョス,ペドロ　ジュニオール,小川　慶治朗",
"away_shoot": 17,
"home_director": "安達　亮",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 2,
"temperature": 8.9,
"away_score": 1,
"away_start_member": "菅野　孝憲,鈴木　大輔,近藤　直也,増嶋　竜也,高山　薫,ハン　グギョン,大谷　秀和,橋本　和,工藤　壮人,レアンドロ,レアンドロ　ドミンゲス",
"home_score": 1,
"home_shoot": 12,
"game_id": "15683",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/03/08 15:05",
"referee": "吉田　寿光"
},
{
"teams": [
"浦和レッズ",
"サガン鳥栖"
],
"away_director": "尹　晶煥",
"home_start_member": "西川　周作,濱田　水輝,永田　充,槙野　智章,森脇　良太,阿部　勇樹,柏木　陽介,宇賀神　友弥,梅崎　司,原口　元気,興梠　慎三",
"away_shoot": 3,
"home_director": "ペトロヴィッチ",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 2,
"temperature": 9.6,
"away_score": 1,
"away_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,呂　成海,安田　理大,早坂　良太,谷口　博之,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 0,
"home_shoot": 17,
"game_id": "15684",
"home_team": "浦和レッズ",
"game_start_at": "2014/03/08 16:04",
"referee": "家本　政明"
},
{
"teams": [
"鹿島アントラーズ",
"ベガルタ仙台"
],
"away_director": "グラハム　アーノルド",
"home_start_member": "曽ヶ端　準,伊東　幸敏,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,豊川　雄太,土居　聖真,ダヴィ",
"away_shoot": 7,
"home_director": "トニーニョ　セレーゾ",
"away_team": "ベガルタ仙台",
"weather": "晴",
"series_number": 2,
"temperature": 6.4,
"away_score": 0,
"away_start_member": "関　憲太郎,菅井　直樹,渡辺　広大,石川　直樹,二見　宏志,太田　吉彰,鎌田　次郎,富田　晋伍,武藤　雄樹,梁　勇基,ウイルソン",
"home_score": 2,
"home_shoot": 12,
"game_id": "15685",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/03/08 19:04",
"referee": "東城　穣"
},
{
"teams": [
"コンサドーレ札幌",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "金山　隼樹,日高　拓磨,小山内　貴哉,櫛引　一紀,上原　慎也,河合　竜二,宮澤　裕樹,砂川　誠,前田　俊介,菊岡　拓朗,内村　圭宏",
"away_shoot": 16,
"home_director": "財前　恵一",
"away_team": "モンテディオ山形",
"weather": "屋内",
"series_number": 2,
"temperature": 20.9,
"away_score": 1,
"away_start_member": "清水　健太,山田　拓巳,當間　建文,イ　ジュヨン,舩津　徹也,中島　裕希,宮阪　政樹,秋葉　勝,ディエゴ,伊東　俊,萬代　宏樹",
"home_score": 1,
"home_shoot": 10,
"game_id": "15986",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/03/09 13:03",
"referee": "小屋　幸栄"
},
{
"teams": [
"栃木ＳＣ",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "鈴木　智幸,山形　辰徳,チャ　ヨンファン,ドゥドゥ,イ　ミンス,西澤　代志也,小野寺　達也,杉本　真,廣瀬　浩二,瀬沼　優司,近藤　祐介",
"away_shoot": 11,
"home_director": "阪倉　裕二",
"away_team": "横浜ＦＣ",
"weather": "晴",
"series_number": 2,
"temperature": 9.6,
"away_score": 1,
"away_start_member": "南　雄太,小池　純輝,ドウグラス,野上　結貴,中島　崇典,松下　年宏,安　英学,小野瀬　康介,寺田　紳一,飯尾　一慶,パク　ソンホ",
"home_score": 1,
"home_shoot": 7,
"game_id": "15987",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/03/09 13:03",
"referee": "井上　知大"
},
{
"teams": [
"カマタマーレ讃岐",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "瀬口　拓弥,持留　新作,西野　泰正,野口　遼太,沼田　圭悟,岡村　和哉,綱田　大志,山本　翔平,アンドレア,高木　和正,我那覇　和樹",
"away_shoot": 15,
"home_director": "北野　誠",
"away_team": "ジュビロ磐田",
"weather": "晴",
"series_number": 2,
"temperature": 13.6,
"away_score": 4,
"away_start_member": "藤ヶ谷　陽介,駒野　友一,菅沼　駿哉,伊野波　雅彦,宮崎　智彦,フェルジナンド,藤田　義明,松井　大輔,ポポ,山崎　亮平,前田　遼一",
"home_score": 1,
"home_shoot": 5,
"game_id": "15989",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/03/09 13:03",
"referee": "岡　宏道"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "大久保　択生,岡本　拓也,前田　悠佑,古部　健太,神崎　大輔,井上　裕大,三原　雅俊,野田　紘史,奥埜　博亮,東　浩史,小松　塁",
"away_shoot": 14,
"home_director": "高木　琢也",
"away_team": "湘南ベルマーレ",
"weather": "曇のち晴",
"series_number": 2,
"temperature": 14.1,
"away_score": 3,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,宇佐美　宏和,岩尾　憲,永木　亮太,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"home_score": 0,
"home_shoot": 7,
"game_id": "15990",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/03/09 13:03",
"referee": "木村　博之"
},
{
"teams": [
"ザスパクサツ群馬",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "北　一真,小柳　達司,クォン　ハンジン,黄　誠秀,夛田　凌輔,瀬川　和樹,加藤　弘堅,宮崎　泰右,平繁　龍一,エデル,小林　竜樹",
"away_shoot": 12,
"home_director": "秋葉　忠宏",
"away_team": "東京ヴェルディ",
"weather": "晴",
"series_number": 2,
"temperature": 8.5,
"away_score": 0,
"away_start_member": "佐藤　優也,安西　幸輝,吉野　恭平,金　鐘必,舘野　俊祐,前田　直輝,田村　直也,姜　成浩,高木　大輔,常盤　聡,平本　一樹",
"home_score": 1,
"home_shoot": 10,
"game_id": "15988",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/03/09 13:04",
"referee": "長谷　拓"
},
{
"teams": [
"愛媛ＦＣ",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "児玉　剛,関根　永悟,村上　佑介,西岡　大輝,浦田　延尚,三原　向平,渡邊　一仁,吉村　圭司,原川　力,西田　剛,河原　和寿",
"away_shoot": 6,
"home_director": "石丸　清隆",
"away_team": "水戸ホーリーホック",
"weather": "曇",
"series_number": 2,
"temperature": 9.1,
"away_score": 2,
"away_start_member": "本間　幸司,田向　泰輝,新里　亮,冨田　大介,金　聖基,田中　雄大,小谷野　顕治,内田　航平,船谷　圭祐,馬場　賢治,三島　康平",
"home_score": 0,
"home_shoot": 13,
"game_id": "15991",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/03/09 14:04",
"referee": "野田　祐樹"
},
{
"teams": [
"大分トリニータ",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "武田　洋平,チェ　ジョンハン,高木　和道,阪田　章裕,若狭　大志,西　弘則,伊藤　大介,末吉　隼也,田中　輝希,木村　祐志,後藤　優介",
"away_shoot": 5,
"home_director": "田坂　和昭",
"away_team": "ギラヴァンツ北九州",
"weather": "晴のち曇",
"series_number": 2,
"temperature": 11.3,
"away_score": 0,
"away_start_member": "大谷　幸輝,宮本　亨,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"home_score": 1,
"home_shoot": 15,
"game_id": "15995",
"home_team": "大分トリニータ",
"game_start_at": "2014/03/09 16:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"ＦＣ岐阜",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "川口　能活,杉山　新,木谷　公亮,阿部　正紀,三都主　アレサンドロ,水野　泰輔,宮沢　正史,スティッペ,髙地　系治,難波　宏明,ナザリト",
"away_shoot": 10,
"home_director": "ラモス　瑠偉",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 2,
"temperature": 10.3,
"away_score": 0,
"away_start_member": "水谷　雄一,木村　勝太,平出　涼,御厨　貴文,内田　健太,大西　容平,キム　ヨングン,ソ　ヨンドク,白崎　凌兵,中島　翔哉,苔口　卓也",
"home_score": 3,
"home_shoot": 7,
"game_id": "15992",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/03/09 16:04",
"referee": "塚田　健太"
},
{
"teams": [
"アビスパ福岡",
"京都サンガF.C."
],
"away_director": "バドゥ",
"home_start_member": "神山　竜一,三島　勇太,堤　俊輔,イ　グァンソン,阿部　巧,パク　ゴン,中原　秀人,坂田　大輔,城後　寿,石津　大介,プノセバッチ",
"away_shoot": 6,
"home_director": "マリヤン　プシュニク",
"away_team": "京都サンガF.C.",
"weather": "曇",
"series_number": 2,
"temperature": 9.6,
"away_score": 0,
"away_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,駒井　善成,ジャイロ,工藤　浩平,山瀬　功治,大黒　将志,横谷　繁",
"home_score": 1,
"home_shoot": 15,
"game_id": "15993",
"home_team": "アビスパ福岡",
"game_start_at": "2014/03/09 16:04",
"referee": "西村　雄一"
},
{
"teams": [
"ロアッソ熊本",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "畑　実,園田　拓也,篠原　弘次郎,矢野　大輔,片山　奨典,橋本　拳人,養父　雄仁,中山　雄登,齊藤　和樹,仲間　隼斗,巻　誠一郎",
"away_shoot": 8,
"home_director": "小野　剛",
"away_team": "松本山雅ＦＣ",
"weather": "曇",
"series_number": 2,
"temperature": 10.5,
"away_score": 1,
"away_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,多々良　敦斗,岩沼　俊介,喜山　康平,岩上　祐三,鐡戸　裕史,船山　貴之,サビア",
"home_score": 0,
"home_shoot": 9,
"game_id": "15994",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/03/09 16:04",
"referee": "河合　英治"
},
{
"teams": [
"ジェフユナイテッド千葉",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "岡本　昌弘,天野　貴史,大岩　一貴,山口　智,中村　太亮,山口　慶,佐藤　健太郎,田中　佑昌,山中　亮輔,町田　也真人,森本　貴幸",
"away_shoot": 8,
"home_director": "鈴木　淳",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 2,
"temperature": 7.9,
"away_score": 0,
"away_start_member": "中林　洋次,近藤　徹志,竹田　忠嗣,後藤　圭太,鎌田　翔雅,島田　譲,千明　聖典,田所　諒,妹尾　隆佑,林　容平,荒田　智之",
"home_score": 1,
"home_shoot": 13,
"game_id": "15996",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/03/09 17:03",
"referee": "廣瀬　格"
},
{
"teams": [
"横浜Ｆ・マリノス",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,富澤　清太郎,藤本　淳吾,中村　俊輔,齋藤　学,伊藤　翔",
"away_shoot": 4,
"home_director": "樋口　靖洋",
"away_team": "徳島ヴォルティス",
"weather": "晴",
"series_number": 3,
"temperature": 12.8,
"away_score": 0,
"away_start_member": "松井　謙弥,福元　洋平,橋内　優也,千代反田　充,アレックス,濱田　武,斉藤　大介,衛藤　裕,大﨑　淳矢,クレイトン　ドミンゲス,高崎　寛之",
"home_score": 3,
"home_shoot": 13,
"game_id": "15686",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/03/15 13:04",
"referee": "飯田　淳平"
},
{
"teams": [
"ヴァンフォーレ甲府",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "岡　大生,青山　直晃,山本　英臣,佐々木　翔,福田　健介,新井　涼平,マルキーニョス　パラナ,阿部　翔平,河本　明人,盛田　剛平,クリスティアーノ",
"away_shoot": 11,
"home_director": "城福　浩",
"away_team": "アルビレックス新潟",
"weather": "晴",
"series_number": 3,
"temperature": 11.1,
"away_score": 1,
"away_start_member": "守田　達弥,松原　健,大井　健太郎,大野　和成,金　珍洙,レオ　シルバ,成岡　翔,加藤　大,田中　亜土夢,岡本　英也,川又　堅碁",
"home_score": 1,
"home_shoot": 10,
"game_id": "15687",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/03/15 14:03",
"referee": "廣瀬　格"
},
{
"teams": [
"サンフレッチェ広島",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,ミキッチ,青山　敏弘,森﨑　和幸,山岸　智,石原　直樹,野津田　岳人,佐藤　寿人",
"away_shoot": 10,
"home_director": "森保　一",
"away_team": "浦和レッズ",
"weather": "晴",
"series_number": 3,
"temperature": 11.2,
"away_score": 2,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,鈴木　啓太,宇賀神　友弥,柏木　陽介,原口　元気,興梠　慎三",
"home_score": 0,
"home_shoot": 5,
"game_id": "15688",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/03/15 14:04",
"referee": "松尾　一"
},
{
"teams": [
"柏レイソル",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "菅野　孝憲,鈴木　大輔,近藤　直也,橋本　和,高山　薫,ハン　グギョン,大谷　秀和,田中　順也,工藤　壮人,レアンドロ,レアンドロ　ドミンゲス",
"away_shoot": 13,
"home_director": "ネルシーニョ",
"away_team": "名古屋グランパス",
"weather": "晴",
"series_number": 3,
"temperature": 12.8,
"away_score": 1,
"away_start_member": "楢﨑　正剛,田鍋　陵太,大武　峻,田中　マルクス闘莉王,本多　勇喜,枝村　匠馬,磯村　亮太,ダニルソン,小川　佳純,玉田　圭司,ケネディ",
"home_score": 0,
"home_shoot": 11,
"game_id": "15689",
"home_team": "柏レイソル",
"game_start_at": "2014/03/15 15:03",
"referee": "今村　義朗"
},
{
"teams": [
"川崎フロンターレ",
"大宮アルディージャ"
],
"away_director": "大熊　清",
"home_start_member": "杉山　力裕,田中　裕介,中澤　聡太,井川　祐輔,福森　晃斗,大島　僚太,パウリーニョ,中村　憲剛,レナト,小林　悠,大久保　嘉人",
"away_shoot": 8,
"home_director": "風間　八宏",
"away_team": "大宮アルディージャ",
"weather": "晴",
"series_number": 3,
"temperature": 11.8,
"away_score": 4,
"away_start_member": "北野　貴之,今井　智基,菊地　光将,高橋　祥平,中村　北斗,渡邉　大剛,片岡　洋介,金澤　慎,家長　昭博,ズラタン,ラドンチッチ",
"home_score": 3,
"home_shoot": 24,
"game_id": "15690",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/03/15 15:03",
"referee": "山本　雄大"
},
{
"teams": [
"セレッソ大阪",
"清水エスパルス"
],
"away_director": "アフシン　ゴトビ",
"home_start_member": "キム　ジンヒョン,丸橋　祐介,酒本　憲幸,山下　達也,ゴイコ　カチャル,長谷川　アーリアジャスール,山口　蛍,南野　拓実,柿谷　曜一朗,フォルラン,杉本　健勇",
"away_shoot": 7,
"home_director": "ランコ　ポポヴィッチ",
"away_team": "清水エスパルス",
"weather": "晴",
"series_number": 3,
"temperature": 9.6,
"away_score": 1,
"away_start_member": "相澤　貴志,石毛　秀樹,平岡　康裕,ヤコヴィッチ,カルフィン　ヨン　ア　ピン,河井　陽介,村松　大輔,竹内　涼,高木　俊幸,大前　元紀,ノヴァコヴィッチ",
"home_score": 4,
"home_shoot": 17,
"game_id": "15691",
"home_team": "セレッソ大阪",
"game_start_at": "2014/03/15 15:04",
"referee": "木村　博之"
},
{
"teams": [
"サガン鳥栖",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,呂　成海,安田　理大,早坂　良太,谷口　博之,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 10,
"home_director": "尹　晶煥",
"away_team": "鹿島アントラーズ",
"weather": "晴",
"series_number": 3,
"temperature": 13.4,
"away_score": 3,
"away_start_member": "曽ヶ端　準,伊東　幸敏,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,豊川　雄太,土居　聖真,ダヴィ",
"home_score": 0,
"home_shoot": 8,
"game_id": "15692",
"home_team": "サガン鳥栖",
"game_start_at": "2014/03/15 15:04",
"referee": "高山　啓義"
},
{
"teams": [
"ベガルタ仙台",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "関　憲太郎,菅井　直樹,渡辺　広大,石川　直樹,二見　宏志,太田　吉彰,鎌田　次郎,富田　晋伍,武藤　雄樹,梁　勇基,ウイルソン",
"away_shoot": 1,
"home_director": "グラハム　アーノルド",
"away_team": "ガンバ大阪",
"weather": "曇",
"series_number": 3,
"temperature": 5.6,
"away_score": 0,
"away_start_member": "東口　順昭,加地　亮,岩下　敬輔,丹羽　大輝,藤春　廣輝,内田　達也,今野　泰幸,大森　晃太郎,遠藤　保仁,佐藤　晃大,倉田　秋",
"home_score": 0,
"home_shoot": 11,
"game_id": "15693",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/03/15 17:04",
"referee": "村上　伸次"
},
{
"teams": [
"ヴィッセル神戸",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "山本　海人,高橋　峻希,岩波　拓也,増川　隆洋,チョン　ウヨン,田中　英雄,森岡　亮太,茂木　弘人,松村　亮,マルキーニョス,ペドロ　ジュニオール",
"away_shoot": 20,
"home_director": "安達　亮",
"away_team": "ＦＣ東京",
"weather": "晴",
"series_number": 3,
"temperature": 8.3,
"away_score": 1,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,加賀　健一,太田　宏介,高橋　秀人,三田　啓貴,東　慶悟,渡邉　千真,エドゥー,武藤　嘉紀",
"home_score": 2,
"home_shoot": 10,
"game_id": "15694",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/03/15 19:04",
"referee": "前田　拓哉"
},
{
"teams": [
"モンテディオ山形",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "清水　健太,山田　拓巳,當間　建文,イ　ジュヨン,舩津　徹也,宮阪　政樹,秋葉　勝,中島　裕希,ディエゴ,伊東　俊,萬代　宏樹",
"away_shoot": 13,
"home_director": "石﨑　信弘",
"away_team": "ＦＣ岐阜",
"weather": "雨",
"series_number": 3,
"temperature": 5.4,
"away_score": 1,
"away_start_member": "川口　能活,杉山　新,木谷　公亮,阿部　正紀,野垣内　俊,水野　泰輔,宮沢　正史,スティッペ,髙地　系治,難波　宏明,ナザリト",
"home_score": 3,
"home_shoot": 18,
"game_id": "15997",
"home_team": "モンテディオ山形",
"game_start_at": "2014/03/16 13:03",
"referee": "上田　益也"
},
{
"teams": [
"松本山雅ＦＣ",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,玉林　睦実,岩沼　俊介,多々良　敦斗,喜山　康平,サビア,船山　貴之,岩上　祐三",
"away_shoot": 13,
"home_director": "反町　康治",
"away_team": "Ｖ・ファーレン長崎",
"weather": "晴",
"series_number": 3,
"temperature": 11.6,
"away_score": 0,
"away_start_member": "大久保　択生,岡本　拓也,山口　貴弘,下田　光平,神崎　大輔,黒木　聖仁,三原　雅俊,野田　紘史,奥埜　博亮,東　浩史,佐藤　洸一",
"home_score": 0,
"home_shoot": 5,
"game_id": "15998",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/03/16 13:03",
"referee": "佐藤　隆治"
},
{
"teams": [
"大分トリニータ",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "武田　洋平,チェ　ジョンハン,阪田　章裕,高木　和道,若狭　大志,伊藤　大介,末吉　隼也,西　弘則,田中　輝希,木村　祐志,後藤　優介",
"away_shoot": 6,
"home_director": "田坂　和昭",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 3,
"temperature": 18.7,
"away_score": 0,
"away_start_member": "森田　耕一郎,持留　新作,西野　泰正,野口　遼太,小澤　雄希,綱田　大志,岡村　和哉,山本　翔平,アンドレア,高木　和正,我那覇　和樹",
"home_score": 1,
"home_shoot": 10,
"game_id": "16001",
"home_team": "大分トリニータ",
"game_start_at": "2014/03/16 13:03",
"referee": "森川　浩次"
},
{
"teams": [
"カターレ富山",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "水谷　雄一,木村　勝太,高　准翼,平出　涼,内田　健太,秋本　倫孝,キム　ヨングン,ソ　ヨンドク,白崎　凌兵,中島　翔哉,苔口　卓也",
"away_shoot": 14,
"home_director": "安間　貴義",
"away_team": "横浜ＦＣ",
"weather": "雨のち曇",
"series_number": 3,
"temperature": 7.9,
"away_score": 2,
"away_start_member": "南　雄太,市村　篤司,ドウグラス,野上　結貴,中島　崇典,松下　年宏,安　英学,寺田　紳一,野崎　陽介,小野瀬　康介,パク　ソンホ",
"home_score": 1,
"home_shoot": 11,
"game_id": "15999",
"home_team": "カターレ富山",
"game_start_at": "2014/03/16 13:05",
"referee": "窪田　陽輔"
},
{
"teams": [
"アビスパ福岡",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "神山　竜一,三島　勇太,堤　俊輔,イ　グァンソン,阿部　巧,パク　ゴン,城後　寿,中原　秀人,坂田　大輔,プノセバッチ,石津　大介",
"away_shoot": 11,
"home_director": "マリヤン　プシュニク",
"away_team": "愛媛ＦＣ",
"weather": "晴",
"series_number": 3,
"temperature": 18.3,
"away_score": 1,
"away_start_member": "児玉　剛,関根　永悟,村上　佑介,林堂　眞,西岡　大輝,キム　ミンジェ,渡邊　一仁,原川　力,堀米　勇輝,渡辺　亮太,表原　玄太",
"home_score": 1,
"home_shoot": 9,
"game_id": "16000",
"home_team": "アビスパ福岡",
"game_start_at": "2014/03/16 13:05",
"referee": "三上　正一郎"
},
{
"teams": [
"京都サンガF.C.",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,田森　大己,比嘉　祐介,駒井　善成,ジャイロ,工藤　浩平,山瀬　功治,大黒　将志,アレッサンドロ",
"away_shoot": 6,
"home_director": "バドゥ",
"away_team": "栃木ＳＣ",
"weather": "曇時々晴",
"series_number": 3,
"temperature": 16.1,
"away_score": 0,
"away_start_member": "鈴木　智幸,山形　辰徳,チャ　ヨンファン,ドゥドゥ,イ　ミンス,廣瀬　浩二,西澤　代志也,小野寺　達也,近藤　祐介,大久保　哲哉,瀬沼　優司",
"home_score": 0,
"home_shoot": 16,
"game_id": "16002",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/03/16 14:04",
"referee": "榎本　一慶"
},
{
"teams": [
"東京ヴェルディ",
"ジェフユナイテッド千葉"
],
"away_director": "鈴木　淳",
"home_start_member": "佐藤　優也,安西　幸輝,吉野　恭平,金　鐘必,安在　和樹,姜　成浩,田村　直也,前田　直輝,高木　大輔,常盤　聡,平本　一樹",
"away_shoot": 10,
"home_director": "三浦　泰年",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 3,
"temperature": 17.7,
"away_score": 1,
"away_start_member": "岡本　昌弘,竹内　彬,大岩　一貴,山口　智,中村　太亮,山口　慶,佐藤　健太郎,田中　佑昌,山中　亮輔,町田　也真人,森本　貴幸",
"home_score": 1,
"home_shoot": 12,
"game_id": "16003",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/03/16 16:03",
"referee": "池内　明彦"
},
{
"teams": [
"ジュビロ磐田",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "藤ヶ谷　陽介,駒野　友一,菅沼　駿哉,伊野波　雅彦,宮崎　智彦,フェルジナンド,藤田　義明,松井　大輔,ポポ,山崎　亮平,前田　遼一",
"away_shoot": 9,
"home_director": "シャムスカ",
"away_team": "ロアッソ熊本",
"weather": "晴",
"series_number": 3,
"temperature": 14.4,
"away_score": 1,
"away_start_member": "畑　実,園田　拓也,篠原　弘次郎,矢野　大輔,片山　奨典,橋本　拳人,養父　雄仁,中山　雄登,齊藤　和樹,仲間　隼斗,巻　誠一郎",
"home_score": 3,
"home_shoot": 14,
"game_id": "16005",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/03/16 16:03",
"referee": "家本　政明"
},
{
"teams": [
"ギラヴァンツ北九州",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "大谷　幸輝,田中　優毅,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,井上　翔太,渡　大生,池元　友樹",
"away_shoot": 14,
"home_director": "柱谷　幸一",
"away_team": "水戸ホーリーホック",
"weather": "晴",
"series_number": 3,
"temperature": 15.7,
"away_score": 0,
"away_start_member": "本間　幸司,田向　泰輝,新里　亮,冨田　大介,金　聖基,船谷　圭祐,内田　航平,中里　崇宏,田中　雄大,三島　康平,馬場　賢治",
"home_score": 1,
"home_shoot": 6,
"game_id": "16006",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/03/16 16:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"湘南ベルマーレ",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,宇佐美　宏和,菊地　俊介,永木　亮太,菊池　大介,大槻　周平,ウェリントン,武富　孝介",
"away_shoot": 7,
"home_director": "曺　貴裁",
"away_team": "コンサドーレ札幌",
"weather": "晴",
"series_number": 3,
"temperature": 16.5,
"away_score": 0,
"away_start_member": "金山　隼樹,日高　拓磨,櫛引　一紀,奈良　竜樹,上原　慎也,河合　竜二,宮澤　裕樹,荒野　拓馬,前田　俊介,砂川　誠,内村　圭宏",
"home_score": 2,
"home_shoot": 15,
"game_id": "16004",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/03/16 16:04",
"referee": "吉田　寿光"
},
{
"teams": [
"ファジアーノ岡山",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "中林　洋次,近藤　徹志,竹田　忠嗣,植田　龍仁朗,石原　崇兆,仙石　廉,千明　聖典,田所　諒,妹尾　隆佑,押谷　祐樹,荒田　智之",
"away_shoot": 10,
"home_director": "影山　雅永",
"away_team": "ザスパクサツ群馬",
"weather": "晴",
"series_number": 3,
"temperature": 15.2,
"away_score": 2,
"away_start_member": "北　一真,小柳　達司,クォン　ハンジン,黄　誠秀,夛田　凌輔,瀬川　和樹,加藤　弘堅,永田　亮太,平繁　龍一,エデル,小林　竜樹",
"home_score": 1,
"home_shoot": 12,
"game_id": "16007",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/03/16 17:03",
"referee": "河合　英治"
},
{
"teams": [
"水戸ホーリーホック",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "本間　幸司,新里　亮,冨田　大介,金　聖基,田中　雄大,中里　崇宏,小谷野　顕治,広瀬　陸斗,船谷　圭祐,三島　康平,馬場　賢治",
"away_shoot": 7,
"home_director": "柱谷　哲二",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 4,
"temperature": 14.3,
"away_score": 1,
"away_start_member": "中林　洋次,近藤　徹志,竹田　忠嗣,植田　龍仁朗,鎌田　翔雅,千明　聖典,島田　譲,田所　諒,石原　崇兆,押谷　祐樹,久保　裕一",
"home_score": 0,
"home_shoot": 8,
"game_id": "16008",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/03/22 13:03",
"referee": "岡　宏道"
},
{
"teams": [
"カマタマーレ讃岐",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "森田　耕一郎,西野　泰正,岡村　和哉,野口　遼太,堀河　俊大,綱田　大志,山本　翔平,小澤　雄希,アンドレア,高橋　泰,我那覇　和樹",
"away_shoot": 17,
"home_director": "北野　誠",
"away_team": "松本山雅ＦＣ",
"weather": "晴",
"series_number": 4,
"temperature": 16.8,
"away_score": 5,
"away_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,多々良　敦斗,岩沼　俊介,喜山　康平,岩間　雄大,岩上　祐三,船山　貴之,塩沢　勝吾",
"home_score": 0,
"home_shoot": 7,
"game_id": "16011",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/03/22 13:03",
"referee": "塚田　健太"
},
{
"teams": [
"カターレ富山",
"京都サンガF.C."
],
"away_director": "バドゥ",
"home_start_member": "水谷　雄一,木村　勝太,御厨　貴文,平出　涼,内田　健太,大西　容平,キム　ヨングン,ソ　ヨンドク,白崎　凌兵,中島　翔哉,苔口　卓也",
"away_shoot": 10,
"home_director": "安間　貴義",
"away_team": "京都サンガF.C.",
"weather": "曇",
"series_number": 4,
"temperature": 9.2,
"away_score": 2,
"away_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,駒井　善成,ジャイロ,工藤　浩平,山瀬　功治,大黒　将志,アレッサンドロ",
"home_score": 1,
"home_shoot": 13,
"game_id": "16009",
"home_team": "カターレ富山",
"game_start_at": "2014/03/22 13:04",
"referee": "小屋　幸栄"
},
{
"teams": [
"ＦＣ岐阜",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "川口　能活,杉山　新,木谷　公亮,阿部　正紀,野垣内　俊,水野　泰輔,宮沢　正史,スティッペ,髙地　系治,難波　宏明,ナザリト",
"away_shoot": 11,
"home_director": "ラモス　瑠偉",
"away_team": "湘南ベルマーレ",
"weather": "晴",
"series_number": 4,
"temperature": 11.3,
"away_score": 3,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,宇佐美　宏和,菊地　俊介,永木　亮太,菊池　大介,大槻　周平,ウェリントン,武富　孝介",
"home_score": 2,
"home_shoot": 5,
"game_id": "16010",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/03/22 13:04",
"referee": "松尾　一"
},
{
"teams": [
"栃木ＳＣ",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "鈴木　智幸,山形　辰徳,赤井　秀行,ドゥドゥ,イ　ミンス,小野寺　達也,湯澤　洋介,大久保　哲哉,廣瀬　浩二,近藤　祐介,瀬沼　優司",
"away_shoot": 8,
"home_director": "阪倉　裕二",
"away_team": "ザスパクサツ群馬",
"weather": "晴",
"series_number": 4,
"temperature": 11.9,
"away_score": 0,
"away_start_member": "北　一真,夛田　凌輔,小柳　達司,クォン　ハンジン,瀬川　和樹,小林　竜樹,加藤　弘堅,黄　誠秀,永田　亮太,平繁　龍一,エデル",
"home_score": 3,
"home_shoot": 16,
"game_id": "16012",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/03/22 14:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"ロアッソ熊本",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "畑　実,園田　拓也,篠原　弘次郎,矢野　大輔,片山　奨典,橋本　拳人,養父　雄仁,五領　淳樹,齊藤　和樹,仲間　隼斗,澤田　崇",
"away_shoot": 10,
"home_director": "小野　剛",
"away_team": "大分トリニータ",
"weather": "晴一時曇",
"series_number": 4,
"temperature": 13.6,
"away_score": 1,
"away_start_member": "武田　洋平,チェ　ジョンハン,阪田　章裕,高木　和道,若狭　大志,伊藤　大介,末吉　隼也,西　弘則,田中　輝希,風間　宏矢,伊佐　耕平",
"home_score": 1,
"home_shoot": 12,
"game_id": "16013",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/03/22 15:03",
"referee": "野田　祐樹"
},
{
"teams": [
"コンサドーレ札幌",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "李　昊乗,日高　拓磨,薗田　淳,奈良　竜樹,上原　慎也,河合　竜二,上原　拓郎,石井　謙伍,前田　俊介,砂川　誠,内村　圭宏",
"away_shoot": 6,
"home_director": "財前　恵一",
"away_team": "ギラヴァンツ北九州",
"weather": "屋内",
"series_number": 4,
"temperature": 20,
"away_score": 0,
"away_start_member": "大谷　幸輝,田中　優毅,渡邉　将基,前田　和哉,冨士　祐樹,下村　東美,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"home_score": 3,
"home_shoot": 11,
"game_id": "16014",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/03/22 16:03",
"referee": "今村　義朗"
},
{
"teams": [
"横浜ＦＣ",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "南　雄太,市村　篤司,ドウグラス,野上　結貴,中島　崇典,安　英学,松下　年宏,寺田　紳一,小野瀬　康介,野崎　陽介,パク　ソンホ",
"away_shoot": 12,
"home_director": "山口　素弘",
"away_team": "モンテディオ山形",
"weather": "晴",
"series_number": 4,
"temperature": 10.7,
"away_score": 1,
"away_start_member": "清水　健太,山田　拓巳,當間　建文,イ　ジュヨン,舩津　徹也,秋葉　勝,宮阪　政樹,中島　裕希,ディエゴ,伊東　俊,萬代　宏樹",
"home_score": 2,
"home_shoot": 5,
"game_id": "16015",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/03/22 16:03",
"referee": "長谷　拓"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"ジェフユナイテッド千葉"
],
"away_director": "鈴木　淳",
"home_start_member": "大久保　択生,岡本　拓也,山口　貴弘,古部　健太,神崎　大輔,黒木　聖仁,三原　雅俊,野田　紘史,奥埜　博亮,東　浩史,佐藤　洸一",
"away_shoot": 12,
"home_director": "高木　琢也",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 4,
"temperature": 14.2,
"away_score": 1,
"away_start_member": "岡本　昌弘,竹内　彬,大岩　一貴,山口　智,中村　太亮,山口　慶,佐藤　健太郎,田中　佑昌,山中　亮輔,町田　也真人,ケンペス",
"home_score": 2,
"home_shoot": 11,
"game_id": "16016",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/03/22 16:03",
"referee": "家本　政明"
},
{
"teams": [
"愛媛ＦＣ",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "児玉　剛,三原　向平,村上　佑介,林堂　眞,西岡　大輝,キム　ミンジェ,渡邊　一仁,原川　力,堀米　勇輝,西田　剛,表原　玄太",
"away_shoot": 3,
"home_director": "石丸　清隆",
"away_team": "東京ヴェルディ",
"weather": "晴",
"series_number": 4,
"temperature": 10.4,
"away_score": 1,
"away_start_member": "佐藤　優也,安西　幸輝,吉野　恭平,金　鐘必,安在　和樹,姜　成浩,田村　直也,高木　大輔,前田　直輝,南　秀仁,常盤　聡",
"home_score": 2,
"home_shoot": 15,
"game_id": "16017",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/03/22 17:04",
"referee": "前田　拓哉"
},
{
"teams": [
"ジュビロ磐田",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "藤ヶ谷　陽介,菅沼　駿哉,駒野　友一,森下　俊,松井　大輔,山本　康裕,フェルジナンド,藤田　義明,ポポ,山崎　亮平,前田　遼一",
"away_shoot": 15,
"home_director": "シャムスカ",
"away_team": "アビスパ福岡",
"weather": "晴",
"series_number": 4,
"temperature": 7.8,
"away_score": 3,
"away_start_member": "清水　圭介,堤　俊輔,イ　グァンソン,パク　ゴン,オ　チャンヒョン,三島　勇太,阿部　巧,武田　英二郎,中原　秀人,坂田　大輔,城後　寿",
"home_score": 3,
"home_shoot": 11,
"game_id": "16018",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/03/22 19:03",
"referee": "村上　伸次"
},
{
"teams": [
"アルビレックス新潟",
"サガン鳥栖"
],
"away_director": "尹　晶煥",
"home_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,金　珍洙,レオ　シルバ,成岡　翔,田中　亜土夢,岡本　英也,鈴木　武蔵,川又　堅碁",
"away_shoot": 16,
"home_director": "柳下　正明",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 4,
"temperature": 11.8,
"away_score": 0,
"away_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,谷口　博之,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 1,
"home_shoot": 8,
"game_id": "15695",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/03/23 13:03",
"referee": "東城　穣"
},
{
"teams": [
"ヴァンフォーレ甲府",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "岡　大生,青山　直晃,山本　英臣,佐々木　翔,福田　健介,新井　涼平,マルキーニョス　パラナ,阿部　翔平,石原　克哉,河本　明人,クリスティアーノ",
"away_shoot": 4,
"home_director": "城福　浩",
"away_team": "横浜Ｆ・マリノス",
"weather": "晴",
"series_number": 4,
"temperature": 17.8,
"away_score": 0,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,富澤　清太郎,兵藤　慎剛,中村　俊輔,佐藤　優平,伊藤　翔",
"home_score": 1,
"home_shoot": 6,
"game_id": "15696",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/03/23 14:04",
"referee": "井上　知大"
},
{
"teams": [
"徳島ヴォルティス",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "松井　謙弥,福元　洋平,橋内　優也,千代反田　充,アレックス,濱田　武,斉藤　大介,衛藤　裕,大﨑　淳矢,クレイトン　ドミンゲス,高崎　寛之",
"away_shoot": 9,
"home_director": "小林　伸二",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 4,
"temperature": 12.4,
"away_score": 2,
"away_start_member": "菅野　孝憲,高山　薫,鈴木　大輔,近藤　直也,橋本　和,ハン　グギョン,レアンドロ　ドミンゲス,大谷　秀和,工藤　壮人,レアンドロ,田中　順也",
"home_score": 0,
"home_shoot": 4,
"game_id": "15697",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/03/23 14:04",
"referee": "山本　雄大"
},
{
"teams": [
"大宮アルディージャ",
"ベガルタ仙台"
],
"away_director": "グラハム　アーノルド",
"home_start_member": "北野　貴之,今井　智基,菊地　光将,高橋　祥平,中村　北斗,家長　昭博,片岡　洋介,金澤　慎,渡邉　大剛,ズラタン,ラドンチッチ",
"away_shoot": 10,
"home_director": "大熊　清",
"away_team": "ベガルタ仙台",
"weather": "晴",
"series_number": 4,
"temperature": 16.9,
"away_score": 0,
"away_start_member": "関　憲太郎,菅井　直樹,渡辺　広大,石川　直樹,二見　宏志,太田　吉彰,鎌田　次郎,富田　晋伍,梁　勇基,武藤　雄樹,赤嶺　真吾",
"home_score": 4,
"home_shoot": 8,
"game_id": "15700",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/03/23 15:03",
"referee": "佐藤　隆治"
},
{
"teams": [
"鹿島アントラーズ",
"セレッソ大阪"
],
"away_director": "ランコ　ポポヴィッチ",
"home_start_member": "曽ヶ端　準,伊東　幸敏,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,豊川　雄太,土居　聖真,ダヴィ",
"away_shoot": 12,
"home_director": "トニーニョ　セレーゾ",
"away_team": "セレッソ大阪",
"weather": "晴",
"series_number": 4,
"temperature": 13.9,
"away_score": 2,
"away_start_member": "キム　ジンヒョン,丸橋　祐介,酒本　憲幸,山下　達也,ゴイコ　カチャル,長谷川　アーリアジャスール,山口　蛍,南野　拓実,杉本　健勇,柿谷　曜一朗,フォルラン",
"home_score": 0,
"home_shoot": 16,
"game_id": "15698",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/03/23 15:04",
"referee": "吉田　寿光"
},
{
"teams": [
"浦和レッズ",
"清水エスパルス"
],
"away_director": "2014年3月13日付Jリーグ制裁により、無観客での試合開催",
"home_start_member": "西川　周作,阿部　勇樹,那須　大亮,槙野　智章,平川　忠亮,鈴木　啓太,柏木　陽介,宇賀神　友弥,梅崎　司,原口　元気,興梠　慎三",
"away_shoot": 6,
"home_director": "アフシン　ゴトビ",
"away_team": "清水エスパルス",
"weather": "晴",
"series_number": 4,
"temperature": 16.2,
"away_score": 1,
"away_start_member": "櫛引　政敏,石毛　秀樹,平岡　康裕,カルフィン　ヨン　ア　ピン,吉田　豊,河井　陽介,六平　光成,竹内　涼,大前　元紀,ノヴァコヴィッチ,長沢　駿",
"home_score": 1,
"home_shoot": 17,
"game_id": "15699",
"home_team": "浦和レッズ",
"game_start_at": "2014/03/23 15:04",
"referee": "飯田　淳平"
},
{
"teams": [
"名古屋グランパス",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "楢﨑　正剛,刀根　亮輔,大武　峻,田中　マルクス闘莉王,本多　勇喜,枝村　匠馬,磯村　亮太,ダニルソン,小川　佳純,ケネディ,玉田　圭司",
"away_shoot": 6,
"home_director": "西野　朗",
"away_team": "ヴィッセル神戸",
"weather": "晴",
"series_number": 4,
"temperature": 16.4,
"away_score": 1,
"away_start_member": "山本　海人,奥井　諒,岩波　拓也,増川　隆洋,茂木　弘人,チョン　ウヨン,シンプリシオ,森岡　亮太,小川　慶治朗,ペドロ　ジュニオール,マルキーニョス",
"home_score": 2,
"home_shoot": 10,
"game_id": "15701",
"home_team": "名古屋グランパス",
"game_start_at": "2014/03/23 15:04",
"referee": "高山　啓義"
},
{
"teams": [
"ガンバ大阪",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "東口　順昭,加地　亮,岩下　敬輔,丹羽　大輝,藤春　廣輝,明神　智和,今野　泰幸,阿部　浩之,倉田　秋,リンス,遠藤　保仁",
"away_shoot": 14,
"home_director": "長谷川　健太",
"away_team": "サンフレッチェ広島",
"weather": "晴",
"series_number": 4,
"temperature": 13.9,
"away_score": 1,
"away_start_member": "林　卓人,塩谷　司,丸谷　拓也,水本　裕貴,ミキッチ,青山　敏弘,森﨑　和幸,山岸　智,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"home_score": 1,
"home_shoot": 12,
"game_id": "15702",
"home_team": "ガンバ大阪",
"game_start_at": "2014/03/23 16:03",
"referee": "中村　太"
},
{
"teams": [
"ＦＣ東京",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,加賀　健一,太田　宏介,高橋　秀人,米本　拓司,三田　啓貴,東　慶悟,渡邉　千真,エドゥー",
"away_shoot": 12,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "川崎フロンターレ",
"weather": "晴",
"series_number": 4,
"temperature": 9.6,
"away_score": 4,
"away_start_member": "西部　洋平,田中　裕介,ジェシ,井川　祐輔,谷口　彰悟,大島　僚太,中村　憲剛,森谷　賢太郎,レナト,小林　悠,大久保　嘉人",
"home_score": 0,
"home_shoot": 6,
"game_id": "15703",
"home_team": "ＦＣ東京",
"game_start_at": "2014/03/23 19:04",
"referee": "岡部　拓人"
},
{
"teams": [
"川崎フロンターレ",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "西部　洋平,田中　裕介,ジェシ,井川　祐輔,谷口　彰悟,大島　僚太,中村　憲剛,森谷　賢太郎,レナト,小林　悠,大久保　嘉人",
"away_shoot": 8,
"home_director": "風間　八宏",
"away_team": "名古屋グランパス",
"weather": "晴",
"series_number": 5,
"temperature": 16.8,
"away_score": 0,
"away_start_member": "楢﨑　正剛,牟田　雄祐,大武　峻,田中　マルクス闘莉王,本多　勇喜,枝村　匠馬,磯村　亮太,ダニルソン,小川　佳純,玉田　圭司,ケネディ",
"home_score": 1,
"home_shoot": 12,
"game_id": "15705",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/03/28 19:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"ベガルタ仙台",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "関　憲太郎,石川　大徳,渡辺　広大,鎌田　次郎,石川　直樹,マグリンチィ,角田　誠,富田　晋伍,梁　勇基,柳沢　敦,ウイルソン",
"away_shoot": 9,
"home_director": "グラハム　アーノルド",
"away_team": "ヴァンフォーレ甲府",
"weather": "晴",
"series_number": 5,
"temperature": 21.3,
"away_score": 1,
"away_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,福田　健介,新井　涼平,マルキーニョス　パラナ,阿部　翔平,河本　明人,石原　克哉,クリスティアーノ",
"home_score": 1,
"home_shoot": 4,
"game_id": "15706",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/03/29 14:04",
"referee": "榎本　一慶"
},
{
"teams": [
"横浜Ｆ・マリノス",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,富澤　清太郎,藤本　淳吾,中村　俊輔,兵藤　慎剛,伊藤　翔",
"away_shoot": 11,
"home_director": "樋口　靖洋",
"away_team": "鹿島アントラーズ",
"weather": "晴",
"series_number": 5,
"temperature": 20.8,
"away_score": 3,
"away_start_member": "曽ヶ端　準,伊東　幸敏,青木　剛,昌子　源,山本　脩斗,小笠原　満男,柴崎　岳,遠藤　康,中村　充孝,土居　聖真,ダヴィ",
"home_score": 1,
"home_shoot": 6,
"game_id": "15707",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/03/29 14:04",
"referee": "家本　政明"
},
{
"teams": [
"セレッソ大阪",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "キム　ジンヒョン,丸橋　祐介,酒本　憲幸,山下　達也,ゴイコ　カチャル,長谷川　アーリアジャスール,山口　蛍,南野　拓実,杉本　健勇,柿谷　曜一朗,フォルラン",
"away_shoot": 13,
"home_director": "ランコ　ポポヴィッチ",
"away_team": "アルビレックス新潟",
"weather": "晴のち曇",
"series_number": 5,
"temperature": 22.5,
"away_score": 0,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,金　珍洙,レオ　シルバ,成岡　翔,田中　亜土夢,岡本　英也,鈴木　武蔵,川又　堅碁",
"home_score": 0,
"home_shoot": 8,
"game_id": "15708",
"home_team": "セレッソ大阪",
"game_start_at": "2014/03/29 14:04",
"referee": "井上　知大"
},
{
"teams": [
"サンフレッチェ広島",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,ミキッチ,青山　敏弘,森﨑　和幸,柏　好文,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"away_shoot": 9,
"home_director": "森保　一",
"away_team": "徳島ヴォルティス",
"weather": "雨",
"series_number": 5,
"temperature": 13.9,
"away_score": 1,
"away_start_member": "松井　謙弥,福元　洋平,橋内　優也,千代反田　充,那須川　将大,濱田　武,小島　秀仁,クレイトン　ドミンゲス,大﨑　淳矢,津田　知宏,高崎　寛之",
"home_score": 3,
"home_shoot": 11,
"game_id": "15709",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/03/29 14:04",
"referee": "廣瀬　格"
},
{
"teams": [
"柏レイソル",
"大宮アルディージャ"
],
"away_director": "大熊　清",
"home_start_member": "菅野　孝憲,鈴木　大輔,近藤　直也,渡部　博文,橋本　和,高山　薫,栗澤　僚一,大谷　秀和,レアンドロ　ドミンゲス,レアンドロ,工藤　壮人",
"away_shoot": 4,
"home_director": "ネルシーニョ",
"away_team": "大宮アルディージャ",
"weather": "晴時々曇",
"series_number": 5,
"temperature": 20.3,
"away_score": 2,
"away_start_member": "北野　貴之,今井　智基,菊地　光将,高橋　祥平,中村　北斗,渡邉　大剛,片岡　洋介,金澤　慎,家長　昭博,ズラタン,ラドンチッチ",
"home_score": 2,
"home_shoot": 11,
"game_id": "15710",
"home_team": "柏レイソル",
"game_start_at": "2014/03/29 15:03",
"referee": "村上　伸次"
},
{
"teams": [
"ヴィッセル神戸",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "山本　海人,高橋　峻希,岩波　拓也,増川　隆洋,相馬　崇人,チョン　ウヨン,シンプリシオ,森岡　亮太,小川　慶治朗,ペドロ　ジュニオール,マルキーニョス",
"away_shoot": 11,
"home_director": "安達　亮",
"away_team": "浦和レッズ",
"weather": "晴",
"series_number": 5,
"temperature": 17.7,
"away_score": 1,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,鈴木　啓太,阿部　勇樹,宇賀神　友弥,原口　元気,梅崎　司,興梠　慎三",
"home_score": 3,
"home_shoot": 18,
"game_id": "15712",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/03/29 15:04",
"referee": "扇谷　健司"
},
{
"teams": [
"清水エスパルス",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "櫛引　政敏,吉田　豊,平岡　康裕,カルフィン　ヨン　ア　ピン,河井　陽介,竹内　涼,六平　光成,大前　元紀,高木　俊幸,ノヴァコヴィッチ,長沢　駿",
"away_shoot": 7,
"home_director": "アフシン　ゴトビ",
"away_team": "ＦＣ東京",
"weather": "晴",
"series_number": 5,
"temperature": 20.5,
"away_score": 3,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,米本　拓司,野澤　英之,三田　啓貴,武藤　嘉紀,エドゥー,河野　広貴",
"home_score": 1,
"home_shoot": 8,
"game_id": "15711",
"home_team": "清水エスパルス",
"game_start_at": "2014/03/29 15:05",
"referee": "今村　義朗"
},
{
"teams": [
"サガン鳥栖",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,谷口　博之,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 8,
"home_director": "尹　晶煥",
"away_team": "ガンバ大阪",
"weather": "雨",
"series_number": 5,
"temperature": 16.1,
"away_score": 0,
"away_start_member": "東口　順昭,オ　ジェソク,岩下　敬輔,丹羽　大輝,藤春　廣輝,明神　智和,今野　泰幸,阿部　浩之,リンス,佐藤　晃大,遠藤　保仁",
"home_score": 2,
"home_shoot": 9,
"game_id": "15713",
"home_team": "サガン鳥栖",
"game_start_at": "2014/03/29 19:04",
"referee": "飯田　淳平"
},
{
"teams": [
"栃木ＳＣ",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "鈴木　智幸,山形　辰徳,チャ　ヨンファン,ドゥドゥ,イ　ミンス,廣瀬　浩二,小野寺　達也,湯澤　洋介,大久保　哲哉,近藤　祐介,瀬沼　優司",
"away_shoot": 16,
"home_director": "阪倉　裕二",
"away_team": "ジュビロ磐田",
"weather": "雨",
"series_number": 5,
"temperature": 15.7,
"away_score": 2,
"away_start_member": "藤ヶ谷　陽介,駒野　友一,伊野波　雅彦,菅沼　駿哉,松井　大輔,フェルジナンド,藤田　義明,山田　大記,ポポ,前田　遼一,山崎　亮平",
"home_score": 0,
"home_shoot": 4,
"game_id": "16019",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/03/30 13:03",
"referee": "前田　拓哉"
},
{
"teams": [
"ファジアーノ岡山",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "中林　洋次,近藤　徹志,竹田　忠嗣,植田　龍仁朗,鎌田　翔雅,千明　聖典,島田　譲,田所　諒,石原　崇兆,押谷　祐樹,久保　裕一",
"away_shoot": 11,
"home_director": "影山　雅永",
"away_team": "大分トリニータ",
"weather": "曇",
"series_number": 5,
"temperature": 17.9,
"away_score": 1,
"away_start_member": "武田　洋平,安川　有,阪田　章裕,高木　和道,岩武　克弥,末吉　隼也,伊藤　大介,木島　悠,田中　輝希,後藤　優介,高松　大樹",
"home_score": 1,
"home_shoot": 12,
"game_id": "16022",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/03/30 13:03",
"referee": "ティアニー　ポール"
},
{
"teams": [
"アビスパ福岡",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "神山　竜一,三島　勇太,阿部　巧,堤　俊輔,イ　グァンソン,中原　秀人,金森　健志,城後　寿,石津　大介,プノセバッチ,坂田　大輔",
"away_shoot": 13,
"home_director": "マリヤン　プシュニク",
"away_team": "横浜ＦＣ",
"weather": "曇",
"series_number": 5,
"temperature": 13.4,
"away_score": 0,
"away_start_member": "南　雄太,市村　篤司,ドウグラス,野上　結貴,中島　崇典,安　英学,寺田　紳一,小野瀬　康介,野崎　陽介,黒津　勝,パク　ソンホ",
"home_score": 1,
"home_shoot": 10,
"game_id": "16023",
"home_team": "アビスパ福岡",
"game_start_at": "2014/03/30 13:03",
"referee": "山本　雄大"
},
{
"teams": [
"ザスパクサツ群馬",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "北　一真,乾　大知,小柳　達司,クォン　ハンジン,瀬川　和樹,青木　孝太,加藤　弘堅,黄　誠秀,永田　亮太,平繁　龍一,野崎　桂太",
"away_shoot": 11,
"home_director": "秋葉　忠宏",
"away_team": "カターレ富山",
"weather": "曇",
"series_number": 5,
"temperature": 11.4,
"away_score": 0,
"away_start_member": "水谷　雄一,木村　勝太,平出　涼,御厨　貴文,内田　健太,秋本　倫孝,キム　ヨングン,ソ　ヨンドク,白崎　凌兵,中島　翔哉,苔口　卓也",
"home_score": 2,
"home_shoot": 7,
"game_id": "16020",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/03/30 13:04",
"referee": "三上　正一郎"
},
{
"teams": [
"松本山雅ＦＣ",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,多々良　敦斗,岩沼　俊介,岩間　雄大,喜山　康平,岩上　祐三,船山　貴之,塩沢　勝吾",
"away_shoot": 17,
"home_director": "反町　康治",
"away_team": "湘南ベルマーレ",
"weather": "雨",
"series_number": 5,
"temperature": 14.3,
"away_score": 4,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,宇佐美　宏和,菊地　俊介,永木　亮太,菊池　大介,大槻　周平,ウェリントン,武富　孝介",
"home_score": 1,
"home_shoot": 14,
"game_id": "16021",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/03/30 13:04",
"referee": "東城　穣"
},
{
"teams": [
"ギラヴァンツ北九州",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,鈴木　修人,風間　宏希,小手川　宏基,井上　翔太,渡　大生,池元　友樹",
"away_shoot": 10,
"home_director": "柱谷　幸一",
"away_team": "カマタマーレ讃岐",
"weather": "曇",
"series_number": 5,
"temperature": 12.5,
"away_score": 1,
"away_start_member": "森田　耕一郎,堀河　俊大,藤井　航大,野口　遼太,沼田　圭悟,アンドレア,綱田　大志,岡村　和哉,小澤　雄希,我那覇　和樹,高橋　泰",
"home_score": 2,
"home_shoot": 14,
"game_id": "16024",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/03/30 14:03",
"referee": "上田　益也"
},
{
"teams": [
"ジェフユナイテッド千葉",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "岡本　昌弘,天野　貴史,大岩　一貴,山口　智,中村　太亮,兵働　昭弘,山口　慶,井出　遥也,谷澤　達也,町田　也真人,ケンペス",
"away_shoot": 11,
"home_director": "鈴木　淳",
"away_team": "ロアッソ熊本",
"weather": "雨のち晴",
"series_number": 5,
"temperature": 19.6,
"away_score": 0,
"away_start_member": "畑　実,園田　拓也,篠原　弘次郎,矢野　大輔,片山　奨典,橋本　拳人,養父　雄仁,五領　淳樹,齊藤　和樹,仲間　隼斗,澤田　崇",
"home_score": 3,
"home_shoot": 10,
"game_id": "16026",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/03/30 16:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"モンテディオ山形",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "清水　健太,山田　拓巳,當間　建文,イ　ジュヨン,石川　竜也,宮阪　政樹,ロメロ　フランク,中島　裕希,ディエゴ,伊東　俊,川西　翔太",
"away_shoot": 3,
"home_director": "石﨑　信弘",
"away_team": "水戸ホーリーホック",
"weather": "雨",
"series_number": 5,
"temperature": 7.6,
"away_score": 0,
"away_start_member": "本間　幸司,新里　亮,金　聖基,田向　泰輝,田中　雄大,鈴木　雄斗,内田　航平,中里　崇宏,船谷　圭祐,馬場　賢治,三島　康平",
"home_score": 0,
"home_shoot": 8,
"game_id": "16025",
"home_team": "モンテディオ山形",
"game_start_at": "2014/03/30 16:04",
"referee": "河合　英治"
},
{
"teams": [
"京都サンガF.C.",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,駒井　善成,ジャイロ,工藤　浩平,山瀬　功治,大黒　将志,アレッサンドロ",
"away_shoot": 10,
"home_director": "バドゥ",
"away_team": "コンサドーレ札幌",
"weather": "曇時々雨",
"series_number": 5,
"temperature": 14.2,
"away_score": 1,
"away_start_member": "李　昊乗,日高　拓磨,薗田　淳,奈良　竜樹,上原　慎也,河合　竜二,宮澤　裕樹,石井　謙伍,前田　俊介,砂川　誠,内村　圭宏",
"home_score": 1,
"home_shoot": 9,
"game_id": "16027",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/03/30 16:04",
"referee": "クート　デービッド"
},
{
"teams": [
"愛媛ＦＣ",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "児玉　剛,三原　向平,村上　佑介,林堂　眞,浦田　延尚,キム　ミンジェ,渡邊　一仁,原川　力,堀米　勇輝,河原　和寿,表原　玄太",
"away_shoot": 13,
"home_director": "石丸　清隆",
"away_team": "ＦＣ岐阜",
"weather": "曇",
"series_number": 5,
"temperature": 14,
"away_score": 0,
"away_start_member": "川口　能活,野垣内　俊,木谷　公亮,阿部　正紀,三都主　アレサンドロ,水野　泰輔,宮沢　正史,太田　圭輔,髙地　系治,難波　宏明,ナザリト",
"home_score": 0,
"home_shoot": 6,
"game_id": "16028",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/03/30 16:04",
"referee": "森川　浩次"
},
{
"teams": [
"東京ヴェルディ",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "佐藤　優也,安西　幸輝,吉野　恭平,金　鐘必,舘野　俊祐,田村　直也,高木　大輔,中後　雅喜,前田　直輝,常盤　聡,平本　一樹",
"away_shoot": 14,
"home_director": "三浦　泰年",
"away_team": "Ｖ・ファーレン長崎",
"weather": "曇",
"series_number": 5,
"temperature": 17.1,
"away_score": 5,
"away_start_member": "大久保　択生,古部　健太,山口　貴弘,下田　光平,神崎　大輔,黒木　聖仁,三原　雅俊,野田　紘史,奥埜　博亮,東　浩史,佐藤　洸一",
"home_score": 1,
"home_shoot": 8,
"game_id": "16029",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/03/30 17:03",
"referee": "松尾　一"
},
{
"teams": [
"コンサドーレ札幌",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "李　昊乗,日高　拓磨,パウロン,奈良　竜樹,上原　慎也,河合　竜二,宮澤　裕樹,石井　謙伍,前田　俊介,砂川　誠,内村　圭宏",
"away_shoot": 9,
"home_director": "財前　恵一",
"away_team": "松本山雅ＦＣ",
"weather": "屋内",
"series_number": 6,
"temperature": 20.4,
"away_score": 0,
"away_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,多々良　敦斗,岩沼　俊介,岩間　雄大,喜山　康平,岩上　祐三,船山　貴之,塩沢　勝吾",
"home_score": 1,
"home_shoot": 11,
"game_id": "16030",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/04/05 13:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"カマタマーレ讃岐",
"栃木ＳＣ"
],
"away_director": "2014年4月7日規律委員会の決定 9'　永芳　卓磨選手（栃木）の警告は、警告対象選手の「人違い」により、 永芳選手の警告累積には算入しない。 本来の対象選手である中野　洋司選手（栃木）の警告累積に算入する。公式記録は変更されない。",
"home_start_member": "森田　耕一郎,武田　有祐,藤井　航大,野口　遼太,沼田　圭悟,小澤　雄希,岡村　和哉,山本　翔平,持留　新作,我那覇　和樹,高橋　泰",
"away_shoot": 4,
"home_director": "阪倉　裕二",
"away_team": "栃木ＳＣ",
"weather": "晴のち曇",
"series_number": 6,
"temperature": 15.5,
"away_score": 1,
"away_start_member": "柴崎　邦博,山形　辰徳,チャ　ヨンファン,ドゥドゥ,中野　洋司,廣瀬　浩二,小野寺　達也,永芳　卓磨,近藤　祐介,瀬沼　優司,大久保　哲哉",
"home_score": 0,
"home_shoot": 11,
"game_id": "16034",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/04/05 13:03",
"referee": "長谷　拓"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "大久保　択生,下田　光平,山口　貴弘,古部　健太,神崎　大輔,黒木　聖仁,三原　雅俊,野田　紘史,奥埜　博亮,東　浩史,佐藤　洸一",
"away_shoot": 9,
"home_director": "高木　琢也",
"away_team": "ギラヴァンツ北九州",
"weather": "曇",
"series_number": 6,
"temperature": 11.4,
"away_score": 1,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,市川　恵多,冨士　祐樹,鈴木　修人,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"home_score": 1,
"home_shoot": 12,
"game_id": "16035",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/04/05 13:03",
"referee": "篠藤　巧"
},
{
"teams": [
"水戸ホーリーホック",
"ジェフユナイテッド千葉"
],
"away_director": "鈴木　淳",
"home_start_member": "本間　幸司,田向　泰輝,金　聖基,新里　亮,田中　雄大,中里　崇宏,内田　航平,鈴木　雄斗,船谷　圭祐,三島　康平,馬場　賢治",
"away_shoot": 15,
"home_director": "柱谷　哲二",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 6,
"temperature": 15.8,
"away_score": 2,
"away_start_member": "岡本　昌弘,天野　貴史,大岩　一貴,山口　智,中村　太亮,兵働　昭弘,山口　慶,谷澤　達也,田中　佑昌,町田　也真人,ケンペス",
"home_score": 1,
"home_shoot": 10,
"game_id": "16031",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/04/05 13:04",
"referee": "ティアニー　ポール"
},
{
"teams": [
"カターレ富山",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "水谷　雄一,木村　勝太,御厨　貴文,高　准翼,内田　健太,平出　涼,大西　容平,國吉　貴博,中島　翔哉,白崎　凌兵,苔口　卓也",
"away_shoot": 11,
"home_director": "安間　貴義",
"away_team": "東京ヴェルディ",
"weather": "曇のち晴",
"series_number": 6,
"temperature": 9.8,
"away_score": 3,
"away_start_member": "佐藤　優也,安西　幸輝,井林　章,吉野　恭平,金　鐘必,田村　直也,鈴木　惇,前田　直輝,安在　和樹,常盤　聡,平本　一樹",
"home_score": 0,
"home_shoot": 7,
"game_id": "16032",
"home_team": "カターレ富山",
"game_start_at": "2014/04/05 13:04",
"referee": "野田　祐樹"
},
{
"teams": [
"ＦＣ岐阜",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "川口　能活,野垣内　俊,木谷　公亮,阿部　正紀,三都主　アレサンドロ,水野　泰輔,宮沢　正史,太田　圭輔,髙地　系治,田中　智大,ナザリト",
"away_shoot": 5,
"home_director": "ラモス　瑠偉",
"away_team": "アビスパ福岡",
"weather": "晴",
"series_number": 6,
"temperature": 14.6,
"away_score": 2,
"away_start_member": "神山　竜一,阿部　巧,三島　勇太,堤　俊輔,イ　グァンソン,城後　寿,パク　ゴン,中原　秀人,石津　大介,坂田　大輔,金森　健志",
"home_score": 1,
"home_shoot": 11,
"game_id": "16033",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/04/05 13:04",
"referee": "岡　宏道"
},
{
"teams": [
"ジュビロ磐田",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "藤ヶ谷　陽介,菅沼　駿哉,駒野　友一,伊野波　雅彦,山田　大記,松井　大輔,フェルジナンド,藤田　義明,ポポ,山崎　亮平,前田　遼一",
"away_shoot": 8,
"home_director": "シャムスカ",
"away_team": "ザスパクサツ群馬",
"weather": "晴",
"series_number": 6,
"temperature": 12.5,
"away_score": 0,
"away_start_member": "北　一真,乾　大知,小柳　達司,クォン　ハンジン,夛田　凌輔,坂井　洋平,黄　誠秀,永田　亮太,小林　竜樹,ダニエル　ロビーニョ,野崎　桂太",
"home_score": 2,
"home_shoot": 16,
"game_id": "16036",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/04/05 15:03",
"referee": "佐藤　隆治"
},
{
"teams": [
"横浜ＦＣ",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "南　雄太,市村　篤司,ドウグラス,野上　結貴,中島　崇典,寺田　紳一,佐藤　謙介,小野瀬　康介,野崎　陽介,黒津　勝,ホナウド",
"away_shoot": 9,
"home_director": "山口　素弘",
"away_team": "ロアッソ熊本",
"weather": "晴",
"series_number": 6,
"temperature": 13.2,
"away_score": 1,
"away_start_member": "畑　実,藏川　洋平,篠原　弘次郎,矢野　大輔,片山　奨典,橋本　拳人,養父　雄仁,岡本　賢明,齊藤　和樹,仲間　隼斗,澤田　崇",
"home_score": 0,
"home_shoot": 11,
"game_id": "16038",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/04/05 16:03",
"referee": "クート　デービッド"
},
{
"teams": [
"大分トリニータ",
"京都サンガF.C."
],
"away_director": "バドゥ",
"home_start_member": "武田　洋平,チェ　ジョンハン,安川　有,阪田　章裕,岩武　克弥,末吉　隼也,伊藤　大介,松本　昌也,田中　輝希,後藤　優介,高松　大樹",
"away_shoot": 8,
"home_director": "田坂　和昭",
"away_team": "京都サンガF.C.",
"weather": "屋内",
"series_number": 6,
"temperature": 8.8,
"away_score": 3,
"away_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,駒井　善成,ジャイロ,工藤　浩平,山瀬　功治,大黒　将志,アレッサンドロ",
"home_score": 0,
"home_shoot": 13,
"game_id": "16040",
"home_team": "大分トリニータ",
"game_start_at": "2014/04/05 16:03",
"referee": "木村　博之"
},
{
"teams": [
"モンテディオ山形",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "清水　健太,山田　拓巳,當間　建文,イ　ジュヨン,石川　竜也,宮阪　政樹,ロメロ　フランク,中島　裕希,ディエゴ,伊東　俊,川西　翔太",
"away_shoot": 6,
"home_director": "石﨑　信弘",
"away_team": "愛媛ＦＣ",
"weather": "曇のち雪",
"series_number": 6,
"temperature": 5.6,
"away_score": 0,
"away_start_member": "児玉　剛,三原　向平,村上　佑介,林堂　眞,浦田　延尚,キム　ミンジェ,渡邊　一仁,村上　巧,原川　力,堀米　勇輝,河原　和寿",
"home_score": 2,
"home_shoot": 15,
"game_id": "16037",
"home_team": "モンテディオ山形",
"game_start_at": "2014/04/05 16:04",
"referee": "塚田　健太"
},
{
"teams": [
"湘南ベルマーレ",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,菊地　俊介,永木　亮太,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"away_shoot": 5,
"home_director": "曺　貴裁",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 6,
"temperature": 14.6,
"away_score": 0,
"away_start_member": "中林　洋次,近藤　徹志,竹田　忠嗣,田所　諒,久木田　紳吾,千明　聖典,島田　譲,染矢　一樹,石原　崇兆,押谷　祐樹,林　容平",
"home_score": 2,
"home_shoot": 26,
"game_id": "16039",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/04/05 16:04",
"referee": "井上　知大"
},
{
"teams": [
"アルビレックス新潟",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,金　珍洙,レオ　シルバ,成岡　翔,田中　亜土夢,岡本　英也,鈴木　武蔵,川又　堅碁",
"away_shoot": 12,
"home_director": "柳下　正明",
"away_team": "横浜Ｆ・マリノス",
"weather": "晴",
"series_number": 6,
"temperature": 8.9,
"away_score": 0,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,小椋　祥平,兵藤　慎剛,中村　俊輔,齋藤　学,伊藤　翔",
"home_score": 0,
"home_shoot": 7,
"game_id": "15714",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/04/06 13:03",
"referee": "松尾　一"
},
{
"teams": [
"名古屋グランパス",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "楢﨑　正剛,刀根　亮輔,大武　峻,田中　マルクス闘莉王,本多　勇喜,矢田　旭,磯村　亮太,田口　泰士,小川　佳純,玉田　圭司,ケネディ",
"away_shoot": 16,
"home_director": "西野　朗",
"away_team": "サンフレッチェ広島",
"weather": "屋内",
"series_number": 6,
"temperature": 10.7,
"away_score": 5,
"away_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,ミキッチ,青山　敏弘,森﨑　和幸,柏　好文,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"home_score": 2,
"home_shoot": 10,
"game_id": "15715",
"home_team": "名古屋グランパス",
"game_start_at": "2014/04/06 13:04",
"referee": "東城　穣"
},
{
"teams": [
"徳島ヴォルティス",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "松井　謙弥,福元　洋平,橋内　優也,青山　隼,那須川　将大,濱田　武,小島　秀仁,衛藤　裕,大﨑　淳矢,クレイトン　ドミンゲス,高崎　寛之",
"away_shoot": 13,
"home_director": "小林　伸二",
"away_team": "川崎フロンターレ",
"weather": "晴",
"series_number": 6,
"temperature": 11.3,
"away_score": 4,
"away_start_member": "西部　洋平,田中　裕介,ジェシ,井川　祐輔,谷口　彰悟,大島　僚太,中村　憲剛,森谷　賢太郎,レナト,森島　康仁,大久保　嘉人",
"home_score": 0,
"home_shoot": 1,
"game_id": "15716",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/04/06 13:04",
"referee": "吉田　寿光"
},
{
"teams": [
"柏レイソル",
"セレッソ大阪"
],
"away_director": "ランコ　ポポヴィッチ",
"home_start_member": "菅野　孝憲,キム　チャンス,鈴木　大輔,近藤　直也,渡部　博文,高山　薫,大谷　秀和,茨田　陽生,田中　順也,工藤　壮人,レアンドロ",
"away_shoot": 10,
"home_director": "ネルシーニョ",
"away_team": "セレッソ大阪",
"weather": "曇のち晴",
"series_number": 6,
"temperature": 12.1,
"away_score": 1,
"away_start_member": "キム　ジンヒョン,丸橋　祐介,酒本　憲幸,山下　達也,ゴイコ　カチャル,扇原　貴宏,長谷川　アーリアジャスール,山口　蛍,南野　拓実,柿谷　曜一朗,フォルラン",
"home_score": 2,
"home_shoot": 10,
"game_id": "15718",
"home_team": "柏レイソル",
"game_start_at": "2014/04/06 15:03",
"referee": "高山　啓義"
},
{
"teams": [
"大宮アルディージャ",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "北野　貴之,今井　智基,菊地　光将,高橋　祥平,中村　北斗,渡邉　大剛,片岡　洋介,金澤　慎,家長　昭博,ズラタン,ラドンチッチ",
"away_shoot": 10,
"home_director": "大熊　清",
"away_team": "ヴィッセル神戸",
"weather": "曇のち晴",
"series_number": 6,
"temperature": 12.1,
"away_score": 3,
"away_start_member": "山本　海人,高橋　峻希,岩波　拓也,増川　隆洋,相馬　崇人,チョン　ウヨン,森岡　亮太,小川　慶治朗,ペドロ　ジュニオール,シンプリシオ,マルキーニョス",
"home_score": 0,
"home_shoot": 7,
"game_id": "15717",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/04/06 15:04",
"referee": "飯田　淳平"
},
{
"teams": [
"ヴァンフォーレ甲府",
"清水エスパルス"
],
"away_director": "*** 甲府 10 クリスティアーノの警告は試合終了後の警告",
"home_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,福田　健介,新井　涼平,マルキーニョス　パラナ,阿部　翔平,河本　明人,ジウシーニョ,クリスティアーノ",
"away_shoot": 6,
"home_director": "アフシン　ゴトビ",
"away_team": "清水エスパルス",
"weather": "晴のち曇",
"series_number": 6,
"temperature": 9.9,
"away_score": 1,
"away_start_member": "櫛引　政敏,ヤコヴィッチ,平岡　康裕,カルフィン　ヨン　ア　ピン,吉田　豊,竹内　涼,六平　光成,河井　陽介,大前　元紀,長沢　駿,ノヴァコヴィッチ",
"home_score": 0,
"home_shoot": 7,
"game_id": "15719",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/04/06 15:04",
"referee": "岡部　拓人"
},
{
"teams": [
"ガンバ大阪",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "東口　順昭,加地　亮,岩下　敬輔,丹羽　大輝,藤春　廣輝,遠藤　保仁,今野　泰幸,阿部　浩之,倉田　秋,佐藤　晃大,リンス",
"away_shoot": 17,
"home_director": "長谷川　健太",
"away_team": "鹿島アントラーズ",
"weather": "曇時々晴一時雨",
"series_number": 6,
"temperature": 7.8,
"away_score": 2,
"away_start_member": "曽ヶ端　準,伊東　幸敏,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,ダヴィ",
"home_score": 0,
"home_shoot": 6,
"game_id": "15721",
"home_team": "ガンバ大阪",
"game_start_at": "2014/04/06 16:03",
"referee": "扇谷　健司"
},
{
"teams": [
"ＦＣ東京",
"サガン鳥栖"
],
"away_director": "尹　晶煥",
"home_start_member": "権田　修一,徳永　悠平,加賀　健一,吉本　一謙,太田　宏介,米本　拓司,野澤　英之,東　慶悟,エドゥー,平山　相太,河野　広貴",
"away_shoot": 9,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "サガン鳥栖",
"weather": "曇のち晴",
"series_number": 6,
"temperature": 10,
"away_score": 1,
"away_start_member": "林　彰洋,丹羽　竜平,キム　ミンヒョク,呂　成海,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 2,
"home_shoot": 11,
"game_id": "15720",
"home_team": "ＦＣ東京",
"game_start_at": "2014/04/06 16:04",
"referee": "中村　太"
},
{
"teams": [
"浦和レッズ",
"ベガルタ仙台"
],
"away_director": "グラハム　アーノルド",
"home_start_member": "西川　周作,森脇　良太,永田　充,槙野　智章,平川　忠亮,柏木　陽介,阿部　勇樹,宇賀神　友弥,原口　元気,興梠　慎三,李　忠成",
"away_shoot": 6,
"home_director": "ペトロヴィッチ",
"away_team": "ベガルタ仙台",
"weather": "晴",
"series_number": 6,
"temperature": 7.7,
"away_score": 0,
"away_start_member": "関　憲太郎,菅井　直樹,渡辺　広大,鎌田　次郎,石川　直樹,太田　吉彰,富田　晋伍,角田　誠,梁　勇基,柳沢　敦,ウイルソン",
"home_score": 4,
"home_shoot": 17,
"game_id": "15722",
"home_team": "浦和レッズ",
"game_start_at": "2014/04/06 19:04",
"referee": "西村　雄一"
},
{
"teams": [
"川崎フロンターレ",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "西部　洋平,田中　裕介,ジェシ,井川　祐輔,谷口　彰悟,パウリーニョ,中村　憲剛,森谷　賢太郎,山本　真希,安　柄俊,大久保　嘉人",
"away_shoot": 8,
"home_director": "風間　八宏",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 7,
"temperature": 13.1,
"away_score": 1,
"away_start_member": "菅野　孝憲,キム　チャンス,鈴木　大輔,近藤　直也,渡部　博文,高山　薫,ハン　グギョン,大谷　秀和,田中　順也,レアンドロ,工藤　壮人",
"home_score": 1,
"home_shoot": 16,
"game_id": "15723",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/04/11 19:04",
"referee": "東城　穣"
},
{
"teams": [
"横浜Ｆ・マリノス",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,小椋　祥平,兵藤　慎剛,中村　俊輔,齋藤　学,伊藤　翔",
"away_shoot": 11,
"home_director": "樋口　靖洋",
"away_team": "ベガルタ仙台",
"weather": "晴",
"series_number": 7,
"temperature": 18.4,
"away_score": 2,
"away_start_member": "関　憲太郎,武井　択也,渡辺　広大,鎌田　次郎,石川　直樹,太田　吉彰,富田　晋伍,角田　誠,梁　勇基,赤嶺　真吾,ウイルソン",
"home_score": 0,
"home_shoot": 11,
"game_id": "15724",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/04/12 14:04",
"referee": "木村　博之"
},
{
"teams": [
"セレッソ大阪",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "キム　ジンヒョン,丸橋　祐介,酒本　憲幸,山下　達也,ゴイコ　カチャル,長谷川　アーリアジャスール,山口　蛍,南野　拓実,杉本　健勇,柿谷　曜一朗,フォルラン",
"away_shoot": 12,
"home_director": "ランコ　ポポヴィッチ",
"away_team": "ガンバ大阪",
"weather": "晴",
"series_number": 7,
"temperature": 18,
"away_score": 2,
"away_start_member": "東口　順昭,加地　亮,岩下　敬輔,丹羽　大輝,藤春　廣輝,内田　達也,今野　泰幸,阿部　浩之,大森　晃太郎,リンス,遠藤　保仁",
"home_score": 2,
"home_shoot": 18,
"game_id": "15725",
"home_team": "セレッソ大阪",
"game_start_at": "2014/04/12 14:04",
"referee": "西村　雄一"
},
{
"teams": [
"鹿島アントラーズ",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "曽ヶ端　準,伊東　幸敏,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,赤﨑　秀平",
"away_shoot": 7,
"home_director": "トニーニョ　セレーゾ",
"away_team": "アルビレックス新潟",
"weather": "晴",
"series_number": 7,
"temperature": 17.7,
"away_score": 2,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,金　珍洙,レオ　シルバ,成岡　翔,田中　亜土夢,岡本　英也,鈴木　武蔵,川又　堅碁",
"home_score": 1,
"home_shoot": 14,
"game_id": "15726",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/04/12 15:04",
"referee": "飯田　淳平"
},
{
"teams": [
"清水エスパルス",
"大宮アルディージャ"
],
"away_director": "大熊　清",
"home_start_member": "櫛引　政敏,ヤコヴィッチ,平岡　康裕,カルフィン　ヨン　ア　ピン,吉田　豊,六平　光成,竹内　涼,河井　陽介,大前　元紀,ノヴァコヴィッチ,長沢　駿",
"away_shoot": 5,
"home_director": "アフシン　ゴトビ",
"away_team": "大宮アルディージャ",
"weather": "晴",
"series_number": 7,
"temperature": 14.6,
"away_score": 0,
"away_start_member": "清水　慶記,今井　智基,菊地　光将,高橋　祥平,中村　北斗,渡邉　大剛,横山　知伸,増田　誓志,家長　昭博,ズラタン,長谷川　悠",
"home_score": 2,
"home_shoot": 9,
"game_id": "15727",
"home_team": "清水エスパルス",
"game_start_at": "2014/04/12 15:04",
"referee": "廣瀬　格"
},
{
"teams": [
"名古屋グランパス",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "楢﨑　正剛,刀根　亮輔,大武　峻,田中　マルクス闘莉王,本多　勇喜,枝村　匠馬,磯村　亮太,ダニルソン,小川　佳純,ケネディ,永井　謙佑",
"away_shoot": 15,
"home_director": "西野　朗",
"away_team": "浦和レッズ",
"weather": "晴",
"series_number": 7,
"temperature": 18.4,
"away_score": 2,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,梅崎　司,柏木　陽介,阿部　勇樹,宇賀神　友弥,原口　元気,興梠　慎三,李　忠成",
"home_score": 1,
"home_shoot": 11,
"game_id": "15728",
"home_team": "名古屋グランパス",
"game_start_at": "2014/04/12 15:04",
"referee": "今村　義朗"
},
{
"teams": [
"ヴィッセル神戸",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "山本　海人,奥井　諒,岩波　拓也,増川　隆洋,高橋　峻希,チョン　ウヨン,シンプリシオ,森岡　亮太,松村　亮,ペドロ　ジュニオール,マルキーニョス",
"away_shoot": 12,
"home_director": "安達　亮",
"away_team": "徳島ヴォルティス",
"weather": "晴",
"series_number": 7,
"temperature": 15.9,
"away_score": 0,
"away_start_member": "松井　謙弥,福元　洋平,橋内　優也,青山　隼,那須川　将大,濱田　武,小島　秀仁,クレイトン　ドミンゲス,大﨑　淳矢,津田　知宏,高崎　寛之",
"home_score": 3,
"home_shoot": 15,
"game_id": "15729",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/04/12 15:04",
"referee": "家本　政明"
},
{
"teams": [
"サガン鳥栖",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "林　彰洋,丹羽　竜平,キム　ミンヒョク,小林　久晃,安田　理大,水沼　宏太,岡本　知剛,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 5,
"home_director": "尹　晶煥",
"away_team": "ヴァンフォーレ甲府",
"weather": "曇",
"series_number": 7,
"temperature": 19.4,
"away_score": 0,
"away_start_member": "岡　大生,青山　直晃,山本　英臣,佐々木　翔,福田　健介,新井　涼平,マルキーニョス　パラナ,阿部　翔平,河本　明人,盛田　剛平,クリスティアーノ",
"home_score": 2,
"home_shoot": 6,
"game_id": "15730",
"home_team": "サガン鳥栖",
"game_start_at": "2014/04/12 18:04",
"referee": "池内　明彦"
},
{
"teams": [
"サンフレッチェ広島",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,ミキッチ,青山　敏弘,森﨑　和幸,柏　好文,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"away_shoot": 7,
"home_director": "森保　一",
"away_team": "ＦＣ東京",
"weather": "曇",
"series_number": 7,
"temperature": 12.4,
"away_score": 0,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,加賀　健一,太田　宏介,米本　拓司,高橋　秀人,三田　啓貴,平山　相太,武藤　嘉紀,河野　広貴",
"home_score": 1,
"home_shoot": 7,
"game_id": "15731",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/04/12 19:04",
"referee": "吉田　寿光"
},
{
"teams": [
"栃木ＳＣ",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "柴崎　邦博,山形　辰徳,チャ　ヨンファン,ドゥドゥ,イ　ミンス,廣瀬　浩二,小野寺　達也,湯澤　洋介,大久保　哲哉,近藤　祐介,瀬沼　優司",
"away_shoot": 12,
"home_director": "阪倉　裕二",
"away_team": "松本山雅ＦＣ",
"weather": "晴",
"series_number": 7,
"temperature": 18.8,
"away_score": 2,
"away_start_member": "村山　智彦,飯田　真輝,岩間　雄大,犬飼　智也,飯尾　和也,岩沼　俊介,田中　隼磨,岩上　祐三,喜山　康平,船山　貴之,塩沢　勝吾",
"home_score": 1,
"home_shoot": 11,
"game_id": "16041",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/04/13 13:03",
"referee": "森川　浩次"
},
{
"teams": [
"大分トリニータ",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "武田　洋平,岩武　克弥,阪田　章裕,安川　有,チェ　ジョンハン,末吉　隼也,伊藤　大介,為田　大貴,松本　昌也,松本　怜,高松　大樹",
"away_shoot": 10,
"home_director": "田坂　和昭",
"away_team": "コンサドーレ札幌",
"weather": "屋内",
"series_number": 7,
"temperature": 11.7,
"away_score": 0,
"away_start_member": "李　昊乗,日高　拓磨,パウロン,奈良　竜樹,上原　慎也,河合　竜二,宮澤　裕樹,石井　謙伍,前田　俊介,砂川　誠,都倉　賢",
"home_score": 1,
"home_shoot": 14,
"game_id": "16043",
"home_team": "大分トリニータ",
"game_start_at": "2014/04/13 13:03",
"referee": "榎本　一慶"
},
{
"teams": [
"ザスパクサツ群馬",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "内藤　圭佑,夛田　凌輔,小柳　達司,クォン　ハンジン,瀬川　和樹,青木　孝太,加藤　弘堅,黄　誠秀,永田　亮太,ダニエル　ロビーニョ,小林　竜樹",
"away_shoot": 6,
"home_director": "秋葉　忠宏",
"away_team": "水戸ホーリーホック",
"weather": "晴",
"series_number": 7,
"temperature": 18.9,
"away_score": 1,
"away_start_member": "本間　幸司,新里　亮,冨田　大介,尾本　敬,広瀬　陸斗,小澤　司,中里　崇宏,内田　航平,船谷　圭祐,吉田　眞紀人,三島　康平",
"home_score": 0,
"home_shoot": 8,
"game_id": "16042",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/04/13 13:04",
"referee": "上田　益也"
},
{
"teams": [
"横浜ＦＣ",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "南　雄太,小池　純輝,ドウグラス,野上　結貴,永田　拓也,寺田　紳一,佐藤　謙介,小野瀬　康介,内田　智也,パク　ソンホ,野崎　陽介",
"away_shoot": 2,
"home_director": "山口　素弘",
"away_team": "ＦＣ岐阜",
"weather": "曇",
"series_number": 7,
"temperature": 17.8,
"away_score": 1,
"away_start_member": "川口　能活,野垣内　俊,木谷　公亮,阿部　正紀,三都主　アレサンドロ,水野　泰輔,宮沢　正史,太田　圭輔,髙地　系治,田中　智大,ナザリト",
"home_score": 0,
"home_shoot": 12,
"game_id": "16044",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/04/13 14:03",
"referee": "扇谷　健司"
},
{
"teams": [
"京都サンガF.C.",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,駒井　善成,ジャイロ,工藤　浩平,山瀬　功治,大黒　将志,アレッサンドロ",
"away_shoot": 7,
"home_director": "バドゥ",
"away_team": "モンテディオ山形",
"weather": "曇",
"series_number": 7,
"temperature": 15.9,
"away_score": 2,
"away_start_member": "清水　健太,山田　拓巳,當間　建文,イ　ジュヨン,石川　竜也,宮阪　政樹,ディエゴ,ロメロ　フランク,中島　裕希,萬代　宏樹,山﨑　雅人",
"home_score": 2,
"home_shoot": 7,
"game_id": "16045",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/04/13 14:04",
"referee": "松尾　一"
},
{
"teams": [
"愛媛ＦＣ",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "児玉　剛,ハン　ヒフン,村上　佑介,林堂　眞,浦田　延尚,三原　向平,村上　巧,吉村　圭司,原川　力,西田　剛,表原　玄太",
"away_shoot": 11,
"home_director": "石丸　清隆",
"away_team": "カターレ富山",
"weather": "雨",
"series_number": 7,
"temperature": 11.5,
"away_score": 0,
"away_start_member": "水谷　雄一,木村　勝太,御厨　貴文,吉川　拓也,内田　健太,ソ　ヨンドク,大西　容平,キム　ヨングン,中島　翔哉,苔口　卓也,白崎　凌兵",
"home_score": 4,
"home_shoot": 9,
"game_id": "16046",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/04/13 14:04",
"referee": "河合　英治"
},
{
"teams": [
"アビスパ福岡",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "神山　竜一,阿部　巧,堤　俊輔,イ　グァンソン,オ　チャンヒョン,中原　秀人,平井　将生,城後　寿,石津　大介,坂田　大輔,プノセバッチ",
"away_shoot": 21,
"home_director": "マリヤン　プシュニク",
"away_team": "Ｖ・ファーレン長崎",
"weather": "雨",
"series_number": 7,
"temperature": 13.4,
"away_score": 5,
"away_start_member": "大久保　択生,前田　悠佑,山口　貴弘,古部　健太,神崎　大輔,黒木　聖仁,三原　雅俊,野田　紘史,奥埜　博亮,東　浩史,佐藤　洸一",
"home_score": 2,
"home_shoot": 4,
"game_id": "16047",
"home_team": "アビスパ福岡",
"game_start_at": "2014/04/13 16:03",
"referee": "前田　拓哉"
},
{
"teams": [
"ギラヴァンツ北九州",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,鈴木　修人,風間　宏希,小手川　宏基,川島　大地,原　一樹,池元　友樹",
"away_shoot": 11,
"home_director": "柱谷　幸一",
"away_team": "ジュビロ磐田",
"weather": "雨",
"series_number": 7,
"temperature": 13,
"away_score": 2,
"away_start_member": "藤ヶ谷　陽介,菅沼　駿哉,駒野　友一,伊野波　雅彦,山崎　亮平,山田　大記,松井　大輔,フェルジナンド,藤田　義明,ポポ,前田　遼一",
"home_score": 3,
"home_shoot": 6,
"game_id": "16048",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/04/13 16:03",
"referee": "山本　雄大"
},
{
"teams": [
"ジェフユナイテッド千葉",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "岡本　昌弘,天野　貴史,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,山口　慶,谷澤　達也,井出　遥也,町田　也真人,ケンペス",
"away_shoot": 29,
"home_director": "鈴木　淳",
"away_team": "湘南ベルマーレ",
"weather": "曇",
"series_number": 7,
"temperature": 15,
"away_score": 6,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,宇佐美　宏和,菊地　俊介,永木　亮太,菊池　大介,大槻　周平,ウェリントン,武富　孝介",
"home_score": 0,
"home_shoot": 7,
"game_id": "16049",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/04/13 17:03",
"referee": "村上　伸次"
},
{
"teams": [
"東京ヴェルディ",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "佐藤　優也,安西　幸輝,井林　章,吉野　恭平,金　鐘必,田村　直也,鈴木　惇,前田　直輝,安在　和樹,常盤　聡,平本　一樹",
"away_shoot": 6,
"home_director": "三浦　泰年",
"away_team": "ファジアーノ岡山",
"weather": "曇",
"series_number": 7,
"temperature": 15.2,
"away_score": 1,
"away_start_member": "中林　洋次,後藤　圭太,竹田　忠嗣,田所　諒,久木田　紳吾,島田　譲,上田　康太,染矢　一樹,林　容平,荒田　智之,押谷　祐樹",
"home_score": 0,
"home_shoot": 18,
"game_id": "16050",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/04/13 17:03",
"referee": "塚田　智宏"
},
{
"teams": [
"ロアッソ熊本",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "金井　大樹,藏川　洋平,園田　拓也,矢野　大輔,片山　奨典,養父　雄仁,原田　拓,仲間　隼斗,齊藤　和樹,岡本　賢明,澤田　崇",
"away_shoot": 7,
"home_director": "小野　剛",
"away_team": "カマタマーレ讃岐",
"weather": "雨",
"series_number": 7,
"temperature": 14,
"away_score": 1,
"away_start_member": "森田　耕一郎,武田　有祐,ソン　ハンキ,野口　遼太,小澤　雄希,岡村　和哉,高木　和正,山本　翔平,アンドレア,我那覇　和樹,高橋　泰",
"home_score": 4,
"home_shoot": 12,
"game_id": "16051",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/04/13 19:03",
"referee": "佐藤　隆治"
},
{
"teams": [
"ベガルタ仙台",
"サガン鳥栖"
],
"away_director": "尹　晶煥",
"home_start_member": "関　憲太郎,菅井　直樹,渡辺　広大,石川　直樹,二見　宏志,太田　吉彰,富田　晋伍,鎌田　次郎,梁　勇基,ウイルソン,赤嶺　真吾",
"away_shoot": 9,
"home_director": "渡邉　晋",
"away_team": "サガン鳥栖",
"weather": "曇",
"series_number": 8,
"temperature": 7,
"away_score": 3,
"away_start_member": "林　彰洋,丹羽　竜平,キム　ミンヒョク,坂井　達弥,安田　理大,水沼　宏太,岡本　知剛,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 0,
"home_shoot": 18,
"game_id": "15732",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/04/19 14:04",
"referee": "扇谷　健司"
},
{
"teams": [
"徳島ヴォルティス",
"清水エスパルス"
],
"away_director": "アフシン　ゴトビ",
"home_start_member": "長谷川　徹,藤原　広太朗,橋内　優也,福元　洋平,那須川　将大,濱田　武,小島　秀仁,クレイトン　ドミンゲス,大﨑　淳矢,津田　知宏,高崎　寛之",
"away_shoot": 12,
"home_director": "小林　伸二",
"away_team": "清水エスパルス",
"weather": "晴",
"series_number": 8,
"temperature": 18.4,
"away_score": 4,
"away_start_member": "櫛引　政敏,ヤコヴィッチ,平岡　康裕,カルフィン　ヨン　ア　ピン,吉田　豊,河井　陽介,六平　光成,竹内　涼,大前　元紀,ノヴァコヴィッチ,長沢　駿",
"home_score": 0,
"home_shoot": 4,
"game_id": "15733",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/04/19 14:04",
"referee": "福島　孝一郎"
},
{
"teams": [
"鹿島アントラーズ",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "曽ヶ端　準,伊東　幸敏,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,ジャイール,土居　聖真,ダヴィ",
"away_shoot": 8,
"home_director": "トニーニョ　セレーゾ",
"away_team": "ヴィッセル神戸",
"weather": "曇時々晴",
"series_number": 8,
"temperature": 12.6,
"away_score": 3,
"away_start_member": "山本　海人,奥井　諒,岩波　拓也,増川　隆洋,高橋　峻希,チョン　ウヨン,森岡　亮太,橋本　英郎,小川　慶治朗,松村　亮,マルキーニョス",
"home_score": 2,
"home_shoot": 19,
"game_id": "15734",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/04/19 15:04",
"referee": "中村　太"
},
{
"teams": [
"柏レイソル",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "菅野　孝憲,鈴木　大輔,近藤　直也,渡部　博文,橋本　和,高山　薫,ハン　グギョン,大谷　秀和,田中　順也,工藤　壮人,レアンドロ",
"away_shoot": 8,
"home_director": "ネルシーニョ",
"away_team": "横浜Ｆ・マリノス",
"weather": "曇",
"series_number": 8,
"temperature": 11.9,
"away_score": 0,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,富澤　清太郎,兵藤　慎剛,中村　俊輔,齋藤　学,藤田　祥史",
"home_score": 0,
"home_shoot": 7,
"game_id": "15735",
"home_team": "柏レイソル",
"game_start_at": "2014/04/19 15:04",
"referee": "村上　伸次"
},
{
"teams": [
"ＦＣ東京",
"セレッソ大阪"
],
"away_director": "ランコ　ポポヴィッチ",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,東　慶悟,エドゥー,平山　相太,河野　広貴",
"away_shoot": 12,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "セレッソ大阪",
"weather": "曇",
"series_number": 8,
"temperature": 13.2,
"away_score": 0,
"away_start_member": "キム　ジンヒョン,丸橋　祐介,酒本　憲幸,山下　達也,ゴイコ　カチャル,長谷川　アーリアジャスール,山口　蛍,南野　拓実,杉本　健勇,柿谷　曜一朗,フォルラン",
"home_score": 2,
"home_shoot": 11,
"game_id": "15736",
"home_team": "ＦＣ東京",
"game_start_at": "2014/04/19 16:04",
"referee": "家本　政明"
},
{
"teams": [
"ガンバ大阪",
"大宮アルディージャ"
],
"away_director": "大熊　清",
"home_start_member": "東口　順昭,オ　ジェソク,岩下　敬輔,丹羽　大輝,藤春　廣輝,内田　達也,遠藤　保仁,阿部　浩之,大森　晃太郎,佐藤　晃大,リンス",
"away_shoot": 10,
"home_director": "長谷川　健太",
"away_team": "大宮アルディージャ",
"weather": "曇",
"series_number": 8,
"temperature": 12.8,
"away_score": 1,
"away_start_member": "江角　浩司,今井　智基,菊地　光将,高橋　祥平,渡部　大輔,橋本　晃司,渡邉　大剛,横山　知伸,曺　永哲,家長　昭博,ズラタン",
"home_score": 2,
"home_shoot": 18,
"game_id": "15737",
"home_team": "ガンバ大阪",
"game_start_at": "2014/04/19 16:04",
"referee": "岡部　拓人"
},
{
"teams": [
"浦和レッズ",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,梅崎　司,柏木　陽介,阿部　勇樹,宇賀神　友弥,原口　元気,興梠　慎三,李　忠成",
"away_shoot": 10,
"home_director": "ペトロヴィッチ",
"away_team": "川崎フロンターレ",
"weather": "晴",
"series_number": 8,
"temperature": 11.4,
"away_score": 0,
"away_start_member": "西部　洋平,田中　裕介,ジェシ,井川　祐輔,谷口　彰悟,大島　僚太,中村　憲剛,森谷　賢太郎,レナト,小林　悠,大久保　嘉人",
"home_score": 1,
"home_shoot": 10,
"game_id": "15738",
"home_team": "浦和レッズ",
"game_start_at": "2014/04/19 17:04",
"referee": "松尾　一"
},
{
"teams": [
"ヴァンフォーレ甲府",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "岡　大生,青山　直晃,山本　英臣,佐々木　翔,福田　健介,新井　涼平,マルキーニョス　パラナ,阿部　翔平,河本　明人,盛田　剛平,クリスティアーノ",
"away_shoot": 7,
"home_director": "城福　浩",
"away_team": "名古屋グランパス",
"weather": "雨",
"series_number": 8,
"temperature": 10.9,
"away_score": 0,
"away_start_member": "楢﨑　正剛,矢野　貴章,ハーフナー　ニッキ,田中　マルクス闘莉王,本多　勇喜,小川　佳純,磯村　亮太,ダニルソン,矢田　旭,松田　力,ケネディ",
"home_score": 2,
"home_shoot": 9,
"game_id": "15739",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/04/19 19:04",
"referee": "木村　博之"
},
{
"teams": [
"コンサドーレ札幌",
"ザスパクサツ群馬"
],
"away_director": "試合開始前 審判交代 副審：前之園　晴廣　→ 第4の審判員：原尾　英祐",
"home_start_member": "李　昊乗,日高　拓磨,パウロン,奈良　竜樹,松本　怜大,河合　竜二,宮澤　裕樹,石井　謙伍,前田　俊介,菊岡　拓朗,都倉　賢",
"away_shoot": 9,
"home_director": "秋葉　忠宏",
"away_team": "ザスパクサツ群馬",
"weather": "屋内",
"series_number": 8,
"temperature": 22.6,
"away_score": 0,
"away_start_member": "内藤　圭佑,夛田　凌輔,小柳　達司,クォン　ハンジン,瀬川　和樹,青木　孝太,坂井　洋平,黄　誠秀,小林　竜樹,ダニエル　ロビーニョ,野崎　桂太",
"home_score": 1,
"home_shoot": 8,
"game_id": "16052",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/04/20 13:03",
"referee": "高山　啓義"
},
{
"teams": [
"松本山雅ＦＣ",
"京都サンガF.C."
],
"away_director": "バドゥ",
"home_start_member": "村山　智彦,岩間　雄大,飯尾　和也,飯田　真輝,犬飼　智也,喜山　康平,岩沼　俊介,田中　隼磨,塩沢　勝吾,岩上　祐三,船山　貴之",
"away_shoot": 12,
"home_director": "反町　康治",
"away_team": "京都サンガF.C.",
"weather": "曇",
"series_number": 8,
"temperature": 13.3,
"away_score": 2,
"away_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,駒井　善成,ジャイロ,工藤　浩平,山瀬　功治,大黒　将志,有田　光希",
"home_score": 2,
"home_shoot": 7,
"game_id": "16053",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/04/20 13:03",
"referee": "河合　英治"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "大久保　択生,前田　悠佑,山口　貴弘,古部　健太,神崎　大輔,三原　雅俊,黒木　聖仁,野田　紘史,東　浩史,奥埜　博亮,小松　塁",
"away_shoot": 6,
"home_director": "高木　琢也",
"away_team": "愛媛ＦＣ",
"weather": "曇",
"series_number": 8,
"temperature": 18.6,
"away_score": 1,
"away_start_member": "児玉　剛,ハン　ヒフン,村上　佑介,林堂　眞,浦田　延尚,三原　向平,村上　巧,吉村　圭司,原川　力,堀米　勇輝,渡辺　亮太",
"home_score": 2,
"home_shoot": 16,
"game_id": "16056",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/04/20 13:03",
"referee": "日高　晴樹"
},
{
"teams": [
"カターレ富山",
"ジェフユナイテッド千葉"
],
"away_director": "鈴木　淳",
"home_start_member": "水谷　雄一,木村　勝太,平出　涼,吉川　拓也,田中　寛己,大西　容平,秋本　倫孝,ソ　ヨンドク,中島　翔哉,三上　陽輔,白崎　凌兵",
"away_shoot": 9,
"home_director": "安間　貴義",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 8,
"temperature": 13.4,
"away_score": 1,
"away_start_member": "岡本　昌弘,天野　貴史,大岩　一貴,山口　智,中村　太亮,兵働　昭弘,佐藤　勇人,田中　佑昌,井出　遥也,町田　也真人,谷澤　達也",
"home_score": 1,
"home_shoot": 15,
"game_id": "16054",
"home_team": "カターレ富山",
"game_start_at": "2014/04/20 13:04",
"referee": "塚田　健太"
},
{
"teams": [
"ＦＣ岐阜",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "川口　能活,野垣内　俊,ヘニキ,木谷　公亮,三都主　アレサンドロ,水野　泰輔,宮沢　正史,太田　圭輔,髙地　系治,田中　智大,ナザリト",
"away_shoot": 9,
"home_director": "ラモス　瑠偉",
"away_team": "栃木ＳＣ",
"weather": "曇",
"series_number": 8,
"temperature": 15.3,
"away_score": 3,
"away_start_member": "鈴木　智幸,山形　辰徳,チャ　ヨンファン,ドゥドゥ,イ　ミンス,湯澤　洋介,岡根　直哉,小野寺　達也,近藤　祐介,廣瀬　浩二,瀬沼　優司",
"home_score": 1,
"home_shoot": 15,
"game_id": "16055",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/04/20 13:04",
"referee": "野田　祐樹"
},
{
"teams": [
"アルビレックス新潟",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,金　珍洙,成岡　翔,レオ　シルバ,田中　亜土夢,岡本　英也,鈴木　武蔵,川又　堅碁",
"away_shoot": 1,
"home_director": "柳下　正明",
"away_team": "サンフレッチェ広島",
"weather": "晴のち曇",
"series_number": 8,
"temperature": 13.8,
"away_score": 0,
"away_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,柏　好文,青山　敏弘,森﨑　和幸,清水　航平,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"home_score": 0,
"home_shoot": 12,
"game_id": "15740",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/04/20 15:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"カマタマーレ讃岐",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "森田　耕一郎,武田　有祐,藤井　航大,ソン　ハンキ,小澤　雄希,関原　凌河,岡村　和哉,高木　和正,持留　新作,西野　泰正,我那覇　和樹",
"away_shoot": 7,
"home_director": "北野　誠",
"away_team": "アビスパ福岡",
"weather": "曇",
"series_number": 8,
"temperature": 16.6,
"away_score": 1,
"away_start_member": "清水　圭介,阿部　巧,武田　英二郎,堤　俊輔,イ　グァンソン,三島　勇太,中原　秀人,森村　昂太,城後　寿,坂田　大輔,平井　将生",
"home_score": 1,
"home_shoot": 11,
"game_id": "16059",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/04/20 16:02",
"referee": "窪田　陽輔"
},
{
"teams": [
"湘南ベルマーレ",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,菊地　俊介,永木　亮太,菊池　大介,大槻　周平,ウェリントン,岡田　翔平",
"away_shoot": 12,
"home_director": "曺　貴裁",
"away_team": "大分トリニータ",
"weather": "曇",
"series_number": 8,
"temperature": 11.6,
"away_score": 0,
"away_start_member": "武田　洋平,岩武　克弥,阪田　章裕,高木　和道,チェ　ジョンハン,末吉　隼也,伊藤　大介,為田　大貴,松本　怜,松本　昌也,伊佐　耕平",
"home_score": 4,
"home_shoot": 23,
"game_id": "16057",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/04/20 16:04",
"referee": "飯田　淳平"
},
{
"teams": [
"ジュビロ磐田",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "八田　直樹,駒野　友一,伊野波　雅彦,木下　高彰,藤田　義明,フェルジナンド,松井　大輔,山田　大記,小林　祐希,ポポ,前田　遼一",
"away_shoot": 8,
"home_director": "シャムスカ",
"away_team": "横浜ＦＣ",
"weather": "雨",
"series_number": 8,
"temperature": 12.1,
"away_score": 2,
"away_start_member": "南　雄太,市村　篤司,ドウグラス,野上　結貴,永田　拓也,寺田　紳一,安　英学,野村　直輝,内田　智也,黒津　勝,飯尾　一慶",
"home_score": 2,
"home_shoot": 11,
"game_id": "16058",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/04/20 16:05",
"referee": "吉田　寿光"
},
{
"teams": [
"モンテディオ山形",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "清水　健太,山田　拓巳,西河　翔吾,イ　ジュヨン,石川　竜也,宮阪　政樹,ディエゴ,秋葉　勝,中島　裕希,川西　翔太,ロメロ　フランク",
"away_shoot": 9,
"home_director": "石﨑　信弘",
"away_team": "ロアッソ熊本",
"weather": "晴",
"series_number": 8,
"temperature": 12.1,
"away_score": 2,
"away_start_member": "金井　大樹,藏川　洋平,園田　拓也,矢野　大輔,片山　奨典,橋本　拳人,養父　雄仁,仲間　隼斗,齊藤　和樹,岡本　賢明,澤田　崇",
"home_score": 1,
"home_shoot": 14,
"game_id": "16060",
"home_team": "モンテディオ山形",
"game_start_at": "2014/04/20 17:04",
"referee": "井上　知大"
},
{
"teams": [
"水戸ホーリーホック",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "本間　幸司,新里　亮,冨田　大介,尾本　敬,広瀬　陸斗,小澤　司,中里　崇宏,内田　航平,船谷　圭祐,吉田　眞紀人,三島　康平",
"away_shoot": 10,
"home_director": "柱谷　哲二",
"away_team": "東京ヴェルディ",
"weather": "曇",
"series_number": 8,
"temperature": 11.6,
"away_score": 1,
"away_start_member": "佐藤　優也,金　鐘必,吉野　恭平,井林　章,安在　和樹,田村　直也,鈴木　惇,常盤　聡,前田　直輝,中後　雅喜,平本　一樹",
"home_score": 1,
"home_shoot": 5,
"game_id": "16061",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/04/20 18:03",
"referee": "小屋　幸栄"
},
{
"teams": [
"ファジアーノ岡山",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "中林　洋次,後藤　圭太,鎌田　翔雅,田所　諒,久木田　紳吾,千明　聖典,上田　康太,染矢　一樹,林　容平,荒田　智之,久保　裕一",
"away_shoot": 14,
"home_director": "影山　雅永",
"away_team": "ギラヴァンツ北九州",
"weather": "曇",
"series_number": 8,
"temperature": 14.4,
"away_score": 3,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,鈴木　修人,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"home_score": 0,
"home_shoot": 13,
"game_id": "16062",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/04/20 19:03",
"referee": "池内　明彦"
},
{
"teams": [
"柏レイソル",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "菅野　孝憲,鈴木　大輔,近藤　直也,渡部　博文,橋本　和,高山　薫,ハン　グギョン,大谷　秀和,太田　徹郎,田中　順也,工藤　壮人",
"away_shoot": 10,
"home_director": "ネルシーニョ",
"away_team": "浦和レッズ",
"weather": "晴時々曇",
"series_number": 9,
"temperature": 23.1,
"away_score": 2,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,濱田　水輝,梅崎　司,柏木　陽介,阿部　勇樹,宇賀神　友弥,原口　元気,興梠　慎三,李　忠成",
"home_score": 3,
"home_shoot": 12,
"game_id": "15741",
"home_team": "柏レイソル",
"game_start_at": "2014/04/26 13:03",
"referee": "吉田　寿光"
},
{
"teams": [
"栃木ＳＣ",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "榎本　達也,山形　辰徳,チャ　ヨンファン,ドゥドゥ,イ　ミンス,湯澤　洋介,岡根　直哉,小野寺　達也,近藤　祐介,廣瀬　浩二,瀬沼　優司",
"away_shoot": 16,
"home_director": "阪倉　裕二",
"away_team": "水戸ホーリーホック",
"weather": "晴",
"series_number": 9,
"temperature": 23.3,
"away_score": 1,
"away_start_member": "本間　幸司,新里　亮,冨田　大介,尾本　敬,内田　航平,中里　崇宏,広瀬　陸斗,小澤　司,船谷　圭祐,馬場　賢治,三島　康平",
"home_score": 0,
"home_shoot": 10,
"game_id": "16063",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/04/26 13:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"東京ヴェルディ",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "佐藤　優也,安西　幸輝,金　鐘必,井林　章,安在　和樹,田村　直也,鈴木　惇,前田　直輝,中後　雅喜,常盤　聡,平本　一樹",
"away_shoot": 13,
"home_director": "三浦　泰年",
"away_team": "ジュビロ磐田",
"weather": "晴",
"series_number": 9,
"temperature": 24.4,
"away_score": 1,
"away_start_member": "八田　直樹,駒野　友一,伊野波　雅彦,櫻内　渚,藤田　義明,小林　祐希,フェルジナンド,山田　大記,松井　大輔,ポポ,前田　遼一",
"home_score": 0,
"home_shoot": 8,
"game_id": "16065",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/04/26 13:03",
"referee": "榎本　一慶"
},
{
"teams": [
"ザスパクサツ群馬",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "内藤　圭佑,小柳　達司,クォン　ハンジン,黄　誠秀,青木　孝太,坂井　洋平,夛田　凌輔,瀬川　和樹,ダニエル　ロビーニョ,永田　亮太,小林　竜樹",
"away_shoot": 15,
"home_director": "秋葉　忠宏",
"away_team": "アビスパ福岡",
"weather": "晴",
"series_number": 9,
"temperature": 24.2,
"away_score": 2,
"away_start_member": "清水　圭介,阿部　巧,三島　勇太,堤　俊輔,イ　グァンソン,中原　秀人,パク　ゴン,城後　寿,平井　将生,プノセバッチ,坂田　大輔",
"home_score": 1,
"home_shoot": 18,
"game_id": "16064",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/04/26 13:04",
"referee": "森川　浩次"
},
{
"teams": [
"松本山雅ＦＣ",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "村山　智彦,犬飼　智也,飯田　真輝,飯尾　和也,田中　隼磨,岩沼　俊介,岩間　雄大,岩上　祐三,喜山　康平,船山　貴之,塩沢　勝吾",
"away_shoot": 13,
"home_director": "反町　康治",
"away_team": "ＦＣ岐阜",
"weather": "晴",
"series_number": 9,
"temperature": 20.4,
"away_score": 0,
"away_start_member": "川口　能活,野垣内　俊,木谷　公亮,阿部　正紀,三都主　アレサンドロ,ヘニキ,宮沢　正史,太田　圭輔,髙地　系治,遠藤　純輝,ナザリト",
"home_score": 1,
"home_shoot": 12,
"game_id": "16066",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/04/26 13:04",
"referee": "高山　啓義"
},
{
"teams": [
"清水エスパルス",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "櫛引　政敏,吉田　豊,平岡　康裕,カルフィン　ヨン　ア　ピン,ヤコヴィッチ,竹内　涼,六平　光成,河井　陽介,大前　元紀,高木　俊幸,ノヴァコヴィッチ",
"away_shoot": 8,
"home_director": "アフシン　ゴトビ",
"away_team": "ベガルタ仙台",
"weather": "晴",
"series_number": 9,
"temperature": 19.3,
"away_score": 0,
"away_start_member": "関　憲太郎,菅井　直樹,渡辺　広大,石川　直樹,太田　吉彰,富田　晋伍,角田　誠,梁　勇基,佐々木　勇人,ウイルソン,赤嶺　真吾",
"home_score": 1,
"home_shoot": 3,
"game_id": "15743",
"home_team": "清水エスパルス",
"game_start_at": "2014/04/26 14:03",
"referee": "山本　雄大"
},
{
"teams": [
"横浜ＦＣ",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "南　雄太,野上　結貴,渡辺　匠,中島　崇典,永田　拓也,寺田　紳一,安　英学,小池　純輝,内田　智也,黒津　勝,飯尾　一慶",
"away_shoot": 15,
"home_director": "山口　素弘",
"away_team": "湘南ベルマーレ",
"weather": "晴",
"series_number": 9,
"temperature": 22.4,
"away_score": 3,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,亀川　諒史,菊地　俊介,永木　亮太,菊池　大介,大槻　周平,ウェリントン,岡田　翔平",
"home_score": 1,
"home_shoot": 6,
"game_id": "16067",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/04/26 14:03",
"referee": "三上　正一郎"
},
{
"teams": [
"横浜Ｆ・マリノス",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,富澤　清太郎,藤本　淳吾,中村　俊輔,齋藤　学,藤田　祥史",
"away_shoot": 5,
"home_director": "樋口　靖洋",
"away_team": "ＦＣ東京",
"weather": "晴",
"series_number": 9,
"temperature": 21.6,
"away_score": 1,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,東　慶悟,三田　啓貴,渡邉　千真,平山　相太",
"home_score": 0,
"home_shoot": 10,
"game_id": "15742",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/04/26 14:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"京都サンガF.C.",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,駒井　善成,ジャイロ,工藤　浩平,山瀬　功治,有田　光希,大黒　将志",
"away_shoot": 13,
"home_director": "バドゥ",
"away_team": "愛媛ＦＣ",
"weather": "晴",
"series_number": 9,
"temperature": 24.4,
"away_score": 0,
"away_start_member": "児玉　剛,三原　向平,村上　佑介,林堂　眞,西岡　大輝,キム　ミンジェ,村上　巧,吉村　圭司,渡辺　亮太,河原　和寿,表原　玄太",
"home_score": 0,
"home_shoot": 9,
"game_id": "16068",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/04/26 14:04",
"referee": "上田　益也"
},
{
"teams": [
"徳島ヴォルティス",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "長谷川　徹,藤原　広太朗,橋内　優也,福元　洋平,小暮　大器,濱田　武,斉藤　大介,クレイトン　ドミンゲス,大﨑　淳矢,ドウグラス,高崎　寛之",
"away_shoot": 8,
"home_director": "小林　伸二",
"away_team": "アルビレックス新潟",
"weather": "晴",
"series_number": 9,
"temperature": 19.6,
"away_score": 2,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,金　珍洙,レオ　シルバ,小泉　慶,成岡　翔,岡本　英也,鈴木　武蔵,川又　堅碁",
"home_score": 1,
"home_shoot": 8,
"game_id": "15744",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/04/26 14:05",
"referee": "今村　義朗"
},
{
"teams": [
"名古屋グランパス",
"サガン鳥栖"
],
"away_director": "尹　晶煥",
"home_start_member": "楢﨑　正剛,矢野　貴章,田中　マルクス闘莉王,ダニルソン,本多　勇喜,枝村　匠馬,田口　泰士,中村　直志,小川　佳純,松田　力,永井　謙佑",
"away_shoot": 17,
"home_director": "西野　朗",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 9,
"temperature": 21.8,
"away_score": 3,
"away_start_member": "林　彰洋,丹羽　竜平,キム　ミンヒョク,坂井　達弥,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 2,
"home_shoot": 14,
"game_id": "15745",
"home_team": "名古屋グランパス",
"game_start_at": "2014/04/26 15:04",
"referee": "飯田　淳平"
},
{
"teams": [
"ヴィッセル神戸",
"セレッソ大阪"
],
"away_director": "ランコ　ポポヴィッチ",
"home_start_member": "山本　海人,奥井　諒,岩波　拓也,増川　隆洋,高橋　峻希,橋本　英郎,チョン　ウヨン,小川　慶治朗,マルキーニョス,ペドロ　ジュニオール,森岡　亮太",
"away_shoot": 15,
"home_director": "安達　亮",
"away_team": "セレッソ大阪",
"weather": "晴",
"series_number": 9,
"temperature": 18.5,
"away_score": 2,
"away_start_member": "武田　博行,染谷　悠太,新井場　徹,山下　達也,ゴイコ　カチャル,扇原　貴宏,長谷川　アーリアジャスール,山口　蛍,丸橋　祐介,柿谷　曜一朗,フォルラン",
"home_score": 2,
"home_shoot": 12,
"game_id": "15746",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/04/26 15:04",
"referee": "松尾　一"
},
{
"teams": [
"ジェフユナイテッド千葉",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "岡本　昌弘,キム　ヒョヌン,大岩　一貴,山口　智,中村　太亮,兵働　昭弘,佐藤　勇人,谷澤　達也,井出　遥也,田中　佑昌,ケンペス",
"away_shoot": 8,
"home_director": "鈴木　淳",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 9,
"temperature": 18.4,
"away_score": 1,
"away_start_member": "森田　耕一郎,藤井　航大,武田　有祐,ソン　ハンキ,小澤　雄希,関原　凌河,岡村　和哉,山本　翔平,綱田　大志,西野　泰正,アンドレア",
"home_score": 1,
"home_shoot": 18,
"game_id": "16069",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/04/26 16:03",
"referee": "東城　穣"
},
{
"teams": [
"ギラヴァンツ北九州",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,鈴木　修人,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"away_shoot": 12,
"home_director": "柱谷　幸一",
"away_team": "モンテディオ山形",
"weather": "晴",
"series_number": 9,
"temperature": 20.8,
"away_score": 1,
"away_start_member": "清水　健太,山田　拓巳,イ　ジュヨン,西河　翔吾,石川　竜也,宮阪　政樹,ディエゴ,秋葉　勝,中島　裕希,川西　翔太,山﨑　雅人",
"home_score": 0,
"home_shoot": 11,
"game_id": "16070",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/04/26 16:03",
"referee": "扇谷　健司"
},
{
"teams": [
"大分トリニータ",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "武田　洋平,岩武　克弥,阪田　章裕,高木　和道,安川　有,末吉　隼也,伊藤　大介,為田　大貴,チェ　ジョンハン,松本　昌也,風間　宏矢",
"away_shoot": 9,
"home_director": "田坂　和昭",
"away_team": "カターレ富山",
"weather": "晴時々曇",
"series_number": 9,
"temperature": 22.3,
"away_score": 0,
"away_start_member": "水谷　雄一,木村　勝太,平出　涼,吉川　拓也,内田　健太,大西　容平,吉川　健太,ソ　ヨンドク,中島　翔哉,三上　陽輔,白崎　凌兵",
"home_score": 3,
"home_shoot": 15,
"game_id": "16071",
"home_team": "大分トリニータ",
"game_start_at": "2014/04/26 16:03",
"referee": "池内　明彦"
},
{
"teams": [
"川崎フロンターレ",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "西部　洋平,田中　裕介,ジェシ,中澤　聡太,谷口　彰悟,大島　僚太,中村　憲剛,森谷　賢太郎,レナト,小林　悠,大久保　嘉人",
"away_shoot": 9,
"home_director": "風間　八宏",
"away_team": "ガンバ大阪",
"weather": "晴",
"series_number": 9,
"temperature": 20.1,
"away_score": 1,
"away_start_member": "東口　順昭,オ　ジェソク,岩下　敬輔,丹羽　大輝,藤春　廣輝,内田　達也,今野　泰幸,阿部　浩之,倉田　秋,リンス,遠藤　保仁",
"home_score": 2,
"home_shoot": 17,
"game_id": "15747",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/04/26 16:04",
"referee": "廣瀬　格"
},
{
"teams": [
"大宮アルディージャ",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "江角　浩司,今井　智基,菊地　光将,高橋　祥平,渡部　大輔,橋本　晃司,横山　知伸,渡邉　大剛,曺　永哲,家長　昭博,ズラタン",
"away_shoot": 16,
"home_director": "大熊　清",
"away_team": "ヴァンフォーレ甲府",
"weather": "晴",
"series_number": 9,
"temperature": 19.7,
"away_score": 2,
"away_start_member": "岡　大生,青山　直晃,山本　英臣,佐々木　翔,福田　健介,新井　涼平,マルキーニョス　パラナ,阿部　翔平,河本　明人,盛田　剛平,クリスティアーノ",
"home_score": 0,
"home_shoot": 5,
"game_id": "15748",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/04/26 17:04",
"referee": "村上　伸次"
},
{
"teams": [
"ロアッソ熊本",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "シュミット　ダニエル,藏川　洋平,篠原　弘次郎,園田　拓也,片山　奨典,養父　雄仁,原田　拓,仲間　隼斗,齊藤　和樹,ファビオ,澤田　崇",
"away_shoot": 10,
"home_director": "小野　剛",
"away_team": "Ｖ・ファーレン長崎",
"weather": "曇",
"series_number": 9,
"temperature": 22.5,
"away_score": 1,
"away_start_member": "大久保　択生,岡本　拓也,山口　貴弘,古部　健太,神崎　大輔,三原　雅俊,黒木　聖仁,野田　紘史,奥埜　博亮,東　浩史,佐藤　洸一",
"home_score": 1,
"home_shoot": 7,
"game_id": "16072",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/04/26 17:04",
"referee": "岡部　拓人"
},
{
"teams": [
"ファジアーノ岡山",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "中林　洋次,鎌田　翔雅,後藤　圭太,田所　諒,久木田　紳吾,島田　譲,上田　康太,染矢　一樹,石原　崇兆,林　容平,久保　裕一",
"away_shoot": 15,
"home_director": "影山　雅永",
"away_team": "コンサドーレ札幌",
"weather": "曇",
"series_number": 9,
"temperature": 18.9,
"away_score": 0,
"away_start_member": "李　昊乗,日高　拓磨,パウロン,奈良　竜樹,松本　怜大,河合　竜二,宮澤　裕樹,古田　寛幸,前田　俊介,菊岡　拓朗,都倉　賢",
"home_score": 2,
"home_shoot": 15,
"game_id": "16073",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/04/26 19:03",
"referee": "前田　拓哉"
},
{
"teams": [
"サンフレッチェ広島",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,柏　好文,青山　敏弘,森﨑　和幸,清水　航平,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"away_shoot": 10,
"home_director": "森保　一",
"away_team": "鹿島アントラーズ",
"weather": "晴",
"series_number": 9,
"temperature": 15.1,
"away_score": 3,
"away_start_member": "曽ヶ端　準,伊東　幸敏,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,ダヴィ",
"home_score": 0,
"home_shoot": 10,
"game_id": "15749",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/04/26 19:04",
"referee": "西村　雄一"
},
{
"teams": [
"ＦＣ東京",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,三田　啓貴,渡邉　千真,平山　相太,東　慶悟",
"away_shoot": 6,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "名古屋グランパス",
"weather": "曇",
"series_number": 10,
"temperature": 19.8,
"away_score": 1,
"away_start_member": "楢﨑　正剛,矢野　貴章,大武　峻,田中　マルクス闘莉王,本多　勇喜,枝村　匠馬,田口　泰士,中村　直志,小川　佳純,玉田　圭司,永井　謙佑",
"home_score": 0,
"home_shoot": 9,
"game_id": "15750",
"home_team": "ＦＣ東京",
"game_start_at": "2014/04/29 13:04",
"referee": "村上　伸次"
},
{
"teams": [
"ヴァンフォーレ甲府",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "岡　大生,青山　直晃,山本　英臣,佐々木　翔,福田　健介,新井　涼平,マルキーニョス　パラナ,阿部　翔平,河本　明人,盛田　剛平,クリスティアーノ",
"away_shoot": 2,
"home_director": "城福　浩",
"away_team": "徳島ヴォルティス",
"weather": "曇",
"series_number": 10,
"temperature": 18.6,
"away_score": 1,
"away_start_member": "長谷川　徹,藤原　広太朗,橋内　優也,斉藤　大介,福元　洋平,濱田　武,小島　秀仁,クレイトン　ドミンゲス,大﨑　淳矢,津田　知宏,高崎　寛之",
"home_score": 0,
"home_shoot": 19,
"game_id": "15751",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/04/29 13:04",
"referee": "東城　穣"
},
{
"teams": [
"ＦＣ岐阜",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "川口　能活,杉山　新,阿部　正紀,関田　寛士,野垣内　俊,ヘニキ,水野　泰輔,太田　圭輔,髙地　系治,難波　宏明,遠藤　純輝",
"away_shoot": 6,
"home_director": "ラモス　瑠偉",
"away_team": "ザスパクサツ群馬",
"weather": "雨",
"series_number": 10,
"temperature": 17.3,
"away_score": 0,
"away_start_member": "内藤　圭佑,小柳　達司,青木　良太,クォン　ハンジン,乾　大知,瀬川　和樹,加藤　弘堅,宮崎　泰右,横山　翔平,小林　竜樹,永田　亮太",
"home_score": 1,
"home_shoot": 9,
"game_id": "16074",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/04/29 13:04",
"referee": "長谷　拓"
},
{
"teams": [
"カマタマーレ讃岐",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "森田　耕一郎,武田　有祐,藤井　航大,ソン　ハンキ,小澤　雄希,高木　和正,岡村　和哉,綱田　大志,関原　凌河,アンドレア,高橋　泰",
"away_shoot": 8,
"home_director": "北野　誠",
"away_team": "横浜ＦＣ",
"weather": "曇",
"series_number": 10,
"temperature": 24.2,
"away_score": 1,
"away_start_member": "南　雄太,市村　篤司,ドウグラス,野上　結貴,永田　拓也,寺田　紳一,安　英学,小池　純輝,内田　智也,黒津　勝,飯尾　一慶",
"home_score": 0,
"home_shoot": 4,
"game_id": "16075",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/04/29 13:04",
"referee": "池内　明彦"
},
{
"teams": [
"アビスパ福岡",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "清水　圭介,阿部　巧,堤　俊輔,イ　グァンソン,三島　勇太,中原　秀人,森村　昂太,坂田　大輔,平井　将生,城後　寿,石津　大介",
"away_shoot": 10,
"home_director": "マリヤン　プシュニク",
"away_team": "ギラヴァンツ北九州",
"weather": "曇",
"series_number": 10,
"temperature": 18.4,
"away_score": 1,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,風間　宏希,八角　剛史,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"home_score": 0,
"home_shoot": 9,
"game_id": "16076",
"home_team": "アビスパ福岡",
"game_start_at": "2014/04/29 13:04",
"referee": "松尾　一"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "大久保　択生,岡本　拓也,山口　貴弘,野田　紘史,古部　健太,三原　雅俊,黒木　聖仁,山田　晃平,奥埜　博亮,佐藤　洸一,イ　デホン",
"away_shoot": 4,
"home_director": "高木　琢也",
"away_team": "大分トリニータ",
"weather": "曇",
"series_number": 10,
"temperature": 18.8,
"away_score": 0,
"away_start_member": "武田　洋平,岩武　克弥,若狭　大志,高木　和道,安川　有,末吉　隼也,伊藤　大介,為田　大貴,松本　怜,風間　宏矢,田中　輝希",
"home_score": 0,
"home_shoot": 9,
"game_id": "16077",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/04/29 13:04",
"referee": "福島　孝一郎"
},
{
"teams": [
"サガン鳥栖",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "林　彰洋,丹羽　竜平,キム　ミンヒョク,坂井　達弥,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 11,
"home_director": "尹　晶煥",
"away_team": "サンフレッチェ広島",
"weather": "曇",
"series_number": 10,
"temperature": 18,
"away_score": 2,
"away_start_member": "林　卓人,ファン　ソッコ,塩谷　司,水本　裕貴,柏　好文,青山　敏弘,柴﨑　晃誠,山岸　智,森﨑　浩司,野津田　岳人,石原　直樹",
"home_score": 1,
"home_shoot": 6,
"game_id": "15753",
"home_team": "サガン鳥栖",
"game_start_at": "2014/04/29 14:00",
"referee": "岡部　拓人"
},
{
"teams": [
"アルビレックス新潟",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "守田　達弥,大野　和成,舞行龍ジェームズ,大井　健太郎,金　珍洙,レオ　シルバ,成岡　翔,田中　亜土夢,岡本　英也,鈴木　武蔵,川又　堅碁",
"away_shoot": 5,
"home_director": "柳下　正明",
"away_team": "ヴィッセル神戸",
"weather": "晴のち曇",
"series_number": 10,
"temperature": 21.4,
"away_score": 1,
"away_start_member": "山本　海人,奥井　諒,岩波　拓也,増川　隆洋,高橋　峻希,森岡　亮太,チョン　ウヨン,ペドロ　ジュニオール,橋本　英郎,マルキーニョス,小川　慶治朗",
"home_score": 1,
"home_shoot": 9,
"game_id": "15752",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/04/29 14:02",
"referee": "窪田　陽輔"
},
{
"teams": [
"愛媛ＦＣ",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "児玉　剛,三原　向平,村上　佑介,林堂　眞,西岡　大輝,キム　ミンジェ,村上　巧,吉村　圭司,原川　力,渡辺　亮太,河原　和寿",
"away_shoot": 11,
"home_director": "石丸　清隆",
"away_team": "栃木ＳＣ",
"weather": "曇",
"series_number": 10,
"temperature": 20.1,
"away_score": 1,
"away_start_member": "榎本　達也,山形　辰徳,チャ　ヨンファン,ドゥドゥ,赤井　秀行,廣瀬　浩二,小野寺　達也,岡根　直哉,近藤　祐介,重松　健太郎,瀬沼　優司",
"home_score": 0,
"home_shoot": 10,
"game_id": "16079",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/04/29 14:03",
"referee": "井上　知大"
},
{
"teams": [
"カターレ富山",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "飯田　健巳,高　准翼,御厨　貴文,吉川　拓也,木村　勝太,ソ　ヨンドク,秋本　倫孝,大西　容平,中島　翔哉,白崎　凌兵,苔口　卓也",
"away_shoot": 18,
"home_director": "安間　貴義",
"away_team": "松本山雅ＦＣ",
"weather": "曇一時雨",
"series_number": 10,
"temperature": 20.1,
"away_score": 2,
"away_start_member": "村山　智彦,田中　隼磨,飯尾　和也,飯田　真輝,犬飼　智也,岩沼　俊介,岩間　雄大,喜山　康平,塩沢　勝吾,船山　貴之,岩上　祐三",
"home_score": 3,
"home_shoot": 11,
"game_id": "16078",
"home_team": "カターレ富山",
"game_start_at": "2014/04/29 14:04",
"referee": "飯田　淳平"
},
{
"teams": [
"鹿島アントラーズ",
"清水エスパルス"
],
"away_director": "アフシン　ゴトビ",
"home_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,ダヴィ",
"away_shoot": 12,
"home_director": "トニーニョ　セレーゾ",
"away_team": "清水エスパルス",
"weather": "曇",
"series_number": 10,
"temperature": 16.5,
"away_score": 1,
"away_start_member": "櫛引　政敏,吉田　豊,ヤコヴィッチ,平岡　康裕,カルフィン　ヨン　ア　ピン,村松　大輔,竹内　涼,六平　光成,河井　陽介,大前　元紀,ノヴァコヴィッチ",
"home_score": 2,
"home_shoot": 19,
"game_id": "15754",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/04/29 15:03",
"referee": "家本　政明"
},
{
"teams": [
"ベガルタ仙台",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "関　憲太郎,菅井　直樹,渡辺　広大,角田　誠,石川　直樹,太田　吉彰,富田　晋伍,武井　択也,梁　勇基,武藤　雄樹,赤嶺　真吾",
"away_shoot": 10,
"home_director": "渡邉　晋",
"away_team": "川崎フロンターレ",
"weather": "曇",
"series_number": 10,
"temperature": 11.9,
"away_score": 0,
"away_start_member": "西部　洋平,田中　裕介,ジェシ,中澤　聡太,谷口　彰悟,大島　僚太,中村　憲剛,森谷　賢太郎,レナト,小林　悠,大久保　嘉人",
"home_score": 0,
"home_shoot": 10,
"game_id": "15755",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/04/29 16:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"浦和レッズ",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "西川　周作,森脇　良太,永田　充,那須　大亮,平川　忠亮,柏木　陽介,阿部　勇樹,宇賀神　友弥,原口　元気,興梠　慎三,李　忠成",
"away_shoot": 8,
"home_director": "ペトロヴィッチ",
"away_team": "横浜Ｆ・マリノス",
"weather": "曇",
"series_number": 10,
"temperature": 19.1,
"away_score": 0,
"away_start_member": "榎本　哲也,奈良輪　雄太,栗原　勇蔵,中澤　佑二,ドゥトラ,三門　雄大,小椋　祥平,藤本　淳吾,中村　俊輔,兵藤　慎剛,藤田　祥史",
"home_score": 1,
"home_shoot": 10,
"game_id": "15756",
"home_team": "浦和レッズ",
"game_start_at": "2014/04/29 16:04",
"referee": "扇谷　健司"
},
{
"teams": [
"ガンバ大阪",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "東口　順昭,今野　泰幸,岩下　敬輔,丹羽　大輝,藤春　廣輝,内田　達也,遠藤　保仁,阿部　浩之,二川　孝広,リンス,倉田　秋",
"away_shoot": 9,
"home_director": "長谷川　健太",
"away_team": "柏レイソル",
"weather": "曇のち雨",
"series_number": 10,
"temperature": 16.8,
"away_score": 2,
"away_start_member": "菅野　孝憲,鈴木　大輔,近藤　直也,渡部　博文,橋本　和,高山　薫,茨田　陽生,大谷　秀和,太田　徹郎,田中　順也,工藤　壮人",
"home_score": 1,
"home_shoot": 8,
"game_id": "15757",
"home_team": "ガンバ大阪",
"game_start_at": "2014/04/29 16:04",
"referee": "高山　啓義"
},
{
"teams": [
"モンテディオ山形",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "清水　健太,山田　拓巳,西河　翔吾,イ　ジュヨン,石川　竜也,宮阪　政樹,ディエゴ,秋葉　勝,中島　裕希,川西　翔太,山﨑　雅人",
"away_shoot": 9,
"home_director": "石﨑　信弘",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 10,
"temperature": 17.4,
"away_score": 2,
"away_start_member": "中林　洋次,鎌田　翔雅,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,妹尾　隆佑,片山　瑛一,清水　慎太郎",
"home_score": 0,
"home_shoot": 14,
"game_id": "16080",
"home_team": "モンテディオ山形",
"game_start_at": "2014/04/29 16:04",
"referee": "小屋　幸栄"
},
{
"teams": [
"ジュビロ磐田",
"ジェフユナイテッド千葉"
],
"away_director": "鈴木　淳",
"home_start_member": "八田　直樹,駒野　友一,藤田　義明,伊野波　雅彦,櫻内　渚,フェルジナンド,小林　祐希,松井　大輔,山田　大記,ポポ,前田　遼一",
"away_shoot": 11,
"home_director": "シャムスカ",
"away_team": "ジェフユナイテッド千葉",
"weather": "雨",
"series_number": 10,
"temperature": 15.5,
"away_score": 0,
"away_start_member": "岡本　昌弘,キム　ヒョヌン,大岩　一貴,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,田中　佑昌,谷澤　達也,森本　貴幸,ケンペス",
"home_score": 2,
"home_shoot": 13,
"game_id": "16081",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/04/29 16:04",
"referee": "西村　雄一"
},
{
"teams": [
"コンサドーレ札幌",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "金山　隼樹,小山内　貴哉,櫛引　一紀,奈良　竜樹,日高　拓磨,河合　竜二,宮澤　裕樹,砂川　誠,古田　寛幸,榊　翔太,前田　俊介",
"away_shoot": 6,
"home_director": "財前　恵一",
"away_team": "東京ヴェルディ",
"weather": "屋内",
"series_number": 10,
"temperature": 22.9,
"away_score": 0,
"away_start_member": "佐藤　優也,森　勇介,金　鐘必,井林　章,安在　和樹,田村　直也,鈴木　惇,前田　直輝,中後　雅喜,常盤　聡,平本　一樹",
"home_score": 0,
"home_shoot": 11,
"game_id": "16082",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/04/29 17:03",
"referee": "岡　宏道"
},
{
"teams": [
"水戸ホーリーホック",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "本間　幸司,新里　亮,冨田　大介,尾本　敬,中里　崇宏,内田　航平,広瀬　陸斗,小澤　司,小谷野　顕治,馬場　賢治,鈴木　隆行",
"away_shoot": 7,
"home_director": "柱谷　哲二",
"away_team": "ロアッソ熊本",
"weather": "曇",
"series_number": 10,
"temperature": 14.3,
"away_score": 0,
"away_start_member": "シュミット　ダニエル,園田　拓也,篠原　弘次郎,矢野　大輔,藏川　洋平,吉井　孝輔,養父　雄仁,中山　雄登,齊藤　和樹,仲間　隼斗,澤田　崇",
"home_score": 0,
"home_shoot": 13,
"game_id": "16083",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/04/29 17:03",
"referee": "塚田　健太"
},
{
"teams": [
"セレッソ大阪",
"大宮アルディージャ"
],
"away_director": "大熊　清",
"home_start_member": "武田　博行,染谷　悠太,藤本　康太,酒本　憲幸,山下　達也,扇原　貴宏,長谷川　アーリアジャスール,山口　蛍,丸橋　祐介,柿谷　曜一朗,フォルラン",
"away_shoot": 7,
"home_director": "ランコ　ポポヴィッチ",
"away_team": "大宮アルディージャ",
"weather": "雨",
"series_number": 10,
"temperature": 17.3,
"away_score": 1,
"away_start_member": "江角　浩司,今井　智基,菊地　光将,高橋　祥平,渡部　大輔,中村　北斗,増田　誓志,片岡　洋介,家長　昭博,富山　貴光,ズラタン",
"home_score": 1,
"home_shoot": 14,
"game_id": "15758",
"home_team": "セレッソ大阪",
"game_start_at": "2014/04/29 19:04",
"referee": "吉田　寿光"
},
{
"teams": [
"湘南ベルマーレ",
"京都サンガF.C."
],
"away_director": "バドゥ",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,菊地　俊介,永木　亮太,菊池　大介,大槻　周平,ウェリントン,武富　孝介",
"away_shoot": 12,
"home_director": "曺　貴裁",
"away_team": "京都サンガF.C.",
"weather": "雨",
"series_number": 10,
"temperature": 16.7,
"away_score": 0,
"away_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,駒井　善成,ジャイロ,工藤　浩平,横谷　繁,有田　光希,大黒　将志",
"home_score": 3,
"home_shoot": 10,
"game_id": "16084",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/04/29 19:04",
"referee": "山本　雄大"
},
{
"teams": [
"栃木ＳＣ",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "榎本　達也,山形　辰徳,チャ　ヨンファン,ドゥドゥ,赤井　秀行,湯澤　洋介,菅　和範,小野寺　達也,近藤　祐介,重松　健太郎,瀬沼　優司",
"away_shoot": 5,
"home_director": "阪倉　裕二",
"away_team": "コンサドーレ札幌",
"weather": "晴",
"series_number": 11,
"temperature": 26,
"away_score": 1,
"away_start_member": "李　昊乗,小山内　貴哉,櫛引　一紀,奈良　竜樹,日高　拓磨,河合　竜二,宮澤　裕樹,菊岡　拓朗,ヘナン,榊　翔太,石井　謙伍",
"home_score": 2,
"home_shoot": 8,
"game_id": "16085",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/05/03 13:03",
"referee": "三上　正一郎"
},
{
"teams": [
"松本山雅ＦＣ",
"愛媛ＦＣ"
],
"away_director": "56' 退席 愛媛 平井　直人 （ＧＫコーチ）",
"home_start_member": "村山　智彦,多々良　敦斗,飯田　真輝,犬飼　智也,田中　隼磨,岩間　雄大,岩沼　俊介,岩上　祐三,喜山　康平,サビア,船山　貴之",
"away_shoot": 11,
"home_director": "石丸　清隆",
"away_team": "愛媛ＦＣ",
"weather": "晴",
"series_number": 11,
"temperature": 22.4,
"away_score": 1,
"away_start_member": "児玉　剛,ハン　ヒフン,村上　佑介,林堂　眞,浦田　延尚,キム　ミンジェ,村上　巧,原川　力,堀米　勇輝,渡辺　亮太,表原　玄太",
"home_score": 2,
"home_shoot": 13,
"game_id": "16086",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/05/03 13:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"アビスパ福岡",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "清水　圭介,阿部　巧,三島　勇太,パク　ゴン,堤　俊輔,中原　秀人,武田　英二郎,石津　大介,酒井　宣福,城後　寿,坂田　大輔",
"away_shoot": 11,
"home_director": "マリヤン　プシュニク",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 11,
"temperature": 21.4,
"away_score": 2,
"away_start_member": "武田　洋平,岩武　克弥,阪田　章裕,高木　和道,安川　有,末吉　隼也,松本　昌也,木村　祐志,西　弘則,風間　宏矢,田中　輝希",
"home_score": 1,
"home_shoot": 4,
"game_id": "16087",
"home_team": "アビスパ福岡",
"game_start_at": "2014/05/03 13:03",
"referee": "村上　伸次"
},
{
"teams": [
"柏レイソル",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "菅野　孝憲,鈴木　大輔,近藤　直也,渡部　博文,橋本　和,高山　薫,大谷　秀和,茨田　陽生,太田　徹郎,田中　順也,工藤　壮人",
"away_shoot": 14,
"home_director": "ネルシーニョ",
"away_team": "鹿島アントラーズ",
"weather": "晴",
"series_number": 11,
"temperature": 25.3,
"away_score": 0,
"away_start_member": "曽ヶ端　準,伊東　幸敏,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,ダヴィ",
"home_score": 1,
"home_shoot": 6,
"game_id": "15761",
"home_team": "柏レイソル",
"game_start_at": "2014/05/03 13:04",
"referee": "東城　穣"
},
{
"teams": [
"東京ヴェルディ",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "佐藤　優也,安西　幸輝,金　鐘必,井林　章,安在　和樹,田村　直也,吉野　恭平,中後　雅喜,鈴木　惇,常盤　聡,平本　一樹",
"away_shoot": 6,
"home_director": "三浦　泰年",
"away_team": "ＦＣ岐阜",
"weather": "晴",
"series_number": 11,
"temperature": 26.7,
"away_score": 1,
"away_start_member": "川口　能活,野垣内　俊,阿部　正紀,関田　寛士,三都主　アレサンドロ,ヘニキ,宮沢　正史,太田　圭輔,髙地　系治,難波　宏明,ナザリト",
"home_score": 0,
"home_shoot": 6,
"game_id": "16089",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/05/03 14:03",
"referee": "上田　益也"
},
{
"teams": [
"ギラヴァンツ北九州",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"away_shoot": 8,
"home_director": "柱谷　幸一",
"away_team": "横浜ＦＣ",
"weather": "晴",
"series_number": 11,
"temperature": 19.4,
"away_score": 1,
"away_start_member": "南　雄太,市村　篤司,ドウグラス,野上　結貴,永田　拓也,寺田　紳一,安　英学,小池　純輝,野村　直輝,黒津　勝,内田　智也",
"home_score": 2,
"home_shoot": 6,
"game_id": "16090",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/05/03 14:03",
"referee": "榎本　一慶"
},
{
"teams": [
"横浜Ｆ・マリノス",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,三門　雄大,小椋　祥平,中村　俊輔,藤本　淳吾,藤田　祥史,伊藤　翔",
"away_shoot": 14,
"home_director": "樋口　靖洋",
"away_team": "ガンバ大阪",
"weather": "晴",
"series_number": 11,
"temperature": 26.8,
"away_score": 0,
"away_start_member": "東口　順昭,オ　ジェソク,岩下　敬輔,丹羽　大輝,藤春　廣輝,内田　達也,遠藤　保仁,阿部　浩之,大森　晃太郎,佐藤　晃大,リンス",
"home_score": 2,
"home_shoot": 9,
"game_id": "15763",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/05/03 14:04",
"referee": "前田　拓哉"
},
{
"teams": [
"徳島ヴォルティス",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "長谷川　徹,藤原　広太朗,橋内　優也,福元　洋平,李　栄直,濱田　武,斉藤　大介,宮崎　光平,大﨑　淳矢,津田　知宏,高崎　寛之",
"away_shoot": 11,
"home_director": "小林　伸二",
"away_team": "ベガルタ仙台",
"weather": "晴",
"series_number": 11,
"temperature": 24,
"away_score": 1,
"away_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,角田　誠,石川　直樹,富田　晋伍,武井　択也,太田　吉彰,梁　勇基,武藤　雄樹,赤嶺　真吾",
"home_score": 0,
"home_shoot": 7,
"game_id": "15767",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/05/03 14:04",
"referee": "松尾　一"
},
{
"teams": [
"モンテディオ山形",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "清水　健太,山田　拓巳,西河　翔吾,イ　ジュヨン,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,中島　裕希,川西　翔太,秋葉　勝",
"away_shoot": 6,
"home_director": "石﨑　信弘",
"away_team": "カターレ富山",
"weather": "晴のち曇",
"series_number": 11,
"temperature": 23.7,
"away_score": 0,
"away_start_member": "飯田　健巳,木村　勝太,御厨　貴文,吉川　拓也,内田　健太,三上　陽輔,大西　容平,キム　ヨングン,中島　翔哉,白崎　凌兵,苔口　卓也",
"home_score": 1,
"home_shoot": 16,
"game_id": "16088",
"home_team": "モンテディオ山形",
"game_start_at": "2014/05/03 14:04",
"referee": "岡　宏道"
},
{
"teams": [
"川崎フロンターレ",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "西部　洋平,田中　裕介,ジェシ,井川　祐輔,谷口　彰悟,山本　真希,大島　僚太,森谷　賢太郎,レナト,小林　悠,大久保　嘉人",
"away_shoot": 12,
"home_director": "風間　八宏",
"away_team": "ヴァンフォーレ甲府",
"weather": "晴時々曇",
"series_number": 11,
"temperature": 26,
"away_score": 0,
"away_start_member": "岡　大生,青山　直晃,山本　英臣,佐々木　翔,松橋　優,新井　涼平,稲垣　祥,阿部　翔平,石原　克哉,下田　北斗,クリスティアーノ",
"home_score": 2,
"home_shoot": 7,
"game_id": "15762",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/05/03 15:03",
"referee": "飯田　淳平"
},
{
"teams": [
"清水エスパルス",
"サガン鳥栖"
],
"away_director": "尹　晶煥",
"home_start_member": "櫛引　政敏,ヤコヴィッチ,平岡　康裕,カルフィン　ヨン　ア　ピン,吉田　豊,村松　大輔,竹内　涼,六平　光成,河井　陽介,大前　元紀,ノヴァコヴィッチ",
"away_shoot": 10,
"home_director": "アフシン　ゴトビ",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 11,
"temperature": 23.4,
"away_score": 1,
"away_start_member": "林　彰洋,丹羽　竜平,キム　ミンヒョク,呂　成海,金　民友,水沼　宏太,高橋　義希,藤田　直之,早坂　良太,池田　圭,豊田　陽平",
"home_score": 0,
"home_shoot": 5,
"game_id": "15764",
"home_team": "清水エスパルス",
"game_start_at": "2014/05/03 15:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"ヴィッセル神戸",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "山本　海人,茂木　弘人,岩波　拓也,河本　裕之,高橋　峻希,橋本　英郎,森岡　亮太,チョン　ウヨン,ペドロ　ジュニオール,小川　慶治朗,マルキーニョス",
"away_shoot": 11,
"home_director": "安達　亮",
"away_team": "サンフレッチェ広島",
"weather": "晴",
"series_number": 11,
"temperature": 23.4,
"away_score": 0,
"away_start_member": "林　卓人,ファン　ソッコ,千葉　和彦,水本　裕貴,清水　航平,柴﨑　晃誠,森﨑　和幸,パク　ヒョンジン,森﨑　浩司,髙萩　洋次郎,佐藤　寿人",
"home_score": 0,
"home_shoot": 12,
"game_id": "15766",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/05/03 15:04",
"referee": "家本　政明"
},
{
"teams": [
"水戸ホーリーホック",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "本間　幸司,新里　亮,冨田　大介,尾本　敬,内田　航平,中里　崇宏,広瀬　陸斗,小澤　司,船谷　圭祐,三島　康平,鈴木　隆行",
"away_shoot": 11,
"home_director": "柱谷　哲二",
"away_team": "湘南ベルマーレ",
"weather": "晴",
"series_number": 11,
"temperature": 25.1,
"away_score": 1,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,宇佐美　宏和,菊地　俊介,永木　亮太,菊池　大介,岡田　翔平,大槻　周平,武富　孝介",
"home_score": 0,
"home_shoot": 12,
"game_id": "16091",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/05/03 16:03",
"referee": "窪田　陽輔"
},
{
"teams": [
"ジェフユナイテッド千葉",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "岡本　昌弘,キム　ヒョヌン,大岩　一貴,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,田中　佑昌,谷澤　達也,森本　貴幸,ケンペス",
"away_shoot": 12,
"home_director": "鈴木　淳",
"away_team": "ザスパクサツ群馬",
"weather": "晴",
"series_number": 11,
"temperature": 23.8,
"away_score": 2,
"away_start_member": "内藤　圭佑,小柳　達司,クォン　ハンジン,夛田　凌輔,瀬川　和樹,青木　孝太,坂井　洋平,黄　誠秀,小林　竜樹,ダニエル　ロビーニョ,永田　亮太",
"home_score": 3,
"home_shoot": 16,
"game_id": "16092",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/05/03 16:03",
"referee": "吉田　寿光"
},
{
"teams": [
"浦和レッズ",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "西川　周作,森脇　良太,永田　充,那須　大亮,梅崎　司,柏木　陽介,阿部　勇樹,宇賀神　友弥,原口　元気,興梠　慎三,李　忠成",
"away_shoot": 13,
"home_director": "ペトロヴィッチ",
"away_team": "ＦＣ東京",
"weather": "晴",
"series_number": 11,
"temperature": 25.6,
"away_score": 0,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,加賀　健一,太田　宏介,高橋　秀人,米本　拓司,東　慶悟,渡邉　千真,平山　相太,武藤　嘉紀",
"home_score": 1,
"home_shoot": 9,
"game_id": "15759",
"home_team": "浦和レッズ",
"game_start_at": "2014/05/03 16:04",
"referee": "廣瀬　格"
},
{
"teams": [
"ジュビロ磐田",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "八田　直樹,駒野　友一,藤田　義明,伊野波　雅彦,櫻内　渚,ペク　ソンドン,フェルジナンド,小林　祐希,山田　大記,前田　遼一,ポポ",
"away_shoot": 10,
"home_director": "シャムスカ",
"away_team": "Ｖ・ファーレン長崎",
"weather": "晴",
"series_number": 11,
"temperature": 24,
"away_score": 0,
"away_start_member": "大久保　択生,岡本　拓也,山口　貴弘,古部　健太,神崎　大輔,黒木　聖仁,三原　雅俊,野田　紘史,奥埜　博亮,東　浩史,佐藤　洸一",
"home_score": 1,
"home_shoot": 5,
"game_id": "16093",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/05/03 16:06",
"referee": "扇谷　健司"
},
{
"teams": [
"ロアッソ熊本",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "シュミット　ダニエル,園田　拓也,篠原　弘次郎,矢野　大輔,片山　奨典,橋本　拳人,原田　拓,中山　雄登,齊藤　和樹,仲間　隼斗,澤田　崇",
"away_shoot": 5,
"home_director": "小野　剛",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 11,
"temperature": 22,
"away_score": 0,
"away_start_member": "中林　洋次,鎌田　翔雅,後藤　圭太,田所　諒,久木田　紳吾,島田　譲,上田　康太,染矢　一樹,石原　崇兆,林　容平,久保　裕一",
"home_score": 0,
"home_shoot": 12,
"game_id": "16094",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/05/03 17:03",
"referee": "森川　浩次"
},
{
"teams": [
"大宮アルディージャ",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "江角　浩司,今井　智基,菊地　光将,高橋　祥平,渡部　大輔,中村　北斗,増田　誓志,片岡　洋介,家長　昭博,富山　貴光,ズラタン",
"away_shoot": 10,
"home_director": "大熊　清",
"away_team": "アルビレックス新潟",
"weather": "晴",
"series_number": 11,
"temperature": 25.4,
"away_score": 2,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,金　珍洙,レオ　シルバ,小林　裕紀,成岡　翔,田中　亜土夢,岡本　英也,川又　堅碁",
"home_score": 2,
"home_shoot": 10,
"game_id": "15760",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/05/03 17:04",
"referee": "西村　雄一"
},
{
"teams": [
"京都サンガF.C.",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,ジャイロ,工藤　浩平,中山　博貴,横谷　繁,三平　和司,大黒　将志",
"away_shoot": 10,
"home_director": "バドゥ",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 11,
"temperature": 18.1,
"away_score": 1,
"away_start_member": "石井　健太,藤井　航大,武田　有祐,ソン　ハンキ,森保　翔平,山本　翔平,綱田　大志,沼田　圭悟,西野　泰正,アンドレア,高橋　泰",
"home_score": 4,
"home_shoot": 14,
"game_id": "16095",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/05/03 18:04",
"referee": "今村　義朗"
},
{
"teams": [
"名古屋グランパス",
"セレッソ大阪"
],
"away_director": "ランコ　ポポヴィッチ",
"home_start_member": "楢﨑　正剛,矢野　貴章,ハーフナー　ニッキ,田中　マルクス闘莉王,本多　勇喜,枝村　匠馬,田口　泰士,中村　直志,小川　佳純,玉田　圭司,永井　謙佑",
"away_shoot": 11,
"home_director": "西野　朗",
"away_team": "セレッソ大阪",
"weather": "晴",
"series_number": 11,
"temperature": 17.8,
"away_score": 2,
"away_start_member": "武田　博行,染谷　悠太,藤本　康太,酒本　憲幸,山下　達也,扇原　貴宏,山口　蛍,南野　拓実,丸橋　祐介,柿谷　曜一朗,フォルラン",
"home_score": 1,
"home_shoot": 13,
"game_id": "15765",
"home_team": "名古屋グランパス",
"game_start_at": "2014/05/03 19:04",
"referee": "山本　雄大"
},
{
"teams": [
"ＦＣ東京",
"大宮アルディージャ"
],
"away_director": "大熊　清",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,東　慶悟,渡邉　千真,平山　相太,武藤　嘉紀",
"away_shoot": 9,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "大宮アルディージャ",
"weather": "曇",
"series_number": 12,
"temperature": 13.2,
"away_score": 1,
"away_start_member": "江角　浩司,今井　智基,菊地　光将,高橋　祥平,中村　北斗,家長　昭博,片岡　洋介,横山　知伸,増田　誓志,富山　貴光,ズラタン",
"home_score": 0,
"home_shoot": 14,
"game_id": "15770",
"home_team": "ＦＣ東京",
"game_start_at": "2014/05/06 13:03",
"referee": "扇谷　健司"
},
{
"teams": [
"コンサドーレ札幌",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "金山　隼樹,日高　拓磨,櫛引　一紀,奈良　竜樹,松本　怜大,宮澤　裕樹,前　貴之,石井　謙伍,工藤　光輝,菊岡　拓朗,前田　俊介",
"away_shoot": 17,
"home_director": "財前　恵一",
"away_team": "ロアッソ熊本",
"weather": "屋内",
"series_number": 12,
"temperature": 22.2,
"away_score": 2,
"away_start_member": "シュミット　ダニエル,藏川　洋平,園田　拓也,矢野　大輔,片山　奨典,養父　雄仁,橋本　拳人,仲間　隼斗,中山　雄登,岡本　賢明,巻　誠一郎",
"home_score": 2,
"home_shoot": 14,
"game_id": "16096",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/05/06 13:03",
"referee": "西村　雄一"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"水戸ホーリーホック"
],
"away_director": "*** 水戸 30 鈴木　隆行の警告は試合終了後の警告",
"home_start_member": "大久保　択生,岡本　拓也,山口　貴弘,古部　健太,神崎　大輔,黒木　聖仁,三原　雅俊,石神　直哉,奥埜　博亮,東　浩史,イ　デホン",
"away_shoot": 9,
"home_director": "柱谷　哲二",
"away_team": "水戸ホーリーホック",
"weather": "晴",
"series_number": 12,
"temperature": 24.1,
"away_score": 1,
"away_start_member": "本間　幸司,新里　亮,金　聖基,尾本　敬,内田　航平,中里　崇宏,広瀬　陸斗,小谷野　顕治,船谷　圭祐,馬場　賢治,三島　康平",
"home_score": 1,
"home_shoot": 8,
"game_id": "16098",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/05/06 13:03",
"referee": "東城　穣"
},
{
"teams": [
"大分トリニータ",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "武田　洋平,岩武　克弥,阪田　章裕,高木　和道,安川　有,末吉　隼也,伊藤　大介,為田　大貴,松本　怜,風間　宏矢,後藤　優介",
"away_shoot": 15,
"home_director": "田坂　和昭",
"away_team": "松本山雅ＦＣ",
"weather": "晴",
"series_number": 12,
"temperature": 20.5,
"away_score": 2,
"away_start_member": "村山　智彦,多々良　敦斗,飯田　真輝,犬飼　智也,岩沼　俊介,岩間　雄大,ユン　ソンヨル,岩上　祐三,田中　隼磨,サビア,船山　貴之",
"home_score": 0,
"home_shoot": 7,
"game_id": "16099",
"home_team": "大分トリニータ",
"game_start_at": "2014/05/06 13:03",
"referee": "上田　益也"
},
{
"teams": [
"ベガルタ仙台",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "関　憲太郎,武井　択也,渡辺　広大,鎌田　次郎,石川　直樹,太田　吉彰,富田　晋伍,角田　誠,梁　勇基,武藤　雄樹,ウイルソン",
"away_shoot": 13,
"home_director": "渡邉　晋",
"away_team": "ヴィッセル神戸",
"weather": "晴",
"series_number": 12,
"temperature": 16.4,
"away_score": 3,
"away_start_member": "山本　海人,茂木　弘人,増川　隆洋,岩波　拓也,奥井　諒,チョン　ウヨン,橋本　英郎,森岡　亮太,ペドロ　ジュニオール,小川　慶治朗,マルキーニョス",
"home_score": 4,
"home_shoot": 13,
"game_id": "15768",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/05/06 13:04",
"referee": "池内　明彦"
},
{
"teams": [
"カターレ富山",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "飯田　健巳,木村　勝太,吉川　拓也,御厨　貴文,田中　寛己,ソ　ヨンドク,大西　容平,秋本　倫孝,中島　翔哉,白崎　凌兵,苔口　卓也",
"away_shoot": 11,
"home_director": "安間　貴義",
"away_team": "ギラヴァンツ北九州",
"weather": "晴",
"series_number": 12,
"temperature": 19.6,
"away_score": 2,
"away_start_member": "大谷　幸輝,宮本　亨,渡邉　将基,前田　和哉,冨士　祐樹,鈴木　修人,八角　剛史,小手川　宏基,渡　大生,池元　友樹,大島　秀夫",
"home_score": 0,
"home_shoot": 10,
"game_id": "16097",
"home_team": "カターレ富山",
"game_start_at": "2014/05/06 13:04",
"referee": "小屋　幸栄"
},
{
"teams": [
"横浜ＦＣ",
"京都サンガF.C."
],
"away_director": "バドゥ",
"home_start_member": "渋谷　飛翔,市村　篤司,ドウグラス,野上　結貴,永田　拓也,松下　裕樹,寺田　紳一,小野瀬　康介,飯尾　一慶,野崎　陽介,ホナウド",
"away_shoot": 5,
"home_director": "山口　素弘",
"away_team": "京都サンガF.C.",
"weather": "曇",
"series_number": 12,
"temperature": 13.4,
"away_score": 2,
"away_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,ジャイロ,工藤　浩平,中山　博貴,三平　和司,大黒　将志,横谷　繁",
"home_score": 0,
"home_shoot": 3,
"game_id": "16100",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/05/06 14:03",
"referee": "長谷　拓"
},
{
"teams": [
"アルビレックス新潟",
"清水エスパルス"
],
"away_director": "アフシン　ゴトビ",
"home_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,金　珍洙,レオ　シルバ,小泉　慶,成岡　翔,田中　亜土夢,岡本　英也,川又　堅碁",
"away_shoot": 6,
"home_director": "柳下　正明",
"away_team": "清水エスパルス",
"weather": "晴",
"series_number": 12,
"temperature": 15.9,
"away_score": 1,
"away_start_member": "櫛引　政敏,ヤコヴィッチ,平岡　康裕,カルフィン　ヨン　ア　ピン,吉田　豊,鍋田　亜人夢,六平　光成,竹内　涼,河井　陽介,大前　元紀,ノヴァコヴィッチ",
"home_score": 2,
"home_shoot": 11,
"game_id": "15772",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/05/06 14:04",
"referee": "高山　啓義"
},
{
"teams": [
"ファジアーノ岡山",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "中林　洋次,鎌田　翔雅,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,妹尾　隆佑,片山　瑛一,清水　慎太郎",
"away_shoot": 16,
"home_director": "影山　雅永",
"away_team": "アビスパ福岡",
"weather": "晴",
"series_number": 12,
"temperature": 19.9,
"away_score": 1,
"away_start_member": "神山　竜一,阿部　巧,堤　俊輔,イ　グァンソン,古賀　正紘,武田　英二郎,中原　秀人,酒井　宣福,石津　大介,城後　寿,坂田　大輔",
"home_score": 1,
"home_shoot": 7,
"game_id": "16101",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/05/06 14:04",
"referee": "塚田　健太"
},
{
"teams": [
"カマタマーレ讃岐",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "石井　健太,藤井　航大,武田　有祐,ソン　ハンキ,関原　凌河,岡村　和哉,高木　和正,小澤　雄希,西野　泰正,高橋　泰,野口　遼太",
"away_shoot": 11,
"home_director": "北野　誠",
"away_team": "東京ヴェルディ",
"weather": "晴",
"series_number": 12,
"temperature": 22.6,
"away_score": 1,
"away_start_member": "佐藤　優也,安西　幸輝,金　鐘必,井林　章,安在　和樹,田村　直也,姜　成浩,前田　直輝,鈴木　惇,常盤　聡,平本　一樹",
"home_score": 0,
"home_shoot": 9,
"game_id": "16102",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/05/06 15:01",
"referee": "野田　祐樹"
},
{
"teams": [
"鹿島アントラーズ",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,梅鉢　貴秀,小笠原　満男,カイオ,ジャイール,柴崎　岳,ダヴィ",
"away_shoot": 11,
"home_director": "トニーニョ　セレーゾ",
"away_team": "名古屋グランパス",
"weather": "曇",
"series_number": 12,
"temperature": 15.4,
"away_score": 2,
"away_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,枝村　匠馬,田口　泰士,中村　直志,小川　佳純,玉田　圭司,松田　力",
"home_score": 1,
"home_shoot": 13,
"game_id": "15769",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/05/06 15:04",
"referee": "吉田　寿光"
},
{
"teams": [
"サガン鳥栖",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "林　彰洋,丹羽　竜平,キム　ミンヒョク,呂　成海,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,早坂　良太,豊田　陽平",
"away_shoot": 5,
"home_director": "尹　晶煥",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 12,
"temperature": 19.8,
"away_score": 0,
"away_start_member": "菅野　孝憲,鈴木　大輔,近藤　直也,渡部　博文,橋本　和,高山　薫,茨田　陽生,秋野　央樹,太田　徹郎,田中　順也,工藤　壮人",
"home_score": 1,
"home_shoot": 6,
"game_id": "15774",
"home_team": "サガン鳥栖",
"game_start_at": "2014/05/06 15:04",
"referee": "木村　博之"
},
{
"teams": [
"ヴァンフォーレ甲府",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "岡　大生,青山　直晃,山本　英臣,佐々木　翔,福田　健介,新井　涼平,マルキーニョス　パラナ,阿部　翔平,ジウシーニョ,盛田　剛平,クリスティアーノ",
"away_shoot": 11,
"home_director": "城福　浩",
"away_team": "浦和レッズ",
"weather": "曇",
"series_number": 12,
"temperature": 14.4,
"away_score": 0,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,梅崎　司,柏木　陽介,阿部　勇樹,関口　訓充,原口　元気,興梠　慎三,李　忠成",
"home_score": 0,
"home_shoot": 6,
"game_id": "15771",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/05/06 16:04",
"referee": "山本　雄大"
},
{
"teams": [
"ザスパクサツ群馬",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "内藤　圭佑,夛田　凌輔,青木　良太,小柳　達司,瀬川　和樹,青木　孝太,黄　誠秀,坂井　洋平,小林　竜樹,永田　亮太,ダニエル　ロビーニョ",
"away_shoot": 9,
"home_director": "秋葉　忠宏",
"away_team": "モンテディオ山形",
"weather": "晴",
"series_number": 12,
"temperature": 14.4,
"away_score": 1,
"away_start_member": "清水　健太,山田　拓巳,西河　翔吾,イ　ジュヨン,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,中島　裕希,川西　翔太,秋葉　勝",
"home_score": 1,
"home_shoot": 18,
"game_id": "16103",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/05/06 16:04",
"referee": "岡部　拓人"
},
{
"teams": [
"湘南ベルマーレ",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,菊地　俊介,永木　亮太,菊池　大介,中川　寛斗,大槻　周平,武富　孝介",
"away_shoot": 7,
"home_director": "曺　貴裁",
"away_team": "栃木ＳＣ",
"weather": "曇",
"series_number": 12,
"temperature": 14.4,
"away_score": 1,
"away_start_member": "柴崎　邦博,山形　辰徳,チャ　ヨンファン,ドゥドゥ,赤井　秀行,廣瀬　浩二,菅　和範,小野寺　達也,近藤　祐介,重松　健太郎,瀬沼　優司",
"home_score": 2,
"home_shoot": 13,
"game_id": "16104",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/05/06 16:04",
"referee": "松尾　一"
},
{
"teams": [
"愛媛ＦＣ",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "児玉　剛,ハン　ヒフン,代　健司,林堂　眞,西岡　大輝,村上　巧,吉村　圭司,原川　力,藤　直也,西田　剛,表原　玄太",
"away_shoot": 8,
"home_director": "石丸　清隆",
"away_team": "ジュビロ磐田",
"weather": "晴",
"series_number": 12,
"temperature": 15.3,
"away_score": 1,
"away_start_member": "八田　直樹,岡田　隆,駒野　友一,伊野波　雅彦,櫻内　渚,藤田　義明,小林　祐希,山田　大記,松井　大輔,阿部　吉朗,前田　遼一",
"home_score": 0,
"home_shoot": 8,
"game_id": "16105",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/05/06 18:05",
"referee": "福島　孝一郎"
},
{
"teams": [
"ガンバ大阪",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "東口　順昭,オ　ジェソク,西野　貴治,岩下　敬輔,藤春　廣輝,今野　泰幸,遠藤　保仁,大森　晃太郎,二川　孝広,宇佐美　貴史,リンス",
"away_shoot": 3,
"home_director": "長谷川　健太",
"away_team": "徳島ヴォルティス",
"weather": "晴",
"series_number": 12,
"temperature": 15,
"away_score": 0,
"away_start_member": "長谷川　徹,小暮　大器,藤原　広太朗,橋内　優也,李　栄直,窪田　良,小島　秀仁,花井　聖,衛藤　裕,津田　知宏,ドウグラス",
"home_score": 3,
"home_shoot": 15,
"game_id": "15773",
"home_team": "ガンバ大阪",
"game_start_at": "2014/05/06 19:04",
"referee": "村上　伸次"
},
{
"teams": [
"ＦＣ岐阜",
"ジェフユナイテッド千葉"
],
"away_director": "鈴木　淳",
"home_start_member": "川口　能活,益山　司,阿部　正紀,関田　寛士,野垣内　俊,ヘニキ,水野　泰輔,比嘉　諒人,髙地　系治,田中　智大,ナザリト",
"away_shoot": 10,
"home_director": "ラモス　瑠偉",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 12,
"temperature": 16.5,
"away_score": 2,
"away_start_member": "岡本　昌弘,天野　貴史,キム　ヒョヌン,大岩　一貴,中村　太亮,兵働　昭弘,佐藤　健太郎,田中　佑昌,谷澤　達也,大塚　翔平,森本　貴幸",
"home_score": 2,
"home_shoot": 15,
"game_id": "16106",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/05/06 19:04",
"referee": "井上　知大"
},
{
"teams": [
"名古屋グランパス",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,枝村　匠馬,中村　直志,田口　泰士,小川　佳純,玉田　圭司,松田　力",
"away_shoot": 16,
"home_director": "西野　朗",
"away_team": "ガンバ大阪",
"weather": "晴",
"series_number": 13,
"temperature": 23.6,
"away_score": 2,
"away_start_member": "東口　順昭,オ　ジェソク,西野　貴治,岩下　敬輔,藤春　廣輝,今野　泰幸,遠藤　保仁,阿部　浩之,二川　孝広,宇佐美　貴史,倉田　秋",
"home_score": 1,
"home_shoot": 12,
"game_id": "15780",
"home_team": "名古屋グランパス",
"game_start_at": "2014/05/10 13:04",
"referee": "家本　政明"
},
{
"teams": [
"横浜Ｆ・マリノス",
"サガン鳥栖"
],
"away_director": "尹　晶煥",
"home_start_member": "榎本　哲也,奈良輪　雄太,栗原　勇蔵,中澤　佑二,ドゥトラ,三門　雄大,小椋　祥平,藤本　淳吾,齋藤　学,藤田　祥史,伊藤　翔",
"away_shoot": 9,
"home_director": "樋口　靖洋",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 13,
"temperature": 25.7,
"away_score": 2,
"away_start_member": "林　彰洋,丹羽　竜平,キム　ミンヒョク,呂　成海,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 1,
"home_shoot": 13,
"game_id": "15779",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/05/10 14:04",
"referee": "廣瀬　格"
},
{
"teams": [
"徳島ヴォルティス",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "長谷川　徹,藤原　広太朗,橋内　優也,福元　洋平,李　栄直,斉藤　大介,濱田　武,小島　秀仁,大﨑　淳矢,佐々木　一輝,高崎　寛之",
"away_shoot": 22,
"home_director": "小林　伸二",
"away_team": "ＦＣ東京",
"weather": "晴",
"series_number": 13,
"temperature": 21.6,
"away_score": 0,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,東　慶悟,河野　広貴,渡邉　千真,平山　相太",
"home_score": 0,
"home_shoot": 8,
"game_id": "15782",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/05/10 14:04",
"referee": "岡部　拓人"
},
{
"teams": [
"サンフレッチェ広島",
"清水エスパルス"
],
"away_director": "アフシン　ゴトビ",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,ミキッチ,青山　敏弘,森﨑　和幸,清水　航平,石原　直樹,森﨑　浩司,佐藤　寿人",
"away_shoot": 9,
"home_director": "森保　一",
"away_team": "清水エスパルス",
"weather": "晴",
"series_number": 13,
"temperature": 23.9,
"away_score": 1,
"away_start_member": "櫛引　政敏,ヤコヴィッチ,平岡　康裕,カルフィン　ヨン　ア　ピン,吉田　豊,杉山　浩太,六平　光成,竹内　涼,河井　陽介,大前　元紀,ノヴァコヴィッチ",
"home_score": 1,
"home_shoot": 10,
"game_id": "15785",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/05/10 14:04",
"referee": "東城　穣"
},
{
"teams": [
"川崎フロンターレ",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "西部　洋平,田中　裕介,ジェシ,中澤　聡太,谷口　彰悟,大島　僚太,中村　憲剛,森谷　賢太郎,レナト,小林　悠,大久保　嘉人",
"away_shoot": 15,
"home_director": "風間　八宏",
"away_team": "鹿島アントラーズ",
"weather": "晴",
"series_number": 13,
"temperature": 24.1,
"away_score": 1,
"away_start_member": "曽ヶ端　準,伊東　幸敏,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,ダヴィ",
"home_score": 4,
"home_shoot": 10,
"game_id": "15783",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/05/10 15:03",
"referee": "村上　伸次"
},
{
"teams": [
"ヴィッセル神戸",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "山本　海人,大屋　翼,河本　裕之,増川　隆洋,チョン　ウヨン,森岡　亮太,ペドロ　ジュニオール,小川　慶治朗,高橋　峻希,茂木　弘人,マルキーニョス",
"away_shoot": 14,
"home_director": "安達　亮",
"away_team": "ヴァンフォーレ甲府",
"weather": "晴",
"series_number": 13,
"temperature": 21.6,
"away_score": 0,
"away_start_member": "岡　大生,青山　直晃,津田　琢磨,佐々木　翔,福田　健介,新井　涼平,マルキーニョス　パラナ,阿部　翔平,ジウシーニョ,盛田　剛平,クリスティアーノ",
"home_score": 1,
"home_shoot": 6,
"game_id": "15781",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/05/10 15:04",
"referee": "今村　義朗"
},
{
"teams": [
"大宮アルディージャ",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "江角　浩司,今井　智基,菊地　光将,高橋　祥平,中村　北斗,家長　昭博,片岡　洋介,横山　知伸,増田　誓志,富山　貴光,長谷川　悠",
"away_shoot": 12,
"home_director": "大熊　清",
"away_team": "浦和レッズ",
"weather": "晴",
"series_number": 13,
"temperature": 23.1,
"away_score": 2,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,青木　拓矢,阿部　勇樹,宇賀神　友弥,原口　元気,柏木　陽介,興梠　慎三",
"home_score": 0,
"home_shoot": 6,
"game_id": "15777",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/05/10 16:04",
"referee": "松尾　一"
},
{
"teams": [
"セレッソ大阪",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "キム　ジンヒョン,藤本　康太,丸橋　祐介,酒本　憲幸,ゴイコ　カチャル,扇原　貴宏,長谷川　アーリアジャスール,山口　蛍,南野　拓実,柿谷　曜一朗,フォルラン",
"away_shoot": 6,
"home_director": "ランコ　ポポヴィッチ",
"away_team": "ベガルタ仙台",
"weather": "晴",
"series_number": 13,
"temperature": 23.9,
"away_score": 1,
"away_start_member": "関　憲太郎,菅井　直樹,渡辺　広大,鎌田　次郎,石川　直樹,太田　吉彰,富田　晋伍,武井　択也,梁　勇基,ウイルソン,武藤　雄樹",
"home_score": 0,
"home_shoot": 9,
"game_id": "15784",
"home_team": "セレッソ大阪",
"game_start_at": "2014/05/10 16:04",
"referee": "扇谷　健司"
},
{
"teams": [
"柏レイソル",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "菅野　孝憲,鈴木　大輔,近藤　直也,渡部　博文,橋本　和,高山　薫,茨田　陽生,小林　祐介,狩野　健太,田中　順也,工藤　壮人",
"away_shoot": 8,
"home_director": "ネルシーニョ",
"away_team": "アルビレックス新潟",
"weather": "晴",
"series_number": 13,
"temperature": 20.8,
"away_score": 0,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,大野　和成,レオ　シルバ,小林　裕紀,成岡　翔,田中　亜土夢,岡本　英也,川又　堅碁",
"home_score": 1,
"home_shoot": 10,
"game_id": "15778",
"home_team": "柏レイソル",
"game_start_at": "2014/05/10 19:04",
"referee": "中村　太"
},
{
"teams": [
"栃木ＳＣ",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "榎本　達也,山形　辰徳,チャ　ヨンファン,ドゥドゥ,赤井　秀行,廣瀬　浩二,岡根　直哉,小野寺　達也,近藤　祐介,瀬沼　優司,大久保　哲哉",
"away_shoot": 9,
"home_director": "阪倉　裕二",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 13,
"temperature": 24,
"away_score": 1,
"away_start_member": "中林　洋次,鎌田　翔雅,後藤　圭太,田所　諒,田中　奏一,島田　譲,上田　康太,三村　真,石原　崇兆,片山　瑛一,清水　慎太郎",
"home_score": 0,
"home_shoot": 14,
"game_id": "16109",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/05/11 13:03",
"referee": "上田　益也"
},
{
"teams": [
"松本山雅ＦＣ",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,多々良　敦斗,岩上　祐三,岩間　雄大,岩沼　俊介,喜山　康平,船山　貴之,サビア",
"away_shoot": 5,
"home_director": "反町　康治",
"away_team": "横浜ＦＣ",
"weather": "晴",
"series_number": 13,
"temperature": 25.9,
"away_score": 0,
"away_start_member": "渋谷　飛翔,市村　篤司,ドウグラス,野上　結貴,永田　拓也,安　英学,寺田　紳一,小池　純輝,内田　智也,野崎　陽介,ホナウド",
"home_score": 2,
"home_shoot": 9,
"game_id": "16110",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/05/11 13:03",
"referee": "前田　拓哉"
},
{
"teams": [
"モンテディオ山形",
"ジェフユナイテッド千葉"
],
"away_director": "鈴木　淳",
"home_start_member": "清水　健太,山田　拓巳,西河　翔吾,イ　ジュヨン,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,中島　裕希,川西　翔太,秋葉　勝",
"away_shoot": 11,
"home_director": "石﨑　信弘",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 13,
"temperature": 24,
"away_score": 1,
"away_start_member": "岡本　昌弘,キム　ヒョヌン,大岩　一貴,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,田中　佑昌,谷澤　達也,大塚　翔平,ケンペス",
"home_score": 1,
"home_shoot": 10,
"game_id": "16107",
"home_team": "モンテディオ山形",
"game_start_at": "2014/05/11 13:04",
"referee": "三上　正一郎"
},
{
"teams": [
"水戸ホーリーホック",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "本間　幸司,金　聖基,新里　亮,田中　雄大,中里　崇宏,内田　航平,広瀬　陸斗,小澤　司,船谷　圭祐,馬場　賢治,三島　康平",
"away_shoot": 9,
"home_director": "柱谷　哲二",
"away_team": "ＦＣ岐阜",
"weather": "晴",
"series_number": 13,
"temperature": 22.1,
"away_score": 2,
"away_start_member": "川口　能活,益山　司,阿部　正紀,関田　寛士,野垣内　俊,ヘニキ,水野　泰輔,太田　圭輔,髙地　系治,田中　智大,ナザリト",
"home_score": 3,
"home_shoot": 11,
"game_id": "16108",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/05/11 13:04",
"referee": "池内　明彦"
},
{
"teams": [
"京都サンガF.C.",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,ジャイロ,工藤　浩平,中山　博貴,三平　和司,大黒　将志,横谷　繁",
"away_shoot": 6,
"home_director": "バドゥ",
"away_team": "Ｖ・ファーレン長崎",
"weather": "曇",
"series_number": 13,
"temperature": 23.9,
"away_score": 0,
"away_start_member": "大久保　択生,岡本　拓也,山口　貴弘,下田　光平,神崎　大輔,前田　悠佑,三原　雅俊,野田　紘史,黒木　聖仁,奥埜　博亮,イ　デホン",
"home_score": 2,
"home_shoot": 7,
"game_id": "16111",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/05/11 13:04",
"referee": "吉田　寿光"
},
{
"teams": [
"アビスパ福岡",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "神山　竜一,阿部　巧,堤　俊輔,イ　グァンソン,武田　英二郎,中原　秀人,森村　昂太,坂田　大輔,城後　寿,石津　大介,酒井　宣福",
"away_shoot": 8,
"home_director": "マリヤン　プシュニク",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 13,
"temperature": 25.8,
"away_score": 1,
"away_start_member": "飯田　健巳,木村　勝太,吉川　拓也,御厨　貴文,田中　寛己,木本　敬介,大西　容平,秋本　倫孝,中島　翔哉,白崎　凌兵,苔口　卓也",
"home_score": 2,
"home_shoot": 8,
"game_id": "16112",
"home_team": "アビスパ福岡",
"game_start_at": "2014/05/11 14:04",
"referee": "山本　雄大"
},
{
"teams": [
"東京ヴェルディ",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "佐藤　優也,田中　貴大,金　鐘必,井林　章,安在　和樹,田村　直也,姜　成浩,安西　幸輝,鈴木　惇,常盤　聡,菅嶋　弘希",
"away_shoot": 4,
"home_director": "三浦　泰年",
"away_team": "ギラヴァンツ北九州",
"weather": "晴",
"series_number": 13,
"temperature": 21.9,
"away_score": 0,
"away_start_member": "大谷　幸輝,宮本　亨,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"home_score": 1,
"home_shoot": 8,
"game_id": "16114",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/05/11 16:03",
"referee": "森川　浩次"
},
{
"teams": [
"ロアッソ熊本",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "金井　大樹,藏川　洋平,篠原　弘次郎,園田　拓也,片山　奨典,養父　雄仁,原田　拓,中山　雄登,齊藤　和樹,仲間　隼斗,澤田　崇",
"away_shoot": 14,
"home_director": "小野　剛",
"away_team": "湘南ベルマーレ",
"weather": "晴",
"series_number": 13,
"temperature": 25.6,
"away_score": 3,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,宇佐美　宏和,菊地　俊介,永木　亮太,菊池　大介,大槻　周平,ウェリントン,武富　孝介",
"home_score": 1,
"home_shoot": 9,
"game_id": "16116",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/05/11 16:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"ザスパクサツ群馬",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "内藤　圭佑,小柳　達司,クォン　ハンジン,夛田　凌輔,瀬川　和樹,青木　孝太,坂井　洋平,黄　誠秀,小林　竜樹,ダニエル　ロビーニョ,永田　亮太",
"away_shoot": 11,
"home_director": "秋葉　忠宏",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 13,
"temperature": 24.7,
"away_score": 0,
"away_start_member": "瀬口　拓弥,武田　有祐,藤井　航大,ソン　ハンキ,小澤　雄希,岡村　和哉,綱田　大志,山本　翔平,アンドレア,我那覇　和樹,高木　和正",
"home_score": 1,
"home_shoot": 9,
"game_id": "16113",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/05/11 16:04",
"referee": "河合　英治"
},
{
"teams": [
"ジュビロ磐田",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "八田　直樹,駒野　友一,藤田　義明,伊野波　雅彦,櫻内　渚,フェルジナンド,松井　大輔,ポポ,小林　祐希,山田　大記,前田　遼一",
"away_shoot": 10,
"home_director": "シャムスカ",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 13,
"temperature": 20.9,
"away_score": 1,
"away_start_member": "武田　洋平,岩武　克弥,阪田　章裕,高木　和道,安川　有,末吉　隼也,伊藤　大介,松本　怜,松本　昌也,風間　宏矢,後藤　優介",
"home_score": 1,
"home_shoot": 8,
"game_id": "16115",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/05/11 16:04",
"referee": "小屋　幸栄"
},
{
"teams": [
"コンサドーレ札幌",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "金山　隼樹,日高　拓磨,薗田　淳,奈良　竜樹,石井　謙伍,河合　竜二,前　貴之,砂川　誠,宮澤　裕樹,菊岡　拓朗,前田　俊介",
"away_shoot": 3,
"home_director": "財前　恵一",
"away_team": "愛媛ＦＣ",
"weather": "屋内",
"series_number": 13,
"temperature": 22.6,
"away_score": 1,
"away_start_member": "児玉　剛,ハン　ヒフン,代　健司,林堂　眞,西岡　大輝,吉村　圭司,原川　力,堀米　勇輝,藤　直也,西田　剛,河原　和寿",
"home_score": 0,
"home_shoot": 12,
"game_id": "16117",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/05/12 19:03",
"referee": "佐藤　隆治"
},
{
"teams": [
"ヴァンフォーレ甲府",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,松橋　優,新井　涼平,マルキーニョス　パラナ,阿部　翔平,ジウシーニョ,盛田　剛平,クリスティアーノ",
"away_shoot": 5,
"home_director": "城福　浩",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 14,
"temperature": 26.4,
"away_score": 0,
"away_start_member": "菅野　孝憲,鈴木　大輔,近藤　直也,渡部　博文,橋本　和,高山　薫,小林　祐介,茨田　陽生,田中　順也,レアンドロ,工藤　壮人",
"home_score": 3,
"home_shoot": 7,
"game_id": "15789",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/05/17 13:04",
"referee": "パベル　ラチコフスキ"
},
{
"teams": [
"清水エスパルス",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "櫛引　政敏,ヤコヴィッチ,平岡　康裕,カルフィン　ヨン　ア　ピン,吉田　豊,杉山　浩太,六平　光成,竹内　涼,大前　元紀,高木　俊幸,ノヴァコヴィッチ",
"away_shoot": 7,
"home_director": "アフシン　ゴトビ",
"away_team": "ヴィッセル神戸",
"weather": "晴",
"series_number": 14,
"temperature": 23.1,
"away_score": 1,
"away_start_member": "山本　海人,茂木　弘人,河本　裕之,岩波　拓也,高橋　峻希,チョン　ウヨン,大屋　翼,森岡　亮太,小川　慶治朗,ペドロ　ジュニオール,マルキーニョス",
"home_score": 1,
"home_shoot": 17,
"game_id": "15791",
"home_team": "清水エスパルス",
"game_start_at": "2014/05/17 14:03",
"referee": "飯田　淳平"
},
{
"teams": [
"浦和レッズ",
"セレッソ大阪"
],
"away_director": "ランコ　ポポヴィッチ",
"home_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,梅崎　司,青木　拓矢,阿部　勇樹,宇賀神　友弥,原口　元気,柏木　陽介,興梠　慎三",
"away_shoot": 6,
"home_director": "ペトロヴィッチ",
"away_team": "セレッソ大阪",
"weather": "晴",
"series_number": 14,
"temperature": 23.6,
"away_score": 0,
"away_start_member": "キム　ジンヒョン,藤本　康太,山下　達也,ゴイコ　カチャル,長谷川　アーリアジャスール,山口　蛍,南野　拓実,丸橋　祐介,酒本　憲幸,柿谷　曜一朗,フォルラン",
"home_score": 1,
"home_shoot": 11,
"game_id": "15787",
"home_team": "浦和レッズ",
"game_start_at": "2014/05/17 14:04",
"referee": "木村　博之"
},
{
"teams": [
"アルビレックス新潟",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,大野　和成,レオ　シルバ,小林　裕紀,田中　亜土夢,岡本　英也,田中　達也,川又　堅碁",
"away_shoot": 3,
"home_director": "柳下　正明",
"away_team": "名古屋グランパス",
"weather": "曇",
"series_number": 14,
"temperature": 14.7,
"away_score": 1,
"away_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,枝村　匠馬,田口　泰士,中村　直志,小川　佳純,玉田　圭司,永井　謙佑",
"home_score": 1,
"home_shoot": 9,
"game_id": "15790",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/05/17 15:03",
"referee": "岡部　拓人"
},
{
"teams": [
"サガン鳥栖",
"大宮アルディージャ"
],
"away_director": "大熊　清",
"home_start_member": "林　彰洋,丹羽　竜平,キム　ミンヒョク,呂　成海,安田　理大,水沼　宏太,岡本　知剛,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 11,
"home_director": "尹　晶煥",
"away_team": "大宮アルディージャ",
"weather": "晴",
"series_number": 14,
"temperature": 25.2,
"away_score": 1,
"away_start_member": "江角　浩司,今井　智基,菊地　光将,高橋　祥平,中村　北斗,渡邉　大剛,片岡　洋介,増田　誓志,家長　昭博,富山　貴光,長谷川　悠",
"home_score": 1,
"home_shoot": 14,
"game_id": "15792",
"home_team": "サガン鳥栖",
"game_start_at": "2014/05/17 15:04",
"referee": "井上　知大"
},
{
"teams": [
"ＦＣ東京",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,三田　啓貴,河野　広貴,武藤　嘉紀,エドゥー",
"away_shoot": 10,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "ガンバ大阪",
"weather": "晴",
"series_number": 14,
"temperature": 20.5,
"away_score": 0,
"away_start_member": "東口　順昭,オ　ジェソク,西野　貴治,岩下　敬輔,藤春　廣輝,今野　泰幸,遠藤　保仁,阿部　浩之,大森　晃太郎,宇佐美　貴史,倉田　秋",
"home_score": 3,
"home_shoot": 9,
"game_id": "15788",
"home_team": "ＦＣ東京",
"game_start_at": "2014/05/17 18:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"鹿島アントラーズ",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "曽ヶ端　準,伊東　幸敏,植田　直通,昌子　源,前野　貴徳,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,赤﨑　秀平",
"away_shoot": 4,
"home_director": "トニーニョ　セレーゾ",
"away_team": "徳島ヴォルティス",
"weather": "曇",
"series_number": 14,
"temperature": 20.3,
"away_score": 0,
"away_start_member": "長谷川　徹,藤原　広太朗,橋内　優也,福元　洋平,アレックス,斉藤　大介,濱田　武,宮崎　光平,大﨑　淳矢,佐々木　一輝,高崎　寛之",
"home_score": 1,
"home_shoot": 26,
"game_id": "15786",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/05/17 19:04",
"referee": "高山　啓義"
},
{
"teams": [
"ファジアーノ岡山",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "中林　洋次,鎌田　翔雅,後藤　圭太,田所　諒,田中　奏一,島田　譲,上田　康太,三村　真,妹尾　隆佑,片山　瑛一,清水　慎太郎",
"away_shoot": 10,
"home_director": "影山　雅永",
"away_team": "ＦＣ岐阜",
"weather": "晴",
"series_number": 14,
"temperature": 25.6,
"away_score": 1,
"away_start_member": "時久　省吾,益山　司,阿部　正紀,関田　寛士,三都主　アレサンドロ,宮沢　正史,水野　泰輔,スティッペ,髙地　系治,田中　智大,難波　宏明",
"home_score": 2,
"home_shoot": 12,
"game_id": "16119",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/05/18 13:03",
"referee": "扇谷　健司"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "中村　隼,藤井　大輔,山口　貴弘,野田　紘史,神崎　大輔,前田　悠佑,三原　雅俊,古部　健太,東　浩史,黒木　聖仁,イ　デホン",
"away_shoot": 11,
"home_director": "高木　琢也",
"away_team": "栃木ＳＣ",
"weather": "曇のち晴",
"series_number": 14,
"temperature": 25.4,
"away_score": 1,
"away_start_member": "榎本　達也,山形　辰徳,チャ　ヨンファン,中野　洋司,イ　ミンス,廣瀬　浩二,西澤　代志也,小野寺　達也,湯澤　洋介,重松　健太郎,瀬沼　優司",
"home_score": 1,
"home_shoot": 18,
"game_id": "16121",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/05/18 13:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"大分トリニータ",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "武田　洋平,安川　有,阪田　章裕,高木　和道,西　弘則,伊藤　大介,末吉　隼也,松本　昌也,松本　怜,風間　宏矢,チェ　ジョンハン",
"away_shoot": 6,
"home_director": "田坂　和昭",
"away_team": "横浜ＦＣ",
"weather": "曇のち晴",
"series_number": 14,
"temperature": 24.1,
"away_score": 0,
"away_start_member": "渋谷　飛翔,市村　篤司,ドウグラス,野上　結貴,永田　拓也,松下　裕樹,安　英学,小池　純輝,寺田　紳一,黒津　勝,野崎　陽介",
"home_score": 1,
"home_shoot": 10,
"game_id": "16122",
"home_team": "大分トリニータ",
"game_start_at": "2014/05/18 13:03",
"referee": "塚田　健太"
},
{
"teams": [
"ベガルタ仙台",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "関　憲太郎,菅井　直樹,渡辺　広大,角田　誠,石川　直樹,太田　吉彰,富田　晋伍,武井　択也,梁　勇基,赤嶺　真吾,ウイルソン",
"away_shoot": 13,
"home_director": "渡邉　晋",
"away_team": "サンフレッチェ広島",
"weather": "晴",
"series_number": 14,
"temperature": 21.4,
"away_score": 0,
"away_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,ミキッチ,柴﨑　晃誠,森﨑　和幸,清水　航平,森﨑　浩司,髙萩　洋次郎,佐藤　寿人",
"home_score": 1,
"home_shoot": 11,
"game_id": "15793",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/05/18 13:04",
"referee": "西村　雄一"
},
{
"teams": [
"モンテディオ山形",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "清水　健太,山田　拓巳,西河　翔吾,イ　ジュヨン,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,秋葉　勝,中島　裕希,山﨑　雅人",
"away_shoot": 11,
"home_director": "石﨑　信弘",
"away_team": "松本山雅ＦＣ",
"weather": "晴",
"series_number": 14,
"temperature": 19,
"away_score": 0,
"away_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,多々良　敦斗,岩間　雄大,岩沼　俊介,岩上　祐三,喜山　康平,船山　貴之,サビア",
"home_score": 0,
"home_shoot": 9,
"game_id": "16118",
"home_team": "モンテディオ山形",
"game_start_at": "2014/05/18 13:04",
"referee": "野田　祐樹"
},
{
"teams": [
"愛媛ＦＣ",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "児玉　剛,ハン　ヒフン,代　健司,林堂　眞,西岡　大輝,吉村　圭司,原川　力,堀米　勇輝,藤　直也,西田　剛,河原　和寿",
"away_shoot": 10,
"home_director": "石丸　清隆",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 14,
"temperature": 24.4,
"away_score": 0,
"away_start_member": "瀬口　拓弥,武田　有祐,藤井　航大,野口　遼太,小澤　雄希,岡村　和哉,持留　新作,綱田　大志,アンドレア,高木　和正,我那覇　和樹",
"home_score": 2,
"home_shoot": 9,
"game_id": "16120",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/05/18 13:04",
"referee": "小屋　幸栄"
},
{
"teams": [
"ギラヴァンツ北九州",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"away_shoot": 6,
"home_director": "柱谷　幸一",
"away_team": "ザスパクサツ群馬",
"weather": "晴",
"series_number": 14,
"temperature": 26.6,
"away_score": 1,
"away_start_member": "内藤　圭佑,小柳　達司,クォン　ハンジン,乾　大知,瀬川　和樹,青木　孝太,坂井　洋平,黄　誠秀,小林　竜樹,ダニエル　ロビーニョ,野崎　桂太",
"home_score": 2,
"home_shoot": 9,
"game_id": "16123",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/05/18 14:03",
"referee": "岡　宏道"
},
{
"teams": [
"ロアッソ熊本",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "畑　実,藏川　洋平,園田　拓也,矢野　大輔,片山　奨典,橋本　拳人,養父　雄仁,中山　雄登,齊藤　和樹,仲間　隼斗,澤田　崇",
"away_shoot": 2,
"home_director": "小野　剛",
"away_team": "東京ヴェルディ",
"weather": "晴",
"series_number": 14,
"temperature": 24.8,
"away_score": 0,
"away_start_member": "佐藤　優也,田中　貴大,金　鐘必,井林　章,安在　和樹,田村　直也,姜　成浩,安西　幸輝,鈴木　惇,菅嶋　弘希,常盤　聡",
"home_score": 0,
"home_shoot": 9,
"game_id": "16124",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/05/18 14:03",
"referee": "日高　晴樹"
},
{
"teams": [
"川崎フロンターレ",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "西部　洋平,田中　裕介,ジェシ,中澤　聡太,谷口　彰悟,大島　僚太,中村　憲剛,森谷　賢太郎,レナト,小林　悠,大久保　嘉人",
"away_shoot": 12,
"home_director": "風間　八宏",
"away_team": "横浜Ｆ・マリノス",
"weather": "晴",
"series_number": 14,
"temperature": 23.7,
"away_score": 3,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,三門　雄大,富澤　清太郎,藤本　淳吾,中村　俊輔,齋藤　学,伊藤　翔",
"home_score": 0,
"home_shoot": 5,
"game_id": "15794",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/05/18 15:05",
"referee": "吉田　寿光"
},
{
"teams": [
"水戸ホーリーホック",
"京都サンガF.C."
],
"away_director": "バドゥ",
"home_start_member": "本間　幸司,新里　亮,金　聖基,田中　雄大,内田　航平,中里　崇宏,広瀬　陸斗,小澤　司,船谷　圭祐,馬場　賢治,三島　康平",
"away_shoot": 15,
"home_director": "柱谷　哲二",
"away_team": "京都サンガF.C.",
"weather": "晴",
"series_number": 14,
"temperature": 21.1,
"away_score": 1,
"away_start_member": "杉本　大地,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,ジャイロ,工藤　浩平,中山　博貴,三平　和司,大黒　将志,横谷　繁",
"home_score": 5,
"home_shoot": 14,
"game_id": "16125",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/05/18 16:03",
"referee": "松尾　一"
},
{
"teams": [
"ジェフユナイテッド千葉",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,大塚　翔平,ケンペス",
"away_shoot": 5,
"home_director": "鈴木　淳",
"away_team": "コンサドーレ札幌",
"weather": "晴",
"series_number": 14,
"temperature": 22.6,
"away_score": 0,
"away_start_member": "金山　隼樹,小山内　貴哉,薗田　淳,奈良　竜樹,上原　慎也,河合　竜二,上里　一将,宮澤　裕樹,都倉　賢,砂川　誠,前田　俊介",
"home_score": 2,
"home_shoot": 18,
"game_id": "16126",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/05/18 16:03",
"referee": "前田　拓哉"
},
{
"teams": [
"湘南ベルマーレ",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,菊地　俊介,永木　亮太,菊池　大介,大槻　周平,ウェリントン,武富　孝介",
"away_shoot": 6,
"home_director": "曺　貴裁",
"away_team": "アビスパ福岡",
"weather": "晴",
"series_number": 14,
"temperature": 20.1,
"away_score": 0,
"away_start_member": "神山　竜一,阿部　巧,武田　英二郎,古賀　正紘,イ　グァンソン,堤　俊輔,中原　秀人,酒井　宣福,石津　大介,坂田　大輔,城後　寿",
"home_score": 2,
"home_shoot": 18,
"game_id": "16127",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/05/18 16:04",
"referee": "家本　政明"
},
{
"teams": [
"カターレ富山",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "水谷　雄一,木村　勝太,吉川　拓也,御厨　貴文,平出　涼,木本　敬介,キム　ヨングン,秋本　倫孝,中島　翔哉,白崎　凌兵,苔口　卓也",
"away_shoot": 10,
"home_director": "安間　貴義",
"away_team": "ジュビロ磐田",
"weather": "晴",
"series_number": 14,
"temperature": 20.6,
"away_score": 1,
"away_start_member": "八田　直樹,駒野　友一,木下　高彰,藤田　義明,櫻内　渚,松井　大輔,フェルジナンド,小林　祐希,山田　大記,ポポ,前田　遼一",
"home_score": 0,
"home_shoot": 10,
"game_id": "16128",
"home_team": "カターレ富山",
"game_start_at": "2014/05/18 16:04",
"referee": "村上　伸次"
},
{
"teams": [
"栃木ＳＣ",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "榎本　達也,山形　辰徳,チャ　ヨンファン,ドゥドゥ,赤井　秀行,廣瀬　浩二,西澤　代志也,小野寺　達也,湯澤　洋介,重松　健太郎,瀬沼　優司",
"away_shoot": 9,
"home_director": "阪倉　裕二",
"away_team": "ロアッソ熊本",
"weather": "晴",
"series_number": 15,
"temperature": 23.8,
"away_score": 1,
"away_start_member": "畑　実,藏川　洋平,園田　拓也,矢野　大輔,片山　奨典,橋本　拳人,原田　拓,中山　雄登,養父　雄仁,澤田　崇,齊藤　和樹",
"home_score": 1,
"home_shoot": 9,
"game_id": "16129",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/05/24 13:03",
"referee": "篠藤　巧"
},
{
"teams": [
"横浜ＦＣ",
"ジェフユナイテッド千葉"
],
"away_director": "鈴木　淳",
"home_start_member": "南　雄太,市村　篤司,ドウグラス,野上　結貴,永田　拓也,安　英学,松下　裕樹,小池　純輝,寺田　紳一,野崎　陽介,黒津　勝",
"away_shoot": 7,
"home_director": "山口　素弘",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 15,
"temperature": 23.2,
"away_score": 0,
"away_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,町田　也真人,大塚　翔平",
"home_score": 0,
"home_shoot": 6,
"game_id": "16130",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/05/24 13:03",
"referee": "家本　政明"
},
{
"teams": [
"愛媛ＦＣ",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "児玉　剛,代　健司,浦田　延尚,林堂　眞,西岡　大輝,吉村　圭司,原川　力,堀米　勇輝,藤　直也,西田　剛,河原　和寿",
"away_shoot": 23,
"home_director": "石丸　清隆",
"away_team": "湘南ベルマーレ",
"weather": "晴",
"series_number": 15,
"temperature": 25,
"away_score": 0,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,菊地　俊介,永木　亮太,菊池　大介,大槻　周平,ウェリントン,武富　孝介",
"home_score": 1,
"home_shoot": 4,
"game_id": "16131",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/05/24 13:04",
"referee": "榎本　一慶"
},
{
"teams": [
"京都サンガF.C.",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,ジャイロ,工藤　浩平,中山　博貴,三平　和司,大黒　将志,山瀬　功治",
"away_shoot": 17,
"home_director": "バドゥ",
"away_team": "ザスパクサツ群馬",
"weather": "晴のち曇",
"series_number": 15,
"temperature": 27.6,
"away_score": 3,
"away_start_member": "内藤　圭佑,小柳　達司,クォン　ハンジン,黄　誠秀,瀬川　和樹,坂井　洋平,永田　亮太,夛田　凌輔,ダニエル　ロビーニョ,野崎　桂太,小林　竜樹",
"home_score": 0,
"home_shoot": 14,
"game_id": "16132",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/05/24 14:04",
"referee": "窪田　陽輔"
},
{
"teams": [
"東京ヴェルディ",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "佐藤　優也,森　勇介,金　鐘必,井林　章,安在　和樹,ニウド,田村　直也,安西　幸輝,鈴木　惇,菅嶋　弘希,常盤　聡",
"away_shoot": 10,
"home_director": "三浦　泰年",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 15,
"temperature": 24.4,
"away_score": 1,
"away_start_member": "武田　洋平,安川　有,阪田　章裕,高木　和道,西　弘則,伊藤　大介,末吉　隼也,松本　昌也,松本　怜,風間　宏矢,チェ　ジョンハン",
"home_score": 1,
"home_shoot": 13,
"game_id": "16133",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/05/24 16:03",
"referee": "飯田　淳平"
},
{
"teams": [
"アビスパ福岡",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "神山　竜一,三島　勇太,阿部　巧,イ　グァンソン,堤　俊輔,坂田　大輔,武田　英二郎,森村　昂太,酒井　宣福,城後　寿,石津　大介",
"away_shoot": 10,
"home_director": "マリヤン　プシュニク",
"away_team": "モンテディオ山形",
"weather": "晴",
"series_number": 15,
"temperature": 22.9,
"away_score": 1,
"away_start_member": "清水　健太,山田　拓巳,西河　翔吾,イ　ジュヨン,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,秋葉　勝,中島　裕希,山﨑　雅人",
"home_score": 0,
"home_shoot": 6,
"game_id": "16134",
"home_team": "アビスパ福岡",
"game_start_at": "2014/05/24 16:03",
"referee": "河合　英治"
},
{
"teams": [
"ファジアーノ岡山",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "中林　洋次,鎌田　翔雅,後藤　圭太,田所　諒,田中　奏一,島田　譲,上田　康太,三村　真,妹尾　隆佑,片山　瑛一,清水　慎太郎",
"away_shoot": 6,
"home_director": "影山　雅永",
"away_team": "Ｖ・ファーレン長崎",
"weather": "晴",
"series_number": 15,
"temperature": 22.1,
"away_score": 1,
"away_start_member": "中村　隼,岡本　拓也,山口　貴弘,下田　光平,古部　健太,黒木　聖仁,三原　雅俊,中村　祐哉,奥埜　博亮,小松　塁,水永　翔馬",
"home_score": 2,
"home_shoot": 8,
"game_id": "16136",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/05/24 19:03",
"referee": "三上　正一郎"
},
{
"teams": [
"カマタマーレ讃岐",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "瀬口　拓弥,ソン　ハンキ,武田　有祐,藤井　航大,小澤　雄希,綱田　大志,藤田　浩平,山本　翔平,持留　新作,アンドレア,高木　和正",
"away_shoot": 5,
"home_director": "北野　誠",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 15,
"temperature": 21.5,
"away_score": 1,
"away_start_member": "水谷　雄一,木村　勝太,御厨　貴文,吉川　拓也,平出　涼,木本　敬介,キム　ヨングン,秋本　倫孝,中島　翔哉,國吉　貴博,苔口　卓也",
"home_score": 2,
"home_shoot": 14,
"game_id": "16137",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/05/24 19:03",
"referee": "森川　浩次"
},
{
"teams": [
"松本山雅ＦＣ",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "村山　智彦,多々良　敦斗,飯田　真輝,犬飼　智也,岩沼　俊介,喜山　康平,岩間　雄大,田中　隼磨,岩上　祐三,塩沢　勝吾,船山　貴之",
"away_shoot": 14,
"home_director": "反町　康治",
"away_team": "ジュビロ磐田",
"weather": "晴のち曇",
"series_number": 15,
"temperature": 20.9,
"away_score": 1,
"away_start_member": "八田　直樹,櫻内　渚,木下　高彰,藤田　義明,ペク　ソンドン,フェルジナンド,小林　祐希,宮崎　智彦,山田　大記,前田　遼一,ポポ",
"home_score": 2,
"home_shoot": 11,
"game_id": "16135",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/05/24 19:04",
"referee": "今村　義朗"
},
{
"teams": [
"コンサドーレ札幌",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "金山　隼樹,小山内　貴哉,パウロン,奈良　竜樹,上原　慎也,河合　竜二,上里　一将,宮澤　裕樹,都倉　賢,石井　謙伍,前田　俊介",
"away_shoot": 8,
"home_director": "財前　恵一",
"away_team": "水戸ホーリーホック",
"weather": "屋内",
"series_number": 15,
"temperature": 21.5,
"away_score": 0,
"away_start_member": "本間　幸司,新里　亮,金　聖基,尾本　敬,内田　航平,中里　崇宏,広瀬　陸斗,小澤　司,船谷　圭祐,馬場　賢治,三島　康平",
"home_score": 4,
"home_shoot": 18,
"game_id": "16138",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/05/25 19:03",
"referee": "上田　益也"
},
{
"teams": [
"ＦＣ岐阜",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "時久　省吾,益山　司,阿部　正紀,関田　寛士,三都主　アレサンドロ,宮沢　正史,ヘニキ,スティッペ,髙地　系治,難波　宏明,中村　祐輝",
"away_shoot": 8,
"home_director": "ラモス　瑠偉",
"away_team": "ギラヴァンツ北九州",
"weather": "曇一時雨",
"series_number": 15,
"temperature": 25,
"away_score": 1,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,鈴木　修人,風間　宏希,小手川　宏基,渡　大生,原　一樹,池元　友樹",
"home_score": 1,
"home_shoot": 7,
"game_id": "16139",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/05/25 19:04",
"referee": "吉田　哲朗"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "大久保　択生,岡本　拓也,黒木　聖仁,下田　光平,神崎　大輔,井上　裕大,前田　悠佑,古部　健太,奥埜　博亮,東　浩史,佐藤　洸一",
"away_shoot": 8,
"home_director": "高木　琢也",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 16,
"temperature": 34.2,
"away_score": 1,
"away_start_member": "瀬口　拓弥,ソン　ハンキ,武田　有祐,藤井　航大,小澤　雄希,綱田　大志,山本　翔平,持留　新作,藤田　浩平,高木　和正,我那覇　和樹",
"home_score": 1,
"home_shoot": 11,
"game_id": "16142",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/05/31 13:03",
"referee": "岡　宏道"
},
{
"teams": [
"ザスパクサツ群馬",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "内藤　圭佑,夛田　凌輔,クォン　ハンジン,小柳　達司,瀬川　和樹,青木　孝太,坂井　洋平,黄　誠秀,小林　竜樹,ダニエル　ロビーニョ,野崎　桂太",
"away_shoot": 9,
"home_director": "秋葉　忠宏",
"away_team": "横浜ＦＣ",
"weather": "晴",
"series_number": 16,
"temperature": 32.3,
"away_score": 2,
"away_start_member": "南　雄太,市村　篤司,ドウグラス,野上　結貴,永田　拓也,松下　裕樹,安　英学,小池　純輝,寺田　紳一,野村　直輝,黒津　勝",
"home_score": 0,
"home_shoot": 11,
"game_id": "16140",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/05/31 13:04",
"referee": "塚田　智宏"
},
{
"teams": [
"ジュビロ磐田",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "八田　直樹,駒野　友一,菅沼　駿哉,藤田　義明,宮崎　智彦,フェルジナンド,小林　祐希,松井　大輔,ペク　ソンドン,前田　遼一,ポポ",
"away_shoot": 15,
"home_director": "シャムスカ",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 16,
"temperature": 26.4,
"away_score": 1,
"away_start_member": "中林　洋次,鎌田　翔雅,後藤　圭太,田所　諒,田中　奏一,島田　譲,上田　康太,三村　真,石原　崇兆,片山　瑛一,清水　慎太郎",
"home_score": 1,
"home_shoot": 16,
"game_id": "16141",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/05/31 13:04",
"referee": "パベル　ラチコフスキ"
},
{
"teams": [
"コンサドーレ札幌",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "金山　隼樹,小山内　貴哉,パウロン,奈良　竜樹,上原　慎也,河合　竜二,上里　一将,宮澤　裕樹,前田　俊介,石井　謙伍,内村　圭宏",
"away_shoot": 9,
"home_director": "財前　恵一",
"away_team": "アビスパ福岡",
"weather": "晴",
"series_number": 16,
"temperature": 25.3,
"away_score": 1,
"away_start_member": "神山　竜一,武田　英二郎,山口　和樹,古賀　正紘,イ　グァンソン,堤　俊輔,パク　ゴン,中原　秀人,光永　祐也,金森　健志,酒井　宣福",
"home_score": 1,
"home_shoot": 9,
"game_id": "16143",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/05/31 14:03",
"referee": "池内　明彦"
},
{
"teams": [
"ギラヴァンツ北九州",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,市川　恵多,冨士　祐樹,鈴木　修人,風間　宏希,渡　大生,小手川　宏基,原　一樹,池元　友樹",
"away_shoot": 10,
"home_director": "柱谷　幸一",
"away_team": "栃木ＳＣ",
"weather": "晴",
"series_number": 16,
"temperature": 30.4,
"away_score": 1,
"away_start_member": "鈴木　智幸,山形　辰徳,赤井　秀行,ドゥドゥ,鈴木　隆雅,近藤　祐介,廣瀬　浩二,岡根　直哉,湯澤　洋介,重松　健太郎,瀬沼　優司",
"home_score": 0,
"home_shoot": 6,
"game_id": "16144",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/05/31 14:03",
"referee": "岡部　拓人"
},
{
"teams": [
"ロアッソ熊本",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "畑　実,藏川　洋平,園田　拓也,矢野　大輔,片山　奨典,養父　雄仁,橋本　拳人,澤田　崇,齊藤　和樹,岡本　賢明,巻　誠一郎",
"away_shoot": 6,
"home_director": "小野　剛",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 16,
"temperature": 32.3,
"away_score": 0,
"away_start_member": "水谷　雄一,高　准翼,御厨　貴文,平出　涼,木村　勝太,木本　敬介,秋本　倫孝,キム　ヨングン,中島　翔哉,白崎　凌兵,三上　陽輔",
"home_score": 2,
"home_shoot": 14,
"game_id": "16145",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/05/31 14:03",
"referee": "野田　祐樹"
},
{
"teams": [
"水戸ホーリーホック",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "本間　幸司,新里　亮,金　聖基,尾本　敬,内田　航平,中里　崇宏,広瀬　陸斗,鈴木　雄斗,船谷　圭祐,馬場　賢治,三島　康平",
"away_shoot": 12,
"home_director": "柱谷　哲二",
"away_team": "松本山雅ＦＣ",
"weather": "晴",
"series_number": 16,
"temperature": 26.3,
"away_score": 2,
"away_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,多々良　敦斗,ユン　ソンヨル,岩上　祐三,鐡戸　裕史,岩沼　俊介,サビア,船山　貴之",
"home_score": 1,
"home_shoot": 6,
"game_id": "16146",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/05/31 16:03",
"referee": "井上　知大"
},
{
"teams": [
"湘南ベルマーレ",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,菊地　俊介,永木　亮太,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"away_shoot": 3,
"home_director": "曺　貴裁",
"away_team": "東京ヴェルディ",
"weather": "晴",
"series_number": 16,
"temperature": 23.6,
"away_score": 0,
"away_start_member": "佐藤　優也,安西　幸輝,金　鐘必,井林　章,安在　和樹,ニウド,田村　直也,常盤　聡,鈴木　惇,高木　大輔,菅嶋　弘希",
"home_score": 1,
"home_shoot": 20,
"game_id": "16147",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/05/31 16:04",
"referee": "小屋　幸栄"
},
{
"teams": [
"大分トリニータ",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "武田　洋平,西　弘則,阪田　章裕,高木　和道,安川　有,末吉　隼也,伊藤　大介,松本　昌也,松本　怜,風間　宏矢,チェ　ジョンハン",
"away_shoot": 16,
"home_director": "田坂　和昭",
"away_team": "モンテディオ山形",
"weather": "晴",
"series_number": 16,
"temperature": 28.1,
"away_score": 0,
"away_start_member": "清水　健太,山田　拓巳,イ　ジュヨン,西河　翔吾,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,秋葉　勝,中島　裕希,比嘉　厚平",
"home_score": 1,
"home_shoot": 5,
"game_id": "16148",
"home_team": "大分トリニータ",
"game_start_at": "2014/05/31 17:03",
"referee": "廣瀬　格"
},
{
"teams": [
"ジェフユナイテッド千葉",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,大塚　翔平,ケンペス",
"away_shoot": 6,
"home_director": "鈴木　淳",
"away_team": "愛媛ＦＣ",
"weather": "晴",
"series_number": 16,
"temperature": 23.5,
"away_score": 0,
"away_start_member": "児玉　剛,代　健司,浦田　延尚,林堂　眞,西岡　大輝,吉村　圭司,原川　力,堀米　勇輝,藤　直也,西田　剛,河原　和寿",
"home_score": 1,
"home_shoot": 20,
"game_id": "16149",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/05/31 19:03",
"referee": "塚田　健太"
},
{
"teams": [
"ＦＣ岐阜",
"京都サンガF.C."
],
"away_director": "バドゥ",
"home_start_member": "川口　能活,益山　司,阿部　正紀,木谷　公亮,三都主　アレサンドロ,宮沢　正史,ヘニキ,水野　泰輔,髙地　系治,難波　宏明,ナザリト",
"away_shoot": 9,
"home_director": "ラモス　瑠偉",
"away_team": "京都サンガF.C.",
"weather": "晴",
"series_number": 16,
"temperature": 26.4,
"away_score": 1,
"away_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,福村　貴幸,山瀬　功治,中山　博貴,工藤　浩平,駒井　善成,アレッサンドロ,大黒　将志",
"home_score": 2,
"home_shoot": 9,
"game_id": "16150",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/06/01 19:04",
"referee": "福島　孝一郎"
},
{
"teams": [
"ファジアーノ岡山",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "真子　秀徳,鎌田　翔雅,後藤　圭太,田所　諒,田中　奏一,島田　譲,上田　康太,三村　真,石原　崇兆,片山　瑛一,清水　慎太郎",
"away_shoot": 9,
"home_director": "影山　雅永",
"away_team": "松本山雅ＦＣ",
"weather": "晴",
"series_number": 17,
"temperature": 27.3,
"away_score": 0,
"away_start_member": "村山　智彦,多々良　敦斗,飯田　真輝,犬飼　智也,鐡戸　裕史,ユン　ソンヨル,岩上　祐三,田中　隼磨,岩沼　俊介,船山　貴之,サビア",
"home_score": 0,
"home_shoot": 16,
"game_id": "16152",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/06/07 13:03",
"referee": "榎本　一慶"
},
{
"teams": [
"カターレ富山",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "飯田　健巳,高　准翼,秋本　倫孝,池端　陽介,田中　寛己,國吉　貴博,木本　敬介,大西　容平,キム　ヨングン,中島　翔哉,三上　陽輔",
"away_shoot": 18,
"home_director": "安間　貴義",
"away_team": "湘南ベルマーレ",
"weather": "曇",
"series_number": 17,
"temperature": 25.8,
"away_score": 1,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,菊地　俊介,永木　亮太,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"home_score": 0,
"home_shoot": 13,
"game_id": "16151",
"home_team": "カターレ富山",
"game_start_at": "2014/06/07 13:04",
"referee": "井上　知大"
},
{
"teams": [
"モンテディオ山形",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "兼田　亜季重,山田　拓巳,當間　建文,イ　ジュヨン,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,秋葉　勝,中島　裕希,比嘉　厚平",
"away_shoot": 13,
"home_director": "石﨑　信弘",
"away_team": "栃木ＳＣ",
"weather": "曇",
"series_number": 17,
"temperature": 21.2,
"away_score": 1,
"away_start_member": "鈴木　智幸,山形　辰徳,赤井　秀行,ドゥドゥ,鈴木　隆雅,近藤　祐介,廣瀬　浩二,岡根　直哉,湯澤　洋介,重松　健太郎,瀬沼　優司",
"home_score": 6,
"home_shoot": 17,
"game_id": "16153",
"home_team": "モンテディオ山形",
"game_start_at": "2014/06/07 14:04",
"referee": "家本　政明"
},
{
"teams": [
"ジュビロ磐田",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "八田　直樹,駒野　友一,菅沼　駿哉,藤田　義明,宮崎　智彦,フェルジナンド,小林　祐希,松井　大輔,山崎　亮平,前田　遼一,ポポ",
"away_shoot": 9,
"home_director": "シャムスカ",
"away_team": "水戸ホーリーホック",
"weather": "晴",
"series_number": 17,
"temperature": 26.3,
"away_score": 0,
"away_start_member": "本間　幸司,新里　亮,金　聖基,尾本　敬,内田　航平,中里　崇宏,広瀬　陸斗,小澤　司,船谷　圭祐,馬場　賢治,三島　康平",
"home_score": 1,
"home_shoot": 15,
"game_id": "16154",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/06/07 14:04",
"referee": "窪田　陽輔"
},
{
"teams": [
"京都サンガF.C.",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,福村　貴幸,田森　大己,山瀬　功治,中山　博貴,工藤　浩平,大黒　将志,有田　光希",
"away_shoot": 9,
"home_director": "バドゥ",
"away_team": "東京ヴェルディ",
"weather": "曇のち晴",
"series_number": 17,
"temperature": 25.6,
"away_score": 0,
"away_start_member": "佐藤　優也,田中　貴大,金　鐘必,井林　章,安在　和樹,安西　幸輝,ニウド,田村　直也,鈴木　惇,菅嶋　弘希,常盤　聡",
"home_score": 1,
"home_shoot": 6,
"game_id": "16155",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/06/07 14:04",
"referee": "上田　益也"
},
{
"teams": [
"愛媛ＦＣ",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "児玉　剛,村上　佑介,代　健司,林堂　眞,西岡　大輝,ハン　ヒフン,村上　巧,原川　力,堀米　勇輝,西田　剛,河原　和寿",
"away_shoot": 7,
"home_director": "石丸　清隆",
"away_team": "ザスパクサツ群馬",
"weather": "晴",
"series_number": 17,
"temperature": 24.9,
"away_score": 2,
"away_start_member": "内藤　圭佑,小柳　達司,クォン　ハンジン,黄　誠秀,青木　良太,横山　翔平,坂井　洋平,宮崎　泰右,瀬川　和樹,ダニエル　ロビーニョ,小林　竜樹",
"home_score": 0,
"home_shoot": 18,
"game_id": "16156",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/06/07 14:04",
"referee": "池内　明彦"
},
{
"teams": [
"カマタマーレ讃岐",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "瀬口　拓弥,武田　有祐,ソン　ハンキ,藤井　航大,小澤　雄希,岡村　和哉,藤田　浩平,持留　新作,高木　和正,我那覇　和樹,高橋　泰",
"away_shoot": 12,
"home_director": "北野　誠",
"away_team": "コンサドーレ札幌",
"weather": "晴",
"series_number": 17,
"temperature": 27.7,
"away_score": 0,
"away_start_member": "金山　隼樹,上原　慎也,パウロン,奈良　竜樹,上原　拓郎,河合　竜二,宮澤　裕樹,荒野　拓馬,ヘナン,菊岡　拓朗,石井　謙伍",
"home_score": 1,
"home_shoot": 4,
"game_id": "16157",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/06/07 16:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"横浜ＦＣ",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "南　雄太,市村　篤司,ドウグラス,野上　結貴,西嶋　弘之,松下　裕樹,安　英学,小池　純輝,寺田　紳一,松下　年宏,黒津　勝",
"away_shoot": 10,
"home_director": "山口　素弘",
"away_team": "Ｖ・ファーレン長崎",
"weather": "雨",
"series_number": 17,
"temperature": 17.4,
"away_score": 2,
"away_start_member": "大久保　択生,下田　光平,山口　貴弘,髙杉　亮太,金久保　彩,前田　悠佑,井上　裕大,神崎　大輔,奥埜　博亮,東　浩史,佐藤　洸一",
"home_score": 1,
"home_shoot": 2,
"game_id": "16158",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/06/07 17:03",
"referee": "森川　浩次"
},
{
"teams": [
"アビスパ福岡",
"ジェフユナイテッド千葉"
],
"away_director": "鈴木　淳",
"home_start_member": "神山　竜一,阿部　巧,パク　ゴン,イ　グァンソン,古賀　正紘,堤　俊輔,三島　勇太,中原　秀人,石津　大介,酒井　宣福,金森　健志",
"away_shoot": 13,
"home_director": "マリヤン　プシュニク",
"away_team": "ジェフユナイテッド千葉",
"weather": "曇",
"series_number": 17,
"temperature": 21.3,
"away_score": 0,
"away_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,大塚　翔平,ケンペス",
"home_score": 1,
"home_shoot": 8,
"game_id": "16159",
"home_team": "アビスパ福岡",
"game_start_at": "2014/06/07 17:03",
"referee": "廣瀬　格"
},
{
"teams": [
"ギラヴァンツ北九州",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "大谷　幸輝,星原　健太,宮本　亨,寺岡　真弘,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"away_shoot": 13,
"home_director": "柱谷　幸一",
"away_team": "ロアッソ熊本",
"weather": "曇",
"series_number": 17,
"temperature": 21,
"away_score": 1,
"away_start_member": "畑　実,藏川　洋平,園田　拓也,篠原　弘次郎,片山　奨典,養父　雄仁,橋本　拳人,中山　雄登,齊藤　和樹,岡本　賢明,澤田　崇",
"home_score": 1,
"home_shoot": 8,
"game_id": "16160",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/06/07 17:03",
"referee": "三上　正一郎"
},
{
"teams": [
"大分トリニータ",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "武田　洋平,西　弘則,阪田　章裕,高木　和道,安川　有,伊藤　大介,末吉　隼也,松本　昌也,木村　祐志,風間　宏矢,後藤　優介",
"away_shoot": 11,
"home_director": "田坂　和昭",
"away_team": "ＦＣ岐阜",
"weather": "晴",
"series_number": 17,
"temperature": 23,
"away_score": 0,
"away_start_member": "川口　能活,益山　司,木谷　公亮,阿部　正紀,三都主　アレサンドロ,宮沢　正史,ヘニキ,太田　圭輔,髙地　系治,難波　宏明,ナザリト",
"home_score": 1,
"home_shoot": 6,
"game_id": "16161",
"home_team": "大分トリニータ",
"game_start_at": "2014/06/07 18:03",
"referee": "前田　拓哉"
},
{
"teams": [
"栃木ＳＣ",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "鈴木　智幸,山形　辰徳,チャ　ヨンファン,中野　洋司,赤井　秀行,近藤　祐介,小野寺　達也,西澤　代志也,湯澤　洋介,重松　健太郎,大久保　哲哉",
"away_shoot": 19,
"home_director": "阪倉　裕二",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 18,
"temperature": 29,
"away_score": 0,
"away_start_member": "武田　洋平,西　弘則,阪田　章裕,高木　和道,安川　有,伊藤　大介,末吉　隼也,松本　昌也,為田　大貴,風間　宏矢,木島　悠",
"home_score": 4,
"home_shoot": 13,
"game_id": "16162",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/06/14 13:03",
"referee": "岡　宏道"
},
{
"teams": [
"カターレ富山",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "飯田　健巳,池端　陽介,秋本　倫孝,御厨　貴文,木村　勝太,國吉　貴博,木本　敬介,キム　ヨングン,大西　容平,中島　翔哉,三上　陽輔",
"away_shoot": 13,
"home_director": "安間　貴義",
"away_team": "水戸ホーリーホック",
"weather": "晴",
"series_number": 18,
"temperature": 25.6,
"away_score": 3,
"away_start_member": "本間　幸司,新里　亮,金　聖基,尾本　敬,西岡　謙太,中里　崇宏,広瀬　陸斗,小澤　司,船谷　圭祐,吉田　眞紀人,鈴木　隆行",
"home_score": 0,
"home_shoot": 10,
"game_id": "16163",
"home_team": "カターレ富山",
"game_start_at": "2014/06/14 13:04",
"referee": "福島　孝一郎"
},
{
"teams": [
"愛媛ＦＣ",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "児玉　剛,ハン　ヒフン,代　健司,林堂　眞,西岡　大輝,村上　巧,吉村　圭司,堀米　勇輝,藤　直也,西田　剛,河原　和寿",
"away_shoot": 11,
"home_director": "石丸　清隆",
"away_team": "ファジアーノ岡山",
"weather": "曇",
"series_number": 18,
"temperature": 26.4,
"away_score": 3,
"away_start_member": "真子　秀徳,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,石原　崇兆,片山　瑛一,清水　慎太郎",
"home_score": 2,
"home_shoot": 11,
"game_id": "16165",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/06/14 13:04",
"referee": "井上　知大"
},
{
"teams": [
"ＦＣ岐阜",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "川口　能活,益山　司,阿部　正紀,木谷　公亮,三都主　アレサンドロ,太田　圭輔,宮沢　正史,ヘニキ,髙地　系治,難波　宏明,ナザリト",
"away_shoot": 14,
"home_director": "ラモス　瑠偉",
"away_team": "ジュビロ磐田",
"weather": "晴",
"series_number": 18,
"temperature": 30.8,
"away_score": 4,
"away_start_member": "八田　直樹,駒野　友一,藤田　義明,菅沼　駿哉,宮崎　智彦,フェルジナンド,小林　祐希,松井　大輔,山崎　亮平,前田　遼一,ポポ",
"home_score": 0,
"home_shoot": 8,
"game_id": "16164",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/06/14 13:05",
"referee": "岡部　拓人"
},
{
"teams": [
"東京ヴェルディ",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "佐藤　優也,安西　幸輝,金　鐘必,井林　章,安在　和樹,ニウド,田村　直也,安田　晃大,鈴木　惇,菅嶋　弘希,常盤　聡",
"away_shoot": 9,
"home_director": "三浦　泰年",
"away_team": "アビスパ福岡",
"weather": "晴",
"series_number": 18,
"temperature": 28.9,
"away_score": 5,
"away_start_member": "神山　竜一,阿部　巧,三島　勇太,イ　グァンソン,堤　俊輔,中原　秀人,パク　ゴン,武田　英二郎,金森　健志,酒井　宣福,城後　寿",
"home_score": 0,
"home_shoot": 10,
"game_id": "16166",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/06/14 14:04",
"referee": "塚田　健太"
},
{
"teams": [
"ザスパクサツ群馬",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "内藤　圭佑,小柳　達司,クォン　ハンジン,黄　誠秀,青木　良太,青木　孝太,坂井　洋平,宮崎　泰右,瀬川　和樹,ダニエル　ロビーニョ,小林　竜樹",
"away_shoot": 16,
"home_director": "秋葉　忠宏",
"away_team": "ロアッソ熊本",
"weather": "晴",
"series_number": 18,
"temperature": 26.5,
"away_score": 1,
"away_start_member": "畑　実,園田　拓也,篠原　弘次郎,矢野　大輔,片山　奨典,中山　雄登,橋本　拳人,澤田　崇,齊藤　和樹,岡本　賢明,巻　誠一郎",
"home_score": 1,
"home_shoot": 11,
"game_id": "16167",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/06/14 15:04",
"referee": "長谷　拓"
},
{
"teams": [
"横浜ＦＣ",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "南　雄太,市村　篤司,ドウグラス,野上　結貴,中島　崇典,松下　年宏,安　英学,寺田　紳一,野崎　陽介,黒津　勝,パク　ソンホ",
"away_shoot": 10,
"home_director": "山口　素弘",
"away_team": "コンサドーレ札幌",
"weather": "晴",
"series_number": 18,
"temperature": 26.3,
"away_score": 2,
"away_start_member": "金山　隼樹,上原　慎也,パウロン,奈良　竜樹,上原　拓郎,河合　竜二,上里　一将,荒野　拓馬,宮澤　裕樹,石井　謙伍,都倉　賢",
"home_score": 2,
"home_shoot": 8,
"game_id": "16168",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/06/14 16:03",
"referee": "野田　祐樹"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "大久保　択生,下田　光平,山口　貴弘,髙杉　亮太,金久保　彩,奥埜　博亮,前田　悠佑,神崎　大輔,東　浩史,佐藤　洸一,イ　デホン",
"away_shoot": 10,
"home_director": "高木　琢也",
"away_team": "モンテディオ山形",
"weather": "曇",
"series_number": 18,
"temperature": 25,
"away_score": 0,
"away_start_member": "兼田　亜季重,山田　拓巳,當間　建文,イ　ジュヨン,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,秋葉　勝,中島　裕希,比嘉　厚平",
"home_score": 0,
"home_shoot": 14,
"game_id": "16170",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/06/14 16:03",
"referee": "小屋　幸栄"
},
{
"teams": [
"湘南ベルマーレ",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,亀川　諒史,菊地　俊介,永木　亮太,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"away_shoot": 8,
"home_director": "曺　貴裁",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 18,
"temperature": 25.7,
"away_score": 1,
"away_start_member": "瀬口　拓弥,武田　有祐,ソン　ハンキ,藤井　航大,小澤　雄希,岡村　和哉,山本　翔平,持留　新作,我那覇　和樹,木島　良輔,高橋　泰",
"home_score": 3,
"home_shoot": 15,
"game_id": "16169",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/06/14 16:04",
"referee": "池内　明彦"
},
{
"teams": [
"ジェフユナイテッド千葉",
"京都サンガF.C."
],
"away_director": "バドゥ",
"home_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,大塚　翔平,ケンペス",
"away_shoot": 7,
"home_director": "鈴木　淳",
"away_team": "京都サンガF.C.",
"weather": "晴",
"series_number": 18,
"temperature": 24.6,
"away_score": 0,
"away_start_member": "オ　スンフン,酒井　隆介,バヤリッツァ,田森　大己,福村　貴幸,中山　博貴,工藤　浩平,山瀬　功治,三平　和司,横谷　繁,大黒　将志",
"home_score": 3,
"home_shoot": 20,
"game_id": "16171",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/06/14 19:03",
"referee": "木村　博之"
},
{
"teams": [
"松本山雅ＦＣ",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "村山　智彦,犬飼　智也,大久保　裕樹,飯田　真輝,田中　隼磨,ユン　ソンヨル,喜山　康平,岩沼　俊介,岩上　祐三,サビア,船山　貴之",
"away_shoot": 8,
"home_director": "反町　康治",
"away_team": "ギラヴァンツ北九州",
"weather": "晴",
"series_number": 18,
"temperature": 20,
"away_score": 1,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"home_score": 0,
"home_shoot": 17,
"game_id": "16172",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/06/14 19:03",
"referee": "河合　英治"
},
{
"teams": [
"コンサドーレ札幌",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "金山　隼樹,小山内　貴哉,パウロン,奈良　竜樹,上原　拓郎,河合　竜二,上里　一将,荒野　拓馬,宮澤　裕樹,砂川　誠,都倉　賢",
"away_shoot": 7,
"home_director": "財前　恵一",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 19,
"temperature": 20.1,
"away_score": 1,
"away_start_member": "飯田　健巳,池端　陽介,秋本　倫孝,高　准翼,木村　勝太,キム　ヨングン,大西　容平,田中　寛己,國吉　貴博,中島　翔哉,三上　陽輔",
"home_score": 2,
"home_shoot": 9,
"game_id": "16173",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/06/21 14:03",
"referee": "山本　雄大"
},
{
"teams": [
"水戸ホーリーホック",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "本間　幸司,新里　亮,金　聖基,尾本　敬,内田　航平,中里　崇宏,広瀬　陸斗,小澤　司,船谷　圭祐,吉田　眞紀人,三島　康平",
"away_shoot": 12,
"home_director": "柱谷　哲二",
"away_team": "アビスパ福岡",
"weather": "雨のち曇",
"series_number": 19,
"temperature": 21,
"away_score": 2,
"away_start_member": "神山　竜一,阿部　巧,堤　俊輔,パク　ゴン,イ　グァンソン,武田　英二郎,中原　秀人,三島　勇太,城後　寿,酒井　宣福,金森　健志",
"home_score": 1,
"home_shoot": 9,
"game_id": "16174",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/06/21 18:03",
"referee": "三上　正一郎"
},
{
"teams": [
"東京ヴェルディ",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "佐藤　優也,田村　直也,金　鐘必,井林　章,安在　和樹,ニウド,鈴木　惇,安西　幸輝,南　秀仁,永井　秀樹,平本　一樹",
"away_shoot": 13,
"home_director": "三浦　泰年",
"away_team": "栃木ＳＣ",
"weather": "曇",
"series_number": 19,
"temperature": 24.7,
"away_score": 1,
"away_start_member": "鈴木　智幸,山形　辰徳,チャ　ヨンファン,中野　洋司,赤井　秀行,近藤　祐介,小野寺　達也,西澤　代志也,湯澤　洋介,廣瀬　浩二,大久保　哲哉",
"home_score": 1,
"home_shoot": 12,
"game_id": "16175",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/06/21 18:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"松本山雅ＦＣ",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "村山　智彦,田中　隼磨,飯田　真輝,大久保　裕樹,犬飼　智也,岩沼　俊介,岩間　雄大,岩上　祐三,喜山　康平,サビア,船山　貴之",
"away_shoot": 8,
"home_director": "反町　康治",
"away_team": "ザスパクサツ群馬",
"weather": "曇",
"series_number": 19,
"temperature": 23.6,
"away_score": 1,
"away_start_member": "北　一真,小柳　達司,クォン　ハンジン,青木　良太,瀬川　和樹,青木　孝太,坂井　洋平,黄　誠秀,加藤　弘堅,宮崎　泰右,ダニエル　ロビーニョ",
"home_score": 3,
"home_shoot": 21,
"game_id": "16176",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/06/21 18:03",
"referee": "上田　益也"
},
{
"teams": [
"カマタマーレ讃岐",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "瀬口　拓弥,武田　有祐,岡村　和哉,藤井　航大,藤田　浩平,山本　翔平,綱田　大志,小澤　雄希,高木　和正,木島　良輔,持留　新作",
"away_shoot": 7,
"home_director": "北野　誠",
"away_team": "モンテディオ山形",
"weather": "雨",
"series_number": 19,
"temperature": 24,
"away_score": 3,
"away_start_member": "山岸　範宏,山田　拓巳,イ　ジュヨン,當間　建文,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,秋葉　勝,中島　裕希,比嘉　厚平",
"home_score": 0,
"home_shoot": 9,
"game_id": "16178",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/06/21 18:03",
"referee": "榎本　一慶"
},
{
"teams": [
"ギラヴァンツ北九州",
"ジェフユナイテッド千葉"
],
"away_director": "*** 千葉 9 ケンペスの警告は試合終了後の警告",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"away_shoot": 16,
"home_director": "鈴木　淳",
"away_team": "ジェフユナイテッド千葉",
"weather": "雨",
"series_number": 19,
"temperature": 20.6,
"away_score": 0,
"away_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,大塚　翔平,ケンペス",
"home_score": 1,
"home_shoot": 6,
"game_id": "16179",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/06/21 18:03",
"referee": "森川　浩次"
},
{
"teams": [
"ＦＣ岐阜",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "川口　能活,益山　司,阿部　正紀,木谷　公亮,三都主　アレサンドロ,ヘニキ,宮沢　正史,太田　圭輔,髙地　系治,美尾　敦,ナザリト",
"away_shoot": 7,
"home_director": "ラモス　瑠偉",
"away_team": "Ｖ・ファーレン長崎",
"weather": "曇",
"series_number": 19,
"temperature": 25,
"away_score": 1,
"away_start_member": "大久保　択生,下田　光平,山口　貴弘,髙杉　亮太,神崎　大輔,前田　悠佑,奥埜　博亮,石神　直哉,東　浩史,佐藤　洸一,イ　デホン",
"home_score": 1,
"home_shoot": 11,
"game_id": "16177",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/06/21 18:05",
"referee": "佐藤　隆治"
},
{
"teams": [
"ロアッソ熊本",
"京都サンガF.C."
],
"away_director": "森下　仁志",
"home_start_member": "畑　実,園田　拓也,篠原　弘次郎,矢野　大輔,片山　奨典,養父　雄仁,橋本　拳人,中山　雄登,齊藤　和樹,澤田　崇,巻　誠一郎",
"away_shoot": 16,
"home_director": "小野　剛",
"away_team": "京都サンガF.C.",
"weather": "雨",
"series_number": 19,
"temperature": 22.6,
"away_score": 4,
"away_start_member": "オ　スンフン,磐瀬　剛,酒井　隆介,バヤリッツァ,福村　貴幸,田森　大己,工藤　浩平,駒井　善成,田村　亮介,山瀬　功治,大黒　将志",
"home_score": 1,
"home_shoot": 7,
"game_id": "16182",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/06/21 19:03",
"referee": "吉田　寿光"
},
{
"teams": [
"大分トリニータ",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "武田　洋平,西　弘則,阪田　章裕,高木　和道,安川　有,末吉　隼也,伊藤　大介,松本　昌也,風間　宏矢,木島　悠,後藤　優介",
"away_shoot": 13,
"home_director": "田坂　和昭",
"away_team": "愛媛ＦＣ",
"weather": "屋内",
"series_number": 19,
"temperature": 20.6,
"away_score": 2,
"away_start_member": "児玉　剛,村上　佑介,林堂　眞,西岡　大輝,キム　ミンジェ,渡邊　一仁,吉村　圭司,堀米　勇輝,藤　直也,西田　剛,河原　和寿",
"home_score": 2,
"home_shoot": 14,
"game_id": "16183",
"home_team": "大分トリニータ",
"game_start_at": "2014/06/21 19:03",
"referee": "河合　英治"
},
{
"teams": [
"ジュビロ磐田",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "八田　直樹,駒野　友一,藤田　義明,菅沼　駿哉,宮崎　智彦,フェルジナンド,小林　祐希,松井　大輔,山崎　亮平,前田　遼一,ポポ",
"away_shoot": 16,
"home_director": "シャムスカ",
"away_team": "湘南ベルマーレ",
"weather": "曇",
"series_number": 19,
"temperature": 23.3,
"away_score": 2,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,菊池　大介,菊地　俊介,永木　亮太,亀川　諒史,岡田　翔平,ウェリントン,武富　孝介",
"home_score": 1,
"home_shoot": 9,
"game_id": "16180",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/06/21 19:04",
"referee": "東城　穣"
},
{
"teams": [
"ファジアーノ岡山",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "椎名　一馬,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,石原　崇兆,片山　瑛一,清水　慎太郎",
"away_shoot": 11,
"home_director": "影山　雅永",
"away_team": "横浜ＦＣ",
"weather": "雨",
"series_number": 19,
"temperature": 22.6,
"away_score": 0,
"away_start_member": "南　雄太,市村　篤司,野上　結貴,ドウグラス,中島　崇典,松下　裕樹,安　英学,寺田　紳一,小池　純輝,黒津　勝,パク　ソンホ",
"home_score": 0,
"home_shoot": 10,
"game_id": "16181",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/06/21 19:04",
"referee": "高山　啓義"
},
{
"teams": [
"コンサドーレ札幌",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "金山　隼樹,小山内　貴哉,櫛引　一紀,奈良　竜樹,上原　拓郎,河合　竜二,上里　一将,荒野　拓馬,宮澤　裕樹,砂川　誠,都倉　賢",
"away_shoot": 8,
"home_director": "財前　恵一",
"away_team": "ＦＣ岐阜",
"weather": "曇のち晴",
"series_number": 20,
"temperature": 23.1,
"away_score": 2,
"away_start_member": "川口　能活,益山　司,木谷　公亮,阿部　正紀,三都主　アレサンドロ,宮沢　正史,ヘニキ,難波　宏明,髙地　系治,美尾　敦,ナザリト",
"home_score": 3,
"home_shoot": 13,
"game_id": "16184",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/06/28 14:03",
"referee": "扇谷　健司"
},
{
"teams": [
"横浜ＦＣ",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "南　雄太,市村　篤司,野上　結貴,ドウグラス,中島　崇典,松下　裕樹,寺田　紳一,小池　純輝,内田　智也,黒津　勝,パク　ソンホ",
"away_shoot": 7,
"home_director": "山口　素弘",
"away_team": "東京ヴェルディ",
"weather": "雨時々曇",
"series_number": 20,
"temperature": 22.3,
"away_score": 0,
"away_start_member": "佐藤　優也,田村　直也,金　鐘必,井林　章,安在　和樹,ニウド,鈴木　惇,前田　直輝,南　秀仁,永井　秀樹,平本　一樹",
"home_score": 0,
"home_shoot": 9,
"game_id": "16186",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/06/28 18:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"カマタマーレ讃岐",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "瀬口　拓弥,波夛野　寛,岡村　和哉,藤井　航大,武田　有祐,山本　翔平,高木　和正,小澤　雄希,西野　泰正,木島　良輔,高橋　泰",
"away_shoot": 8,
"home_director": "北野　誠",
"away_team": "水戸ホーリーホック",
"weather": "曇",
"series_number": 20,
"temperature": 25.9,
"away_score": 0,
"away_start_member": "本間　幸司,新里　亮,金　聖基,尾本　敬,西岡　謙太,中里　崇宏,広瀬　陸斗,小澤　司,船谷　圭祐,吉田　眞紀人,三島　康平",
"home_score": 0,
"home_shoot": 6,
"game_id": "16188",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/06/28 18:03",
"referee": "塚田　健太"
},
{
"teams": [
"アビスパ福岡",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "神山　竜一,阿部　巧,堤　俊輔,パク　ゴン,イ　グァンソン,中原　秀人,石津　大介,武田　英二郎,金森　健志,城後　寿,酒井　宣福",
"away_shoot": 11,
"home_director": "マリヤン　プシュニク",
"away_team": "栃木ＳＣ",
"weather": "曇",
"series_number": 20,
"temperature": 23.9,
"away_score": 0,
"away_start_member": "鈴木　智幸,山形　辰徳,チャ　ヨンファン,岡根　直哉,赤井　秀行,近藤　祐介,西澤　代志也,小野寺　達也,湯澤　洋介,廣瀬　浩二,大久保　哲哉",
"home_score": 2,
"home_shoot": 11,
"game_id": "16189",
"home_team": "アビスパ福岡",
"game_start_at": "2014/06/28 18:03",
"referee": "野田　祐樹"
},
{
"teams": [
"モンテディオ山形",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "山岸　範宏,山田　拓巳,當間　建文,イ　ジュヨン,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,秋葉　勝,中島　裕希,伊東　俊",
"away_shoot": 11,
"home_director": "石﨑　信弘",
"away_team": "ジュビロ磐田",
"weather": "曇",
"series_number": 20,
"temperature": 23.2,
"away_score": 1,
"away_start_member": "八田　直樹,駒野　友一,藤田　義明,菅沼　駿哉,宮崎　智彦,岡田　隆,小林　祐希,松井　大輔,山田　大記,山崎　亮平,前田　遼一",
"home_score": 0,
"home_shoot": 13,
"game_id": "16185",
"home_team": "モンテディオ山形",
"game_start_at": "2014/06/28 18:04",
"referee": "今村　義朗"
},
{
"teams": [
"カターレ富山",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "飯田　健巳,木村　勝太,平出　涼,御厨　貴文,高　准翼,白崎　凌兵,キム　ヨングン,大西　容平,内田　健太,中島　翔哉,三上　陽輔",
"away_shoot": 9,
"home_director": "安間　貴義",
"away_team": "Ｖ・ファーレン長崎",
"weather": "雨",
"series_number": 20,
"temperature": 21.4,
"away_score": 0,
"away_start_member": "大久保　択生,下田　光平,山口　貴弘,髙杉　亮太,神崎　大輔,奥埜　博亮,前田　悠佑,野田　紘史,深井　正樹,東　浩史,佐藤　洸一",
"home_score": 1,
"home_shoot": 15,
"game_id": "16187",
"home_team": "カターレ富山",
"game_start_at": "2014/06/28 18:04",
"referee": "前田　拓哉"
},
{
"teams": [
"ジェフユナイテッド千葉",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,大塚　翔平,ケンペス",
"away_shoot": 8,
"home_director": "斉藤　和夫",
"away_team": "松本山雅ＦＣ",
"weather": "曇のち雨",
"series_number": 20,
"temperature": 22.8,
"away_score": 1,
"away_start_member": "村山　智彦,岩沼　俊介,飯田　真輝,犬飼　智也,大久保　裕樹,喜山　康平,田中　隼磨,岩間　雄大,サビア,岩上　祐三,船山　貴之",
"home_score": 0,
"home_shoot": 22,
"game_id": "16190",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/06/28 19:03",
"referee": "松尾　一"
},
{
"teams": [
"湘南ベルマーレ",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,亀川　諒史,藤田　征也,菊地　俊介,岩尾　憲,菊池　大介,吉濱　遼平,岡田　翔平,武富　孝介",
"away_shoot": 6,
"home_director": "曺　貴裁",
"away_team": "ギラヴァンツ北九州",
"weather": "雨",
"series_number": 20,
"temperature": 22.2,
"away_score": 0,
"away_start_member": "大谷　幸輝,星原　健太,前田　和哉,市川　恵多,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"home_score": 2,
"home_shoot": 13,
"game_id": "16191",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/06/28 19:04",
"referee": "飯田　淳平"
},
{
"teams": [
"京都サンガF.C.",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "オ　スンフン,駒井　善成,酒井　隆介,内野　貴志,福村　貴幸,工藤　浩平,田森　大己,中山　博貴,田村　亮介,山瀬　功治,大黒　将志",
"away_shoot": 9,
"home_director": "森下　仁志",
"away_team": "ファジアーノ岡山",
"weather": "曇",
"series_number": 20,
"temperature": 24.4,
"away_score": 1,
"away_start_member": "椎名　一馬,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,石原　崇兆,片山　瑛一,清水　慎太郎",
"home_score": 1,
"home_shoot": 6,
"game_id": "16192",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/06/28 19:04",
"referee": "村上　伸次"
},
{
"teams": [
"愛媛ＦＣ",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "児玉　剛,村上　佑介,林堂　眞,西岡　大輝,キム　ミンジェ,渡邊　一仁,吉村　圭司,堀米　勇輝,藤　直也,西田　剛,河原　和寿",
"away_shoot": 4,
"home_director": "石丸　清隆",
"away_team": "ロアッソ熊本",
"weather": "曇",
"series_number": 20,
"temperature": 23.6,
"away_score": 0,
"away_start_member": "畑　実,園田　拓也,篠原　弘次郎,矢野　大輔,藏川　洋平,橋本　拳人,養父　雄仁,中山　雄登,齊藤　和樹,藤本　主税,澤田　崇",
"home_score": 4,
"home_shoot": 11,
"game_id": "16193",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/06/28 19:04",
"referee": "岡　宏道"
},
{
"teams": [
"ザスパクサツ群馬",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "内藤　圭佑,小柳　達司,クォン　ハンジン,青木　良太,青木　孝太,坂井　洋平,加藤　弘堅,瀬川　和樹,永田　亮太,ダニエル　ロビーニョ,宮崎　泰右",
"away_shoot": 13,
"home_director": "秋葉　忠宏",
"away_team": "大分トリニータ",
"weather": "曇のち雨",
"series_number": 20,
"temperature": 21.9,
"away_score": 1,
"away_start_member": "武田　洋平,安川　有,高木　和道,阪田　章裕,岩武　克弥,伊藤　大介,末吉　隼也,松本　昌也,西　弘則,風間　宏矢,後藤　優介",
"home_score": 2,
"home_shoot": 9,
"game_id": "16194",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/06/28 19:34",
"referee": "小屋　幸栄"
},
{
"teams": [
"栃木ＳＣ",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "鈴木　智幸,山形　辰徳,チャ　ヨンファン,岡根　直哉,中野　洋司,近藤　祐介,西澤　代志也,小野寺　達也,湯澤　洋介,廣瀬　浩二,瀬沼　優司",
"away_shoot": 9,
"home_director": "阪倉　裕二",
"away_team": "カターレ富山",
"weather": "曇",
"series_number": 21,
"temperature": 22.4,
"away_score": 1,
"away_start_member": "飯田　健巳,御厨　貴文,秋本　倫孝,高　准翼,木村　勝太,キム　ヨングン,大西　容平,内田　健太,白崎　凌兵,三上　陽輔,中島　翔哉",
"home_score": 2,
"home_shoot": 14,
"game_id": "16195",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/07/05 18:03",
"referee": "河合　英治"
},
{
"teams": [
"東京ヴェルディ",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "佐藤　優也,田中　貴大,金　鐘必,井林　章,安在　和樹,ニウド,鈴木　惇,安西　幸輝,南　秀仁,永井　秀樹,平本　一樹",
"away_shoot": 15,
"home_director": "三浦　泰年",
"away_team": "モンテディオ山形",
"weather": "曇",
"series_number": 21,
"temperature": 22.7,
"away_score": 2,
"away_start_member": "山岸　範宏,山田　拓巳,イ　ジュヨン,當間　建文,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,秋葉　勝,中島　裕希,伊東　俊",
"home_score": 1,
"home_shoot": 8,
"game_id": "16196",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/07/05 18:03",
"referee": "森川　浩次"
},
{
"teams": [
"横浜ＦＣ",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "南　雄太,市村　篤司,野上　結貴,ドウグラス,中島　崇典,松下　裕樹,安　英学,松下　年宏,内田　智也,黒津　勝,小野瀬　康介",
"away_shoot": 8,
"home_director": "山口　素弘",
"away_team": "水戸ホーリーホック",
"weather": "曇",
"series_number": 21,
"temperature": 22.1,
"away_score": 1,
"away_start_member": "笠原　昂史,新里　亮,冨田　大介,尾本　敬,内田　航平,西岡　謙太,鈴木　雄斗,小澤　司,船谷　圭祐,三島　康平,馬場　賢治",
"home_score": 1,
"home_shoot": 11,
"game_id": "16197",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/07/05 18:03",
"referee": "榎本　一慶"
},
{
"teams": [
"松本山雅ＦＣ",
"アビスパ福岡"
],
"away_director": "*** 福岡 7 平井　将生の警告は試合終了後の警告",
"home_start_member": "村山　智彦,犬飼　智也,飯田　真輝,大久保　裕樹,喜山　康平,田中　隼磨,岩間　雄大,岩上　祐三,岩沼　俊介,船山　貴之,サビア",
"away_shoot": 18,
"home_director": "マリヤン　プシュニク",
"away_team": "アビスパ福岡",
"weather": "晴のち曇",
"series_number": 21,
"temperature": 23.4,
"away_score": 1,
"away_start_member": "神山　竜一,阿部　巧,三島　勇太,イ　グァンソン,堤　俊輔,パク　ゴン,武田　英二郎,中原　秀人,酒井　宣福,金森　健志,城後　寿",
"home_score": 2,
"home_shoot": 15,
"game_id": "16198",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/07/05 18:03",
"referee": "村上　伸次"
},
{
"teams": [
"ギラヴァンツ北九州",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,鈴木　修人,八角　剛史,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"away_shoot": 14,
"home_director": "柱谷　幸一",
"away_team": "愛媛ＦＣ",
"weather": "曇",
"series_number": 21,
"temperature": 22.7,
"away_score": 3,
"away_start_member": "児玉　剛,村上　佑介,ハン　ヒフン,西岡　大輝,キム　ミンジェ,渡邊　一仁,吉村　圭司,堀米　勇輝,藤　直也,西田　剛,河原　和寿",
"home_score": 0,
"home_shoot": 7,
"game_id": "16199",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/07/05 18:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "大久保　択生,下田　光平,山口　貴弘,髙杉　亮太,神崎　大輔,碓井　鉄平,奥埜　博亮,野田　紘史,深井　正樹,佐藤　洸一,イ　デホン",
"away_shoot": 6,
"home_director": "高木　琢也",
"away_team": "コンサドーレ札幌",
"weather": "曇",
"series_number": 21,
"temperature": 24.6,
"away_score": 1,
"away_start_member": "金山　隼樹,小山内　貴哉,櫛引　一紀,奈良　竜樹,上原　拓郎,河合　竜二,上里　一将,荒野　拓馬,宮澤　裕樹,砂川　誠,内村　圭宏",
"home_score": 0,
"home_shoot": 6,
"game_id": "16200",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/07/05 18:04",
"referee": "飯田　淳平"
},
{
"teams": [
"ファジアーノ岡山",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "椎名　一馬,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,片山　瑛一,押谷　祐樹,久保　裕一",
"away_shoot": 11,
"home_director": "影山　雅永",
"away_team": "カマタマーレ讃岐",
"weather": "曇",
"series_number": 21,
"temperature": 25.4,
"away_score": 2,
"away_start_member": "瀬口　拓弥,武田　有祐,岡村　和哉,西野　泰正,沼田　圭悟,関原　凌河,山本　翔平,大沢　朋也,小澤　雄希,木島　良輔,高木　和正",
"home_score": 2,
"home_shoot": 11,
"game_id": "16202",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/07/05 19:03",
"referee": "三上　正一郎"
},
{
"teams": [
"ロアッソ熊本",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "畑　実,大迫　希,篠原　弘次郎,園田　拓也,片山　奨典,黒木　晃平,養父　雄仁,橋本　拳人,キム　ジョンソク,齊藤　和樹,澤田　崇",
"away_shoot": 8,
"home_director": "小野　剛",
"away_team": "ＦＣ岐阜",
"weather": "曇",
"series_number": 21,
"temperature": 24.6,
"away_score": 3,
"away_start_member": "時久　省吾,益山　司,阿部　正紀,関田　寛士,野垣内　俊,比嘉　諒人,ヘニキ,水野　泰輔,髙地　系治,難波　宏明,遠藤　純輝",
"home_score": 0,
"home_shoot": 8,
"game_id": "16203",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/07/05 19:03",
"referee": "木村　博之"
},
{
"teams": [
"大分トリニータ",
"ジェフユナイテッド千葉"
],
"away_director": "斉藤　和夫",
"home_start_member": "室　拓哉,若狭　大志,阪田　章裕,高木　和道,安川　有,末吉　隼也,伊藤　大介,松本　昌也,松本　怜,風間　宏矢,高松　大樹",
"away_shoot": 13,
"home_director": "田坂　和昭",
"away_team": "ジェフユナイテッド千葉",
"weather": "曇",
"series_number": 21,
"temperature": 24.1,
"away_score": 4,
"away_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,田中　佑昌,大塚　翔平,森本　貴幸,ケンペス",
"home_score": 2,
"home_shoot": 13,
"game_id": "16204",
"home_team": "大分トリニータ",
"game_start_at": "2014/07/05 19:03",
"referee": "家本　政明"
},
{
"teams": [
"京都サンガF.C.",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,駒井　善成,田森　大己,工藤　浩平,中山　博貴,山瀬　功治,田村　亮介,大黒　将志",
"away_shoot": 8,
"home_director": "川勝　良一",
"away_team": "ジュビロ磐田",
"weather": "曇",
"series_number": 21,
"temperature": 25.4,
"away_score": 3,
"away_start_member": "八田　直樹,駒野　友一,藤田　義明,伊野波　雅彦,宮崎　智彦,フェルジナンド,小林　祐希,松井　大輔,ペク　ソンドン,前田　遼一,山崎　亮平",
"home_score": 2,
"home_shoot": 5,
"game_id": "16201",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/07/05 19:04",
"referee": "扇谷　健司"
},
{
"teams": [
"ザスパクサツ群馬",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "内藤　圭佑,小柳　達司,クォン　ハンジン,青木　良太,青木　孝太,坂井　洋平,加藤　弘堅,瀬川　和樹,夛田　凌輔,ダニエル　ロビーニョ,宮崎　泰右",
"away_shoot": 21,
"home_director": "秋葉　忠宏",
"away_team": "湘南ベルマーレ",
"weather": "曇",
"series_number": 21,
"temperature": 22.6,
"away_score": 1,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,島村　毅,岩尾　憲,菊地　俊介,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"home_score": 0,
"home_shoot": 8,
"game_id": "16205",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/07/05 19:34",
"referee": "前田　拓哉"
},
{
"teams": [
"サンフレッチェ広島",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,柏　好文,柴﨑　晃誠,森﨑　和幸,山岸　智,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"away_shoot": 9,
"home_director": "森保　一",
"away_team": "横浜Ｆ・マリノス",
"weather": "晴",
"series_number": 12,
"temperature": 25.1,
"away_score": 2,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,小椋　祥平,藤本　淳吾,中村　俊輔,齋藤　学,伊藤　翔",
"home_score": 1,
"home_shoot": 10,
"game_id": "15775",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/07/15 19:04",
"referee": "木村　博之"
},
{
"teams": [
"セレッソ大阪",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "キム　ジンヒョン,藤本　康太,丸橋　祐介,酒本　憲幸,山下　達也,扇原　貴宏,山口　蛍,楠神　順平,南野　拓実,安藤　淳,杉本　健勇",
"away_shoot": 11,
"home_director": "マルコ　ペッツァイオリ",
"away_team": "川崎フロンターレ",
"weather": "晴",
"series_number": 12,
"temperature": 29.9,
"away_score": 2,
"away_start_member": "杉山　力裕,田中　裕介,ジェシ,谷口　彰悟,小宮山　尊信,大島　僚太,中村　憲剛,森谷　賢太郎,登里　享平,小林　悠,大久保　嘉人",
"home_score": 1,
"home_shoot": 17,
"game_id": "15776",
"home_team": "セレッソ大阪",
"game_start_at": "2014/07/15 19:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"浦和レッズ",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,青木　拓矢,阿部　勇樹,宇賀神　友弥,柏木　陽介,梅崎　司,興梠　慎三",
"away_shoot": 14,
"home_director": "ペトロヴィッチ",
"away_team": "アルビレックス新潟",
"weather": "雨",
"series_number": 15,
"temperature": 23.2,
"away_score": 0,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,大野　和成,レオ　シルバ,小林　裕紀,山本　康裕,田中　亜土夢,鈴木　武蔵,岡本　英也",
"home_score": 1,
"home_shoot": 6,
"game_id": "15795",
"home_team": "浦和レッズ",
"game_start_at": "2014/07/19 18:04",
"referee": "扇谷　健司"
},
{
"teams": [
"清水エスパルス",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "相澤　貴志,ヤコヴィッチ,平岡　康裕,杉山　浩太,吉田　豊,本田　拓也,六平　光成,河井　陽介,大前　元紀,ノヴァコヴィッチ,高木　俊幸",
"away_shoot": 8,
"home_director": "アフシン　ゴトビ",
"away_team": "川崎フロンターレ",
"weather": "曇のち雨",
"series_number": 15,
"temperature": 21.4,
"away_score": 2,
"away_start_member": "杉山　力裕,小宮山　尊信,實藤　友紀,谷口　彰悟,登里　享平,大島　僚太,中村　憲剛,森谷　賢太郎,金久保　順,小林　悠,大久保　嘉人",
"home_score": 0,
"home_shoot": 8,
"game_id": "15799",
"home_team": "清水エスパルス",
"game_start_at": "2014/07/19 18:04",
"referee": "家本　政明"
},
{
"teams": [
"ＦＣ東京",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,三田　啓貴,河野　広貴,エドゥー,武藤　嘉紀",
"away_shoot": 13,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "鹿島アントラーズ",
"weather": "曇一時雨",
"series_number": 15,
"temperature": 24.1,
"away_score": 1,
"away_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,ダヴィ",
"home_score": 1,
"home_shoot": 6,
"game_id": "15798",
"home_team": "ＦＣ東京",
"game_start_at": "2014/07/19 18:34",
"referee": "山本　雄大"
},
{
"teams": [
"大宮アルディージャ",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "江角　浩司,渡部　大輔,菊地　光将,今井　智基,高橋　祥平,橋本　晃司,和田　拓也,渡邉　大剛,富山　貴光,家長　昭博,ズラタン",
"away_shoot": 9,
"home_director": "大熊　清",
"away_team": "サンフレッチェ広島",
"weather": "雨",
"series_number": 15,
"temperature": 23.3,
"away_score": 3,
"away_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,清水　航平,青山　敏弘,森﨑　和幸,山岸　智,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"home_score": 3,
"home_shoot": 9,
"game_id": "15796",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/07/19 19:04",
"referee": "福島　孝一郎"
},
{
"teams": [
"名古屋グランパス",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "楢﨑　正剛,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,矢野　貴章,ダニルソン,田口　泰士,佐藤　和樹,レアンドロ　ドミンゲス,永井　謙佑,小川　佳純",
"away_shoot": 5,
"home_director": "西野　朗",
"away_team": "徳島ヴォルティス",
"weather": "曇",
"series_number": 15,
"temperature": 23.3,
"away_score": 1,
"away_start_member": "長谷川　徹,藤原　広太朗,福元　洋平,村松　大輔,アレックス,斉藤　大介,濱田　武,衛藤　裕,大﨑　淳矢,宮崎　光平,高崎　寛之",
"home_score": 1,
"home_shoot": 13,
"game_id": "15800",
"home_team": "名古屋グランパス",
"game_start_at": "2014/07/19 19:04",
"referee": "村上　伸次"
},
{
"teams": [
"ガンバ大阪",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "東口　順昭,米倉　恒貴,西野　貴治,岩下　敬輔,オ　ジェソク,今野　泰幸,遠藤　保仁,阿部　浩之,大森　晃太郎,宇佐美　貴史,倉田　秋",
"away_shoot": 10,
"home_director": "長谷川　健太",
"away_team": "ヴァンフォーレ甲府",
"weather": "曇のち晴",
"series_number": 15,
"temperature": 24.6,
"away_score": 0,
"away_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,福田　健介,稲垣　祥,マルキーニョス　パラナ,阿部　翔平,ジウシーニョ,盛田　剛平,クリスティアーノ",
"home_score": 2,
"home_shoot": 3,
"game_id": "15801",
"home_team": "ガンバ大阪",
"game_start_at": "2014/07/19 19:04",
"referee": "松尾　一"
},
{
"teams": [
"セレッソ大阪",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "キム　ジンヒョン,染谷　悠太,丸橋　祐介,酒本　憲幸,山下　達也,扇原　貴宏,山口　蛍,安藤　淳,平野　甲斐,キム　ソンジュン,杉本　健勇",
"away_shoot": 14,
"home_director": "マルコ　ペッツァイオリ",
"away_team": "横浜Ｆ・マリノス",
"weather": "晴",
"series_number": 15,
"temperature": 27.5,
"away_score": 2,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,小椋　祥平,兵藤　慎剛,中村　俊輔,齋藤　学,伊藤　翔",
"home_score": 2,
"home_shoot": 13,
"game_id": "15802",
"home_team": "セレッソ大阪",
"game_start_at": "2014/07/19 19:04",
"referee": "中村　太"
},
{
"teams": [
"ヴィッセル神戸",
"サガン鳥栖"
],
"away_director": "尹　晶煥",
"home_start_member": "山本　海人,高橋　峻希,岩波　拓也,増川　隆洋,茂木　弘人,チョン　ウヨン,シンプリシオ,ペドロ　ジュニオール,森岡　亮太,小川　慶治朗,マルキーニョス",
"away_shoot": 11,
"home_director": "安達　亮",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 15,
"temperature": 27,
"away_score": 1,
"away_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,早坂　良太,岡本　知剛,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 0,
"home_shoot": 18,
"game_id": "15803",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/07/19 19:04",
"referee": "木村　博之"
},
{
"teams": [
"柏レイソル",
"ベガルタ仙台"
],
"away_director": "雷雨のため60分遅延",
"home_start_member": "菅野　孝憲,鈴木　大輔,増嶋　竜也,渡部　博文,橋本　和,キム　チャンス,ハン　グギョン,大谷　秀和,茨田　陽生,レアンドロ,工藤　壮人",
"away_shoot": 7,
"home_director": "渡邉　晋",
"away_team": "ベガルタ仙台",
"weather": "雨のち曇",
"series_number": 15,
"temperature": 21.2,
"away_score": 0,
"away_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,角田　誠,石川　直樹,太田　吉彰,富田　晋伍,武井　択也,八反田　康平,赤嶺　真吾,柳沢　敦",
"home_score": 0,
"home_shoot": 12,
"game_id": "15797",
"home_team": "柏レイソル",
"game_start_at": "2014/07/19 20:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"コンサドーレ札幌",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "金山　隼樹,小山内　貴哉,櫛引　一紀,奈良　竜樹,上原　慎也,河合　竜二,上里　一将,荒野　拓馬,宮澤　裕樹,小野　伸二,内村　圭宏",
"away_shoot": 15,
"home_director": "財前　恵一",
"away_team": "大分トリニータ",
"weather": "屋内",
"series_number": 22,
"temperature": 24.6,
"away_score": 1,
"away_start_member": "武田　洋平,阪田　章裕,高木　和道,若狭　大志,土岐田　洸平,伊藤　大介,末吉　隼也,松本　昌也,為田　大貴,風間　宏矢,ラドンチッチ",
"home_score": 1,
"home_shoot": 15,
"game_id": "16206",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/07/20 14:03",
"referee": "吉田　寿光"
},
{
"teams": [
"水戸ホーリーホック",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "笠原　昂史,新里　亮,冨田　大介,田中　雄大,小澤　司,中里　崇宏,広瀬　陸斗,小谷野　顕治,鈴木　雄斗,船谷　圭祐,鈴木　隆行",
"away_shoot": 14,
"home_director": "柱谷　哲二",
"away_team": "ザスパクサツ群馬",
"weather": "晴時々曇",
"series_number": 22,
"temperature": 22.9,
"away_score": 0,
"away_start_member": "富居　大樹,小柳　達司,クォン　ハンジン,青木　良太,瀬川　和樹,坂井　洋平,加藤　弘堅,永田　亮太,青木　孝太,ダニエル　ロビーニョ,宮崎　泰右",
"home_score": 2,
"home_shoot": 11,
"game_id": "16208",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/07/20 18:03",
"referee": "塚田　智宏"
},
{
"teams": [
"栃木ＳＣ",
"ジェフユナイテッド千葉"
],
"away_director": "関塚　隆",
"home_start_member": "鈴木　智幸,山形　辰徳,チャ　ヨンファン,岡根　直哉,赤井　秀行,近藤　祐介,西澤　代志也,菅　和範,湯澤　洋介,廣瀬　浩二,瀬沼　優司",
"away_shoot": 9,
"home_director": "阪倉　裕二",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 22,
"temperature": 22.9,
"away_score": 2,
"away_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,ケンペス,森本　貴幸",
"home_score": 0,
"home_shoot": 11,
"game_id": "16209",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/07/20 18:03",
"referee": "廣瀬　格"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "大久保　択生,下田　光平,山口　貴弘,髙杉　亮太,神崎　大輔,三原　雅俊,前田　悠佑,古部　健太,奥埜　博亮,佐藤　洸一,イ　ヨンジェ",
"away_shoot": 6,
"home_director": "高木　琢也",
"away_team": "松本山雅ＦＣ",
"weather": "晴のち曇",
"series_number": 22,
"temperature": 28.3,
"away_score": 2,
"away_start_member": "村山　智彦,多々良　敦斗,飯田　真輝,犬飼　智也,田中　隼磨,岩沼　俊介,岩間　雄大,岩上　祐三,喜山　康平,サビア,船山　貴之",
"home_score": 0,
"home_shoot": 9,
"game_id": "16213",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/07/20 18:03",
"referee": "高山　啓義"
},
{
"teams": [
"モンテディオ山形",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "山岸　範宏,當間　建文,イ　ジュヨン,石井　秀典,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,秋葉　勝,中島　裕希,伊東　俊",
"away_shoot": 11,
"home_director": "石﨑　信弘",
"away_team": "ギラヴァンツ北九州",
"weather": "晴",
"series_number": 22,
"temperature": 22.9,
"away_score": 2,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,渡　大生",
"home_score": 1,
"home_shoot": 8,
"game_id": "16207",
"home_team": "モンテディオ山形",
"game_start_at": "2014/07/20 18:04",
"referee": "岡　宏道"
},
{
"teams": [
"ＦＣ岐阜",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "川口　能活,益山　司,阿部　正紀,木谷　公亮,田中　秀人,ヘニキ,宮沢　正史,遠藤　純輝,髙地　系治,難波　宏明,ナザリト",
"away_shoot": 3,
"home_director": "ラモス　瑠偉",
"away_team": "横浜ＦＣ",
"weather": "曇",
"series_number": 22,
"temperature": 26.3,
"away_score": 2,
"away_start_member": "南　雄太,市村　篤司,ドウグラス,野上　結貴,永田　拓也,寺田　紳一,松下　裕樹,内田　智也,松下　年宏,黒津　勝,小野瀬　康介",
"home_score": 1,
"home_shoot": 11,
"game_id": "16211",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/07/20 18:04",
"referee": "前田　拓哉"
},
{
"teams": [
"アビスパ福岡",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "神山　竜一,阿部　巧,パク　ゴン,イ　グァンソン,堤　俊輔,中原　秀人,武田　英二郎,酒井　宣福,坂田　大輔,城後　寿,石津　大介",
"away_shoot": 15,
"home_director": "マリヤン　プシュニク",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 22,
"temperature": 27,
"away_score": 3,
"away_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,片山　瑛一,石原　崇兆,久保　裕一",
"home_score": 2,
"home_shoot": 10,
"game_id": "16212",
"home_team": "アビスパ福岡",
"game_start_at": "2014/07/20 18:04",
"referee": "吉田　哲朗"
},
{
"teams": [
"カターレ富山",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "飯田　健巳,御厨　貴文,秋本　倫孝,吉川　拓也,木村　勝太,田中　寛己,大山　俊輔,内田　健太,白崎　凌兵,中島　翔哉,苔口　卓也",
"away_shoot": 11,
"home_director": "安間　貴義",
"away_team": "カマタマーレ讃岐",
"weather": "曇",
"series_number": 22,
"temperature": 25.5,
"away_score": 1,
"away_start_member": "森田　耕一郎,武田　有祐,藤井　航大,西野　泰正,沼田　圭悟,岡村　和哉,エブソン,関原　凌河,大沢　朋也,小澤　雄希,木島　良輔",
"home_score": 1,
"home_shoot": 11,
"game_id": "16210",
"home_team": "カターレ富山",
"game_start_at": "2014/07/20 18:05",
"referee": "長谷　拓"
},
{
"teams": [
"湘南ベルマーレ",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,亀川　諒史,菊地　俊介,岩尾　憲,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"away_shoot": 11,
"home_director": "曺　貴裁",
"away_team": "ロアッソ熊本",
"weather": "曇",
"series_number": 22,
"temperature": 24.3,
"away_score": 1,
"away_start_member": "畑　実,大迫　希,園田　拓也,橋本　拳人,片山　奨典,上村　周平,養父　雄仁,黒木　晃平,中山　雄登,齊藤　和樹,澤田　崇",
"home_score": 2,
"home_shoot": 9,
"game_id": "16214",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/07/20 19:04",
"referee": "塚田　健太"
},
{
"teams": [
"ジュビロ磐田",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "八田　直樹,駒野　友一,藤田　義明,伊野波　雅彦,宮崎　智彦,フェルジナンド,小林　祐希,松井　大輔,山崎　亮平,金園　英学,ポポ",
"away_shoot": 18,
"home_director": "シャムスカ",
"away_team": "東京ヴェルディ",
"weather": "曇",
"series_number": 22,
"temperature": 24.7,
"away_score": 2,
"away_start_member": "佐藤　優也,田村　直也,金　鐘必,井林　章,安在　和樹,ニウド,鈴木　惇,澤井　直人,南　秀仁,杉本　竜士,常盤　聡",
"home_score": 1,
"home_shoot": 13,
"game_id": "16215",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/07/20 19:04",
"referee": "池内　明彦"
},
{
"teams": [
"愛媛ＦＣ",
"京都サンガF.C."
],
"away_director": "川勝　良一",
"home_start_member": "児玉　剛,村上　佑介,ハン　ヒフン,西岡　大輝,キム　ミンジェ,渡邊　一仁,吉村　圭司,堀米　勇輝,藤　直也,西田　剛,河原　和寿",
"away_shoot": 10,
"home_director": "石丸　清隆",
"away_team": "京都サンガF.C.",
"weather": "晴",
"series_number": 22,
"temperature": 26.2,
"away_score": 0,
"away_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,駒井　善成,田森　大己,工藤　浩平,山瀬　功治,中山　博貴,伊藤　優汰,三平　和司",
"home_score": 0,
"home_shoot": 3,
"game_id": "16216",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/07/20 19:04",
"referee": "野田　祐樹"
},
{
"teams": [
"ベガルタ仙台",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,角田　誠,石川　直樹,太田　吉彰,武井　択也,富田　晋伍,梁　勇基,赤嶺　真吾,ウイルソン",
"away_shoot": 12,
"home_director": "渡邉　晋",
"away_team": "名古屋グランパス",
"weather": "曇",
"series_number": 16,
"temperature": 27.2,
"away_score": 3,
"away_start_member": "楢﨑　正剛,牟田　雄祐,大武　峻,本多　勇喜,矢野　貴章,ダニルソン,田口　泰士,佐藤　和樹,レアンドロ　ドミンゲス,松田　力,永井　謙佑",
"home_score": 3,
"home_shoot": 9,
"game_id": "15804",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/07/23 19:03",
"referee": "吉田　寿光"
},
{
"teams": [
"鹿島アントラーズ",
"大宮アルディージャ"
],
"away_director": "大熊　清",
"home_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,ダヴィ",
"away_shoot": 10,
"home_director": "トニーニョ　セレーゾ",
"away_team": "大宮アルディージャ",
"weather": "晴",
"series_number": 16,
"temperature": 26.8,
"away_score": 2,
"away_start_member": "江角　浩司,今井　智基,菊地　光将,高橋　祥平,渡部　大輔,橋本　晃司,和田　拓也,渡邉　大剛,家長　昭博,ムルジャ,ズラタン",
"home_score": 2,
"home_shoot": 22,
"game_id": "15805",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/07/23 19:03",
"referee": "家本　政明"
},
{
"teams": [
"ヴァンフォーレ甲府",
"セレッソ大阪"
],
"away_director": "マルコ　ペッツァイオリ",
"home_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,稲垣　祥,新井　涼平,マルキーニョス　パラナ,阿部　翔平,ジウシーニョ,石原　克哉,クリスティアーノ",
"away_shoot": 7,
"home_director": "城福　浩",
"away_team": "セレッソ大阪",
"weather": "曇",
"series_number": 16,
"temperature": 28.6,
"away_score": 0,
"away_start_member": "キム　ジンヒョン,藤本　康太,丸橋　祐介,安藤　淳,山下　達也,扇原　貴宏,山口　蛍,南野　拓実,平野　甲斐,キム　ソンジュン,杉本　健勇",
"home_score": 0,
"home_shoot": 10,
"game_id": "15807",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/07/23 19:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"アルビレックス新潟",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,李　明載,レオ　シルバ,小林　裕紀,山本　康裕,田中　亜土夢,鈴木　武蔵,岡本　英也",
"away_shoot": 6,
"home_director": "柳下　正明",
"away_team": "ＦＣ東京",
"weather": "曇",
"series_number": 16,
"temperature": 26.9,
"away_score": 1,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,三田　啓貴,河野　広貴,エドゥー,武藤　嘉紀",
"home_score": 0,
"home_shoot": 12,
"game_id": "15808",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/07/23 19:03",
"referee": "榎本　一慶"
},
{
"teams": [
"ガンバ大阪",
"清水エスパルス"
],
"away_director": "アフシン　ゴトビ",
"home_start_member": "東口　順昭,米倉　恒貴,西野　貴治,岩下　敬輔,オ　ジェソク,今野　泰幸,遠藤　保仁,阿部　浩之,大森　晃太郎,宇佐美　貴史,パトリック",
"away_shoot": 4,
"home_director": "長谷川　健太",
"away_team": "清水エスパルス",
"weather": "晴",
"series_number": 16,
"temperature": 29.5,
"away_score": 0,
"away_start_member": "相澤　貴志,ヤコヴィッチ,平岡　康裕,杉山　浩太,吉田　豊,本田　拓也,六平　光成,河井　陽介,ノヴァコヴィッチ,大前　元紀,高木　俊幸",
"home_score": 4,
"home_shoot": 18,
"game_id": "15809",
"home_team": "ガンバ大阪",
"game_start_at": "2014/07/23 19:03",
"referee": "岡部　拓人"
},
{
"teams": [
"サンフレッチェ広島",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "林　卓人,ファン　ソッコ,塩谷　司,水本　裕貴,清水　航平,柴﨑　晃誠,森﨑　和幸,柏　好文,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"away_shoot": 15,
"home_director": "森保　一",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 16,
"temperature": 27.4,
"away_score": 2,
"away_start_member": "菅野　孝憲,鈴木　大輔,増嶋　竜也,渡部　博文,橋本　和,キム　チャンス,茨田　陽生,大谷　秀和,狩野　健太,工藤　壮人,レアンドロ",
"home_score": 5,
"home_shoot": 9,
"game_id": "15810",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/07/23 19:04",
"referee": "山本　雄大"
},
{
"teams": [
"サガン鳥栖",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,早坂　良太,岡本　知剛,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 8,
"home_director": "尹　晶煥",
"away_team": "川崎フロンターレ",
"weather": "曇",
"series_number": 16,
"temperature": 29.2,
"away_score": 1,
"away_start_member": "杉山　力裕,小宮山　尊信,實藤　友紀,谷口　彰悟,登里　享平,大島　僚太,中村　憲剛,森谷　賢太郎,金久保　順,小林　悠,大久保　嘉人",
"home_score": 0,
"home_shoot": 9,
"game_id": "15812",
"home_team": "サガン鳥栖",
"game_start_at": "2014/07/23 19:04",
"referee": "松尾　一"
},
{
"teams": [
"徳島ヴォルティス",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "長谷川　徹,藤原　広太朗,福元　洋平,村松　大輔,アレックス,斉藤　大介,濱田　武,衛藤　裕,大﨑　淳矢,宮崎　光平,高崎　寛之",
"away_shoot": 10,
"home_director": "小林　伸二",
"away_team": "浦和レッズ",
"weather": "晴",
"series_number": 16,
"temperature": 26.8,
"away_score": 2,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,青木　拓矢,阿部　勇樹,宇賀神　友弥,柏木　陽介,梅崎　司,興梠　慎三",
"home_score": 0,
"home_shoot": 10,
"game_id": "15811",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/07/23 19:05",
"referee": "今村　義朗"
},
{
"teams": [
"横浜Ｆ・マリノス",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,ドゥトラ,中町　公祐,小椋　祥平,兵藤　慎剛,中村　俊輔,齋藤　学,伊藤　翔",
"away_shoot": 7,
"home_director": "樋口　靖洋",
"away_team": "ヴィッセル神戸",
"weather": "晴",
"series_number": 16,
"temperature": 28.6,
"away_score": 1,
"away_start_member": "山本　海人,奥井　諒,河本　裕之,増川　隆洋,高橋　峻希,森岡　亮太,チョン　ウヨン,ペドロ　ジュニオール,シンプリシオ,マルキーニョス,小川　慶治朗",
"home_score": 1,
"home_shoot": 16,
"game_id": "15806",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/07/23 19:34",
"referee": "佐藤　隆治"
},
{
"teams": [
"横浜ＦＣ",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "南　雄太,市村　篤司,野上　結貴,ドウグラス,中島　崇典,寺田　紳一,松下　裕樹,松下　年宏,小池　純輝,野崎　陽介,パク　ソンホ",
"away_shoot": 7,
"home_director": "山口　素弘",
"away_team": "ジュビロ磐田",
"weather": "晴",
"series_number": 23,
"temperature": 29.4,
"away_score": 0,
"away_start_member": "八田　直樹,駒野　友一,藤田　義明,菅沼　駿哉,宮崎　智彦,岡田　隆,山崎　亮平,松井　大輔,小林　祐希,阿部　吉朗,ポポ",
"home_score": 4,
"home_shoot": 11,
"game_id": "16218",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/07/26 18:03",
"referee": "松尾　一"
},
{
"teams": [
"カマタマーレ讃岐",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "瀬口　拓弥,武田　有祐,エブソン,藤井　航大,沼田　圭悟,山本　翔平,関原　凌河,岡村　和哉,大沢　朋也,小澤　雄希,木島　良輔",
"away_shoot": 6,
"home_director": "北野　誠",
"away_team": "ＦＣ岐阜",
"weather": "晴",
"series_number": 23,
"temperature": 31,
"away_score": 2,
"away_start_member": "川口　能活,益山　司,木谷　公亮,関田　寛士,田中　秀人,宮沢　正史,水野　泰輔,井上　平,髙地　系治,遠藤　純輝,ナザリト",
"home_score": 1,
"home_shoot": 10,
"game_id": "16220",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/07/26 18:03",
"referee": "上田　益也"
},
{
"teams": [
"ギラヴァンツ北九州",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"away_shoot": 9,
"home_director": "柱谷　幸一",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 23,
"temperature": 29.4,
"away_score": 1,
"away_start_member": "武田　洋平,安川　有,高木　和道,若狭　大志,松本　怜,伊藤　大介,末吉　隼也,松本　昌也,為田　大貴,林　容平,ラドンチッチ",
"home_score": 1,
"home_shoot": 10,
"game_id": "16221",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/07/26 18:03",
"referee": "長谷　拓"
},
{
"teams": [
"モンテディオ山形",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "山岸　範宏,山田　拓巳,イ　ジュヨン,當間　建文,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,秋葉　勝,中島　裕希,伊東　俊",
"away_shoot": 6,
"home_director": "石﨑　信弘",
"away_team": "ザスパクサツ群馬",
"weather": "晴",
"series_number": 23,
"temperature": 31.3,
"away_score": 2,
"away_start_member": "富居　大樹,小柳　達司,クォン　ハンジン,青木　良太,瀬川　和樹,坂井　洋平,加藤　弘堅,永田　亮太,青木　孝太,ダニエル　ロビーニョ,宮崎　泰右",
"home_score": 1,
"home_shoot": 12,
"game_id": "16217",
"home_team": "モンテディオ山形",
"game_start_at": "2014/07/26 18:04",
"referee": "山本　雄大"
},
{
"teams": [
"松本山雅ＦＣ",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "村山　智彦,犬飼　智也,飯田　真輝,多々良　敦斗,田中　隼磨,岩間　雄大,岩沼　俊介,喜山　康平,岩上　祐三,船山　貴之,サビア",
"away_shoot": 12,
"home_director": "反町　康治",
"away_team": "東京ヴェルディ",
"weather": "晴",
"series_number": 23,
"temperature": 29.8,
"away_score": 1,
"away_start_member": "キローラン　菜入,田村　直也,金　鐘必,井林　章,安在　和樹,吉野　恭平,鈴木　惇,澤井　直人,南　秀仁,常盤　聡,杉本　竜士",
"home_score": 1,
"home_shoot": 12,
"game_id": "16219",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/07/26 18:04",
"referee": "窪田　陽輔"
},
{
"teams": [
"ジェフユナイテッド千葉",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "岡本　昌弘,竹内　彬,大岩　一貴,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,山中　亮輔,大塚　翔平,森本　貴幸",
"away_shoot": 12,
"home_director": "関塚　隆",
"away_team": "Ｖ・ファーレン長崎",
"weather": "晴",
"series_number": 23,
"temperature": 29.2,
"away_score": 1,
"away_start_member": "中村　隼,岡本　拓也,山口　貴弘,髙杉　亮太,古部　健太,黒木　聖仁,三原　雅俊,神崎　大輔,奥埜　博亮,佐藤　洸一,イ　ヨンジェ",
"home_score": 1,
"home_shoot": 8,
"game_id": "16222",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/07/26 19:03",
"referee": "佐藤　隆治"
},
{
"teams": [
"ファジアーノ岡山",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,片山　瑛一,妹尾　隆佑,久保　裕一",
"away_shoot": 10,
"home_director": "影山　雅永",
"away_team": "栃木ＳＣ",
"weather": "晴",
"series_number": 23,
"temperature": 31.6,
"away_score": 1,
"away_start_member": "鈴木　智幸,山形　辰徳,チャ　ヨンファン,岡根　直哉,赤井　秀行,近藤　祐介,西澤　代志也,小野寺　達也,湯澤　洋介,廣瀬　浩二,瀬沼　優司",
"home_score": 3,
"home_shoot": 12,
"game_id": "16225",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/07/26 19:03",
"referee": "森川　浩次"
},
{
"teams": [
"ロアッソ熊本",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "畑　実,藏川　洋平,園田　拓也,橋本　拳人,片山　奨典,中山　雄登,養父　雄仁,黒木　晃平,五領　淳樹,齊藤　和樹,澤田　崇",
"away_shoot": 7,
"home_director": "小野　剛",
"away_team": "水戸ホーリーホック",
"weather": "晴",
"series_number": 23,
"temperature": 29.3,
"away_score": 1,
"away_start_member": "笠原　昂史,新里　亮,冨田　大介,田中　雄大,小澤　司,中里　崇宏,広瀬　陸斗,小谷野　顕治,鈴木　雄斗,船谷　圭祐,鈴木　隆行",
"home_score": 2,
"home_shoot": 20,
"game_id": "16227",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/07/26 19:03",
"referee": "日高　晴樹"
},
{
"teams": [
"湘南ベルマーレ",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,岩尾　憲,菊地　俊介,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"away_shoot": 6,
"home_director": "曺　貴裁",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 23,
"temperature": 29.8,
"away_score": 0,
"away_start_member": "飯田　健巳,吉川　拓也,秋本　倫孝,高　准翼,木村　勝太,田中　寛己,キム　ヨングン,内田　健太,白崎　凌兵,中島　翔哉,苔口　卓也",
"home_score": 2,
"home_shoot": 19,
"game_id": "16223",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/07/26 19:04",
"referee": "榎本　一慶"
},
{
"teams": [
"愛媛ＦＣ",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "児玉　剛,村上　佑介,ハン　ヒフン,西岡　大輝,キム　ミンジェ,渡邊　一仁,吉村　圭司,藤　直也,原川　力,堀米　勇輝,西田　剛",
"away_shoot": 10,
"home_director": "石丸　清隆",
"away_team": "コンサドーレ札幌",
"weather": "晴",
"series_number": 23,
"temperature": 29.3,
"away_score": 3,
"away_start_member": "金山　隼樹,石井　謙伍,櫛引　一紀,奈良　竜樹,上原　慎也,河合　竜二,上里　一将,荒野　拓馬,宮澤　裕樹,小野　伸二,内村　圭宏",
"home_score": 2,
"home_shoot": 4,
"game_id": "16226",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/07/26 19:04",
"referee": "河合　英治"
},
{
"teams": [
"京都サンガF.C.",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,駒井　善成,田森　大己,工藤　浩平,中山　博貴,伊藤　優汰,三平　和司,大黒　将志",
"away_shoot": 4,
"home_director": "川勝　良一",
"away_team": "アビスパ福岡",
"weather": "晴",
"series_number": 23,
"temperature": 30.1,
"away_score": 1,
"away_start_member": "神山　竜一,阿部　巧,パク　ゴン,イ　グァンソン,堤　俊輔,中原　秀人,武田　英二郎,酒井　宣福,坂田　大輔,城後　寿,三島　勇太",
"home_score": 3,
"home_shoot": 15,
"game_id": "16224",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/07/26 19:05",
"referee": "高山　啓義"
},
{
"teams": [
"浦和レッズ",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,関根　貴大,鈴木　啓太,阿部　勇樹,宇賀神　友弥,柏木　陽介,梅崎　司,興梠　慎三",
"away_shoot": 11,
"home_director": "ペトロヴィッチ",
"away_team": "鹿島アントラーズ",
"weather": "晴",
"series_number": 17,
"temperature": 28.3,
"away_score": 1,
"away_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,カイオ,豊川　雄太,土居　聖真,ダヴィ",
"home_score": 1,
"home_shoot": 9,
"game_id": "15813",
"home_team": "浦和レッズ",
"game_start_at": "2014/07/27 18:04",
"referee": "西村　雄一"
},
{
"teams": [
"清水エスパルス",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "相澤　貴志,ヤコヴィッチ,吉田　豊,平岡　康裕,杉山　浩太,本田　拓也,六平　光成,河井　陽介,大前　元紀,ノヴァコヴィッチ,高木　俊幸",
"away_shoot": 3,
"home_director": "アフシン　ゴトビ",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 17,
"temperature": 29.4,
"away_score": 0,
"away_start_member": "菅野　孝憲,鈴木　大輔,増嶋　竜也,渡部　博文,橋本　和,キム　チャンス,茨田　陽生,大谷　秀和,狩野　健太,工藤　壮人,レアンドロ",
"home_score": 3,
"home_shoot": 13,
"game_id": "15817",
"home_team": "清水エスパルス",
"game_start_at": "2014/07/27 18:04",
"referee": "池内　明彦"
},
{
"teams": [
"ＦＣ東京",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,河野　広貴,平山　相太,武藤　嘉紀",
"away_shoot": 11,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "ベガルタ仙台",
"weather": "晴一時雨",
"series_number": 17,
"temperature": 28.3,
"away_score": 0,
"away_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,角田　誠,二見　宏志,太田　吉彰,富田　晋伍,武井　択也,梁　勇基,柳沢　敦,ウイルソン",
"home_score": 3,
"home_shoot": 8,
"game_id": "15815",
"home_team": "ＦＣ東京",
"game_start_at": "2014/07/27 18:34",
"referee": "前田　拓哉"
},
{
"teams": [
"川崎フロンターレ",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "杉山　力裕,小宮山　尊信,實藤　友紀,谷口　彰悟,登里　享平,大島　僚太,中村　憲剛,森谷　賢太郎,金久保　順,小林　悠,大久保　嘉人",
"away_shoot": 11,
"home_director": "風間　八宏",
"away_team": "アルビレックス新潟",
"weather": "曇のち晴",
"series_number": 17,
"temperature": 28.9,
"away_score": 0,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,李　明載,レオ　シルバ,小林　裕紀,山本　康裕,成岡　翔,田中　達也,岡本　英也",
"home_score": 1,
"home_shoot": 11,
"game_id": "15816",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/07/27 19:03",
"referee": "木村　博之"
},
{
"teams": [
"大宮アルディージャ",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "江角　浩司,今井　智基,菊地　光将,高橋　祥平,和田　拓也,増田　誓志,渡邉　大剛,渡部　大輔,家長　昭博,ズラタン,ムルジャ",
"away_shoot": 10,
"home_director": "大熊　清",
"away_team": "徳島ヴォルティス",
"weather": "晴のち曇",
"series_number": 17,
"temperature": 26.9,
"away_score": 3,
"away_start_member": "長谷川　徹,藤原　広太朗,福元　洋平,村松　大輔,アレックス,斉藤　大介,濱田　武,衛藤　裕,大﨑　淳矢,佐々木　一輝,高崎　寛之",
"home_score": 1,
"home_shoot": 15,
"game_id": "15814",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/07/27 19:04",
"referee": "吉田　寿光"
},
{
"teams": [
"名古屋グランパス",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,大武　峻,本多　勇喜,小川　佳純,ダニルソン,田口　泰士,矢田　旭,レアンドロ　ドミンゲス,玉田　圭司",
"away_shoot": 10,
"home_director": "西野　朗",
"away_team": "横浜Ｆ・マリノス",
"weather": "晴",
"series_number": 17,
"temperature": 27.8,
"away_score": 1,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,ドゥトラ,中町　公祐,小椋　祥平,兵藤　慎剛,中村　俊輔,齋藤　学,伊藤　翔",
"home_score": 1,
"home_shoot": 6,
"game_id": "15818",
"home_team": "名古屋グランパス",
"game_start_at": "2014/07/27 19:04",
"referee": "岡部　拓人"
},
{
"teams": [
"セレッソ大阪",
"サガン鳥栖"
],
"away_director": "尹　晶煥",
"home_start_member": "キム　ジンヒョン,藤本　康太,丸橋　祐介,安藤　淳,山下　達也,扇原　貴宏,山口　蛍,南野　拓実,平野　甲斐,キム　ソンジュン,フォルラン",
"away_shoot": 7,
"home_director": "マルコ　ペッツァイオリ",
"away_team": "サガン鳥栖",
"weather": "曇",
"series_number": 17,
"temperature": 27.9,
"away_score": 1,
"away_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 0,
"home_shoot": 9,
"game_id": "15819",
"home_team": "セレッソ大阪",
"game_start_at": "2014/07/27 19:04",
"referee": "村上　伸次"
},
{
"teams": [
"ヴィッセル神戸",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "山本　海人,岩波　拓也,増川　隆洋,高橋　峻希,チョン　ウヨン,シンプリシオ,小川　慶治朗,ペドロ　ジュニオール,橋本　英郎,森岡　亮太,マルキーニョス",
"away_shoot": 19,
"home_director": "安達　亮",
"away_team": "ガンバ大阪",
"weather": "晴",
"series_number": 17,
"temperature": 27.4,
"away_score": 5,
"away_start_member": "東口　順昭,米倉　恒貴,西野　貴治,岩下　敬輔,オ　ジェソク,今野　泰幸,遠藤　保仁,阿部　浩之,大森　晃太郎,宇佐美　貴史,パトリック",
"home_score": 1,
"home_shoot": 15,
"game_id": "15820",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/07/27 19:04",
"referee": "扇谷　健司"
},
{
"teams": [
"サンフレッチェ広島",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "林　卓人,ファン　ソッコ,塩谷　司,水本　裕貴,柏　好文,柴﨑　晃誠,森﨑　和幸,山岸　智,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"away_shoot": 4,
"home_director": "森保　一",
"away_team": "ヴァンフォーレ甲府",
"weather": "晴",
"series_number": 17,
"temperature": 25.3,
"away_score": 1,
"away_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,稲垣　祥,新井　涼平,マルキーニョス　パラナ,阿部　翔平,水野　晃樹,石原　克哉,クリスティアーノ",
"home_score": 1,
"home_shoot": 16,
"game_id": "15821",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/07/27 19:04",
"referee": "今村　義朗"
},
{
"teams": [
"コンサドーレ札幌",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "金山　隼樹,石井　謙伍,櫛引　一紀,奈良　竜樹,上原　慎也,上里　一将,上原　拓郎,荒野　拓馬,宮澤　裕樹,小野　伸二,内村　圭宏",
"away_shoot": 9,
"home_director": "財前　恵一",
"away_team": "横浜ＦＣ",
"weather": "屋内",
"series_number": 24,
"temperature": 23.1,
"away_score": 1,
"away_start_member": "南　雄太,市村　篤司,野上　結貴,ドウグラス,中島　崇典,松下　裕樹,寺田　紳一,松下　年宏,小池　純輝,野崎　陽介,パク　ソンホ",
"home_score": 0,
"home_shoot": 9,
"game_id": "16228",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/07/30 19:03",
"referee": "岡部　拓人"
},
{
"teams": [
"水戸ホーリーホック",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "本間　幸司,細川　淳矢,新里　亮,尾本　敬,田中　雄大,内田　航平,西岡　謙太,鈴木　雄斗,吉田　眞紀人,三島　康平,馬場　賢治",
"away_shoot": 9,
"home_director": "柱谷　哲二",
"away_team": "Ｖ・ファーレン長崎",
"weather": "晴",
"series_number": 24,
"temperature": 25.6,
"away_score": 0,
"away_start_member": "中村　隼,岡本　拓也,山口　貴弘,髙杉　亮太,神崎　大輔,黒木　聖仁,三原　雅俊,野田　紘史,奥埜　博亮,スティッペ,イ　ヨンジェ",
"home_score": 0,
"home_shoot": 12,
"game_id": "16229",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/07/30 19:03",
"referee": "塚田　健太"
},
{
"teams": [
"ジェフユナイテッド千葉",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,山中　亮輔,谷澤　達也,森本　貴幸",
"away_shoot": 13,
"home_director": "関塚　隆",
"away_team": "モンテディオ山形",
"weather": "晴",
"series_number": 24,
"temperature": 26.9,
"away_score": 0,
"away_start_member": "山岸　範宏,山田　拓巳,當間　建文,石井　秀典,石川　竜也,宮阪　政樹,ディエゴ,松岡　亮輔,秋葉　勝,中島　裕希,比嘉　厚平",
"home_score": 2,
"home_shoot": 14,
"game_id": "16230",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/07/30 19:03",
"referee": "高山　啓義"
},
{
"teams": [
"東京ヴェルディ",
"京都サンガF.C."
],
"away_director": "川勝　良一",
"home_start_member": "キローラン　菜入,田村　直也,金　鐘必,井林　章,安在　和樹,ニウド,鈴木　惇,澤井　直人,南　秀仁,杉本　竜士,常盤　聡",
"away_shoot": 7,
"home_director": "三浦　泰年",
"away_team": "京都サンガF.C.",
"weather": "晴",
"series_number": 24,
"temperature": 28.3,
"away_score": 0,
"away_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,駒井　善成,田森　大己,工藤　浩平,伊藤　優汰,山瀬　功治,中山　博貴,大黒　将志",
"home_score": 1,
"home_shoot": 6,
"game_id": "16231",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/07/30 19:03",
"referee": "長谷　拓"
},
{
"teams": [
"アビスパ福岡",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "神山　竜一,阿部　巧,パク　ゴン,イ　グァンソン,堤　俊輔,中原　秀人,武田　英二郎,金森　健志,石津　大介,城後　寿,酒井　宣福",
"away_shoot": 13,
"home_director": "マリヤン　プシュニク",
"away_team": "湘南ベルマーレ",
"weather": "曇",
"series_number": 24,
"temperature": 25.4,
"away_score": 0,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,岩尾　憲,菊地　俊介,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"home_score": 0,
"home_shoot": 5,
"game_id": "16236",
"home_team": "アビスパ福岡",
"game_start_at": "2014/07/30 19:03",
"referee": "窪田　陽輔"
},
{
"teams": [
"大分トリニータ",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "武田　洋平,安川　有,高木　和道,若狭　大志,松本　怜,伊藤　大介,為田　大貴,キム　ジョンヒョン,松本　昌也,林　容平,ラドンチッチ",
"away_shoot": 16,
"home_director": "田坂　和昭",
"away_team": "栃木ＳＣ",
"weather": "雨時々曇",
"series_number": 24,
"temperature": 25.4,
"away_score": 1,
"away_start_member": "鈴木　智幸,赤井　秀行,岡根　直哉,ドゥドゥ,菅　和範,近藤　祐介,西澤　代志也,小野寺　達也,中美　慶哉,重松　健太郎,大久保　哲哉",
"home_score": 2,
"home_shoot": 9,
"game_id": "16237",
"home_team": "大分トリニータ",
"game_start_at": "2014/07/30 19:03",
"referee": "小屋　幸栄"
},
{
"teams": [
"松本山雅ＦＣ",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "村山　智彦,犬飼　智也,飯田　真輝,多々良　敦斗,岩沼　俊介,岩間　雄大,田中　隼磨,岩上　祐三,喜山　康平,船山　貴之,サビア",
"away_shoot": 4,
"home_director": "反町　康治",
"away_team": "ロアッソ熊本",
"weather": "曇",
"series_number": 24,
"temperature": 27,
"away_score": 1,
"away_start_member": "畑　実,園田　拓也,篠原　弘次郎,キム　ビョンヨン,藏川　洋平,上村　周平,養父　雄仁,黒木　晃平,中山　雄登,齊藤　和樹,澤田　崇",
"home_score": 2,
"home_shoot": 21,
"game_id": "16232",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/07/30 19:04",
"referee": "榎本　一慶"
},
{
"teams": [
"カターレ富山",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "飯田　健巳,御厨　貴文,秋本　倫孝,高　准翼,木村　勝太,田中　寛己,大山　俊輔,内田　健太,白崎　凌兵,中島　翔哉,苔口　卓也",
"away_shoot": 10,
"home_director": "安間　貴義",
"away_team": "愛媛ＦＣ",
"weather": "晴",
"series_number": 24,
"temperature": 29.3,
"away_score": 3,
"away_start_member": "児玉　剛,三原　向平,村上　佑介,ハン　ヒフン,代　健司,キム　ミンジェ,渡邊　一仁,原川　力,堀米　勇輝,西田　剛,河原　和寿",
"home_score": 1,
"home_shoot": 16,
"game_id": "16233",
"home_team": "カターレ富山",
"game_start_at": "2014/07/30 19:04",
"referee": "篠藤　巧"
},
{
"teams": [
"ジュビロ磐田",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "八田　直樹,櫻内　渚,菅沼　駿哉,伊野波　雅彦,森下　俊,藤田　義明,フェルジナンド,チンガ,ペク　ソンドン,山崎　亮平,阿部　吉朗",
"away_shoot": 7,
"home_director": "シャムスカ",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 24,
"temperature": 26.7,
"away_score": 2,
"away_start_member": "瀬口　拓弥,武田　有祐,大杉　誠人,藤井　航大,沼田　圭悟,堀河　俊大,岡村　和哉,山本　翔平,小澤　雄希,西野　泰正,古田　寛幸",
"home_score": 4,
"home_shoot": 11,
"game_id": "16234",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/07/30 19:04",
"referee": "福島　孝一郎"
},
{
"teams": [
"ＦＣ岐阜",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "川口　能活,田中　秀人,中村　英之,阿部　正紀,関田　寛士,水野　泰輔,清本　拓己,益山　司,髙地　系治,遠藤　純輝,ナザリト",
"away_shoot": 11,
"home_director": "ラモス　瑠偉",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 24,
"temperature": 28,
"away_score": 2,
"away_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,片山　瑛一,妹尾　隆佑,久保　裕一",
"home_score": 2,
"home_shoot": 8,
"game_id": "16235",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/07/30 19:04",
"referee": "野田　祐樹"
},
{
"teams": [
"ザスパクサツ群馬",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "富居　大樹,小柳　達司,クォン　ハンジン,青木　良太,瀬川　和樹,坂井　洋平,加藤　弘堅,永田　亮太,青木　孝太,ダニエル　ロビーニョ,宮崎　泰右",
"away_shoot": 5,
"home_director": "秋葉　忠宏",
"away_team": "ギラヴァンツ北九州",
"weather": "晴",
"series_number": 24,
"temperature": 27.9,
"away_score": 0,
"away_start_member": "大谷　幸輝,宮本　亨,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,井上　翔太,渡　大生,大島　秀夫",
"home_score": 0,
"home_shoot": 14,
"game_id": "16238",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/07/30 19:34",
"referee": "三上　正一郎"
},
{
"teams": [
"ガンバ大阪",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "東口　順昭,米倉　恒貴,西野　貴治,岩下　敬輔,オ　ジェソク,今野　泰幸,遠藤　保仁,阿部　浩之,倉田　秋,宇佐美　貴史,パトリック",
"away_shoot": 8,
"home_director": "長谷川　健太",
"away_team": "横浜Ｆ・マリノス",
"weather": "雨",
"series_number": 18,
"temperature": 25.3,
"away_score": 0,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,小椋　祥平,中町　公祐,兵藤　慎剛,中村　俊輔,齋藤　学,伊藤　翔",
"home_score": 2,
"home_shoot": 10,
"game_id": "15828",
"home_team": "ガンバ大阪",
"game_start_at": "2014/08/02 18:03",
"referee": "飯田　淳平"
},
{
"teams": [
"鹿島アントラーズ",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,カイオ,中村　充孝,土居　聖真,ダヴィ",
"away_shoot": 11,
"home_director": "トニーニョ　セレーゾ",
"away_team": "サンフレッチェ広島",
"weather": "晴",
"series_number": 18,
"temperature": 30.8,
"away_score": 1,
"away_start_member": "増田　卓也,塩谷　司,千葉　和彦,水本　裕貴,柏　好文,柴﨑　晃誠,森﨑　和幸,山岸　智,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"home_score": 5,
"home_shoot": 18,
"game_id": "15823",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/08/02 18:34",
"referee": "扇谷　健司"
},
{
"teams": [
"ＦＣ東京",
"清水エスパルス"
],
"away_director": "大榎　克己",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,河野　広貴,エドゥー,武藤　嘉紀",
"away_shoot": 14,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "清水エスパルス",
"weather": "晴",
"series_number": 18,
"temperature": 31.3,
"away_score": 0,
"away_start_member": "相澤　貴志,ヤコヴィッチ,平岡　康裕,吉田　豊,杉山　浩太,本田　拓也,河井　陽介,六平　光成,高木　俊幸,大前　元紀,ノヴァコヴィッチ",
"home_score": 4,
"home_shoot": 11,
"game_id": "15826",
"home_team": "ＦＣ東京",
"game_start_at": "2014/08/02 18:34",
"referee": "木村　博之"
},
{
"teams": [
"徳島ヴォルティス",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "長谷川　徹,藤原　広太朗,福元　洋平,村松　大輔,アレックス,斉藤　大介,濱田　武,衛藤　裕,大﨑　淳矢,佐々木　一輝,高崎　寛之",
"away_shoot": 14,
"home_director": "小林　伸二",
"away_team": "ヴァンフォーレ甲府",
"weather": "雨",
"series_number": 18,
"temperature": 24.4,
"away_score": 2,
"away_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,稲垣　祥,新井　涼平,マルキーニョス　パラナ,阿部　翔平,阿部　拓馬,ジウシーニョ,クリスティアーノ",
"home_score": 2,
"home_shoot": 6,
"game_id": "15829",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/08/02 18:34",
"referee": "岡部　拓人"
},
{
"teams": [
"柏レイソル",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "菅野　孝憲,藤田　優人,鈴木　大輔,増嶋　竜也,橋本　和,秋野　央樹,栗澤　僚一,大谷　秀和,高山　薫,レアンドロ,工藤　壮人",
"away_shoot": 8,
"home_director": "ネルシーニョ",
"away_team": "川崎フロンターレ",
"weather": "晴",
"series_number": 18,
"temperature": 29.3,
"away_score": 1,
"away_start_member": "杉山　力裕,小宮山　尊信,實藤　友紀,谷口　彰悟,登里　享平,大島　僚太,中村　憲剛,森谷　賢太郎,金久保　順,小林　悠,大久保　嘉人",
"home_score": 4,
"home_shoot": 16,
"game_id": "15825",
"home_team": "柏レイソル",
"game_start_at": "2014/08/02 19:03",
"referee": "高山　啓義"
},
{
"teams": [
"アルビレックス新潟",
"セレッソ大阪"
],
"away_director": "マルコ　ペッツァイオリ",
"home_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,李　明載,レオ　シルバ,小林　裕紀,山本　康裕,田中　亜土夢,田中　達也,岡本　英也",
"away_shoot": 6,
"home_director": "柳下　正明",
"away_team": "セレッソ大阪",
"weather": "晴",
"series_number": 18,
"temperature": 30.4,
"away_score": 0,
"away_start_member": "キム　ジンヒョン,藤本　康太,丸橋　祐介,安藤　淳,山下　達也,扇原　貴宏,山口　蛍,キム　ソンジュン,フォルラン,南野　拓実,杉本　健勇",
"home_score": 1,
"home_shoot": 8,
"game_id": "15827",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/08/02 19:03",
"referee": "今村　義朗"
},
{
"teams": [
"ベガルタ仙台",
"大宮アルディージャ"
],
"away_director": "大熊　清",
"home_start_member": "関　憲太郎,菅井　直樹,渡辺　広大,鎌田　次郎,石川　直樹,太田　吉彰,富田　晋伍,角田　誠,梁　勇基,赤嶺　真吾,ウイルソン",
"away_shoot": 14,
"home_director": "渡邉　晋",
"away_team": "大宮アルディージャ",
"weather": "晴",
"series_number": 18,
"temperature": 27.4,
"away_score": 2,
"away_start_member": "清水　慶記,中村　北斗,今井　智基,横山　知伸,高橋　祥平,橋本　晃司,和田　拓也,家長　昭博,富山　貴光,ムルジャ,ズラタン",
"home_score": 2,
"home_shoot": 10,
"game_id": "15822",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/08/02 19:04",
"referee": "中村　太"
},
{
"teams": [
"浦和レッズ",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,鈴木　啓太,阿部　勇樹,宇賀神　友弥,柏木　陽介,梅崎　司,興梠　慎三",
"away_shoot": 7,
"home_director": "ペトロヴィッチ",
"away_team": "ヴィッセル神戸",
"weather": "晴",
"series_number": 18,
"temperature": 31.7,
"away_score": 2,
"away_start_member": "山本　海人,河本　裕之,増川　隆洋,大屋　翼,橋本　英郎,杉浦　恭平,奥井　諒,高橋　峻希,小川　慶治朗,森岡　亮太,マルキーニョス",
"home_score": 2,
"home_shoot": 12,
"game_id": "15824",
"home_team": "浦和レッズ",
"game_start_at": "2014/08/02 19:04",
"referee": "松尾　一"
},
{
"teams": [
"サガン鳥栖",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 6,
"home_director": "尹　晶煥",
"away_team": "名古屋グランパス",
"weather": "曇",
"series_number": 18,
"temperature": 26.8,
"away_score": 0,
"away_start_member": "楢﨑　正剛,田鍋　陵太,牟田　雄祐,大武　峻,本多　勇喜,松田　力,ダニルソン,田口　泰士,レアンドロ　ドミンゲス,玉田　圭司,永井　謙佑",
"home_score": 1,
"home_shoot": 11,
"game_id": "15830",
"home_team": "サガン鳥栖",
"game_start_at": "2014/08/02 19:04",
"referee": "家本　政明"
},
{
"teams": [
"栃木ＳＣ",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "鈴木　智幸,赤井　秀行,岡根　直哉,ドゥドゥ,菅　和範,近藤　祐介,西澤　代志也,小野寺　達也,廣瀬　浩二,重松　健太郎,瀬沼　優司",
"away_shoot": 12,
"home_director": "阪倉　裕二",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 25,
"temperature": 30.1,
"away_score": 2,
"away_start_member": "石井　健太,藤田　浩平,藤井　航大,エブソン,沼田　圭悟,堀河　俊大,山本　翔平,岡村　和哉,小澤　雄希,古田　寛幸,我那覇　和樹",
"home_score": 1,
"home_shoot": 3,
"game_id": "16240",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/08/03 18:03",
"referee": "三上　正一郎"
},
{
"teams": [
"横浜ＦＣ",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "南　雄太,市村　篤司,野上　結貴,ドウグラス,中島　崇典,寺田　紳一,松下　裕樹,松下　年宏,小池　純輝,野崎　陽介,パク　ソンホ",
"away_shoot": 10,
"home_director": "山口　素弘",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 25,
"temperature": 28.8,
"away_score": 0,
"away_start_member": "飯田　健巳,御厨　貴文,秋本　倫孝,高　准翼,木村　勝太,平出　涼,大山　俊輔,國吉　貴博,白崎　凌兵,中島　翔哉,苔口　卓也",
"home_score": 2,
"home_shoot": 13,
"game_id": "16241",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/08/03 18:03",
"referee": "上田　益也"
},
{
"teams": [
"ギラヴァンツ北九州",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"away_shoot": 20,
"home_director": "柱谷　幸一",
"away_team": "コンサドーレ札幌",
"weather": "曇時々雨",
"series_number": 25,
"temperature": 27.5,
"away_score": 0,
"away_start_member": "金山　隼樹,石井　謙伍,櫛引　一紀,奈良　竜樹,上原　慎也,深井　一希,上里　一将,ヘナン,宮澤　裕樹,小野　伸二,都倉　賢",
"home_score": 2,
"home_shoot": 5,
"game_id": "16244",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/08/03 18:03",
"referee": "村上　伸次"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "中村　隼,岡本　拓也,山口　貴弘,髙杉　亮太,神崎　大輔,黒木　聖仁,三原　雅俊,野田　紘史,佐藤　洸一,奥埜　博亮,スティッペ",
"away_shoot": 7,
"home_director": "高木　琢也",
"away_team": "ＦＣ岐阜",
"weather": "雨",
"series_number": 25,
"temperature": 27.5,
"away_score": 2,
"away_start_member": "川口　能活,木谷　公亮,中村　英之,阿部　正紀,岩﨑　陽平,ヘニキ,髙地　系治,比嘉　諒人,清本　拓己,井上　平,難波　宏明",
"home_score": 0,
"home_shoot": 10,
"game_id": "16245",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/08/03 18:03",
"referee": "池内　明彦"
},
{
"teams": [
"モンテディオ山形",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "山岸　範宏,小林　亮,西河　翔吾,石井　秀典,石川　竜也,宮阪　政樹,ロメロ　フランク,松岡　亮輔,秋葉　勝,ディエゴ,伊東　俊",
"away_shoot": 10,
"home_director": "石﨑　信弘",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 25,
"temperature": 30.9,
"away_score": 0,
"away_start_member": "武田　洋平,安川　有,高木　和道,若狭　大志,末吉　隼也,伊藤　大介,松本　怜,松本　昌也,為田　大貴,林　容平,ラドンチッチ",
"home_score": 2,
"home_shoot": 17,
"game_id": "16239",
"home_team": "モンテディオ山形",
"game_start_at": "2014/08/03 18:04",
"referee": "吉田　哲朗"
},
{
"teams": [
"ジュビロ磐田",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "八田　直樹,駒野　友一,菅沼　駿哉,伊野波　雅彦,森下　俊,藤田　義明,小林　祐希,ペク　ソンドン,松井　大輔,チンガ,阿部　吉朗",
"away_shoot": 10,
"home_director": "シャムスカ",
"away_team": "松本山雅ＦＣ",
"weather": "曇",
"series_number": 25,
"temperature": 26.9,
"away_score": 1,
"away_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,多々良　敦斗,岩間　雄大,喜山　康平,岩沼　俊介,岩上　祐三,サビア,船山　貴之",
"home_score": 1,
"home_shoot": 13,
"game_id": "16242",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/08/03 18:04",
"referee": "山本　雄大"
},
{
"teams": [
"愛媛ＦＣ",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "児玉　剛,三原　向平,村上　佑介,ハン　ヒフン,代　健司,キム　ミンジェ,渡邊　一仁,吉村　圭司,堀米　勇輝,渡辺　亮太,河原　和寿",
"away_shoot": 10,
"home_director": "石丸　清隆",
"away_team": "アビスパ福岡",
"weather": "曇",
"series_number": 25,
"temperature": 27.6,
"away_score": 0,
"away_start_member": "神山　竜一,阿部　巧,パク　ゴン,イ　グァンソン,堤　俊輔,中原　秀人,平井　将生,酒井　宣福,石津　大介,城後　寿,坂田　大輔",
"home_score": 0,
"home_shoot": 11,
"game_id": "16243",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/08/03 18:04",
"referee": "榎本　一慶"
},
{
"teams": [
"ファジアーノ岡山",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,片山　瑛一,押谷　祐樹,久保　裕一",
"away_shoot": 9,
"home_director": "影山　雅永",
"away_team": "東京ヴェルディ",
"weather": "雨",
"series_number": 25,
"temperature": 25.7,
"away_score": 1,
"away_start_member": "キローラン　菜入,田村　直也,金　鐘必,井林　章,安在　和樹,ニウド,鈴木　惇,澤井　直人,南　秀仁,杉本　竜士,常盤　聡",
"home_score": 2,
"home_shoot": 15,
"game_id": "16248",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/08/03 19:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"ロアッソ熊本",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "畑　実,藏川　洋平,園田　拓也,橋本　拳人,片山　奨典,中山　雄登,養父　雄仁,キム　ビョンヨン,澤田　崇,齊藤　和樹,キム　ジョンソク",
"away_shoot": 6,
"home_director": "小野　剛",
"away_team": "ザスパクサツ群馬",
"weather": "曇",
"series_number": 25,
"temperature": 28.9,
"away_score": 1,
"away_start_member": "富居　大樹,小柳　達司,クォン　ハンジン,青木　良太,瀬川　和樹,坂井　洋平,黄　誠秀,永田　亮太,青木　孝太,ダニエル　ロビーニョ,宮崎　泰右",
"home_score": 0,
"home_shoot": 17,
"game_id": "16249",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/08/03 19:03",
"referee": "前田　拓哉"
},
{
"teams": [
"湘南ベルマーレ",
"ジェフユナイテッド千葉"
],
"away_director": "関塚　隆",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,菊地　俊介,岩尾　憲,亀川　諒史,樋口　寛規,ウェリントン,菊池　大介",
"away_shoot": 8,
"home_director": "曺　貴裁",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 25,
"temperature": 29.3,
"away_score": 1,
"away_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,山中　亮輔,ケンペス",
"home_score": 1,
"home_shoot": 13,
"game_id": "16246",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/08/03 19:04",
"referee": "西村　雄一"
},
{
"teams": [
"京都サンガF.C.",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "オ　スンフン,石櫃　洋祐,バヤリッツァ,酒井　隆介,駒井　善成,田中　英雄,田森　大己,山瀬　功治,中山　博貴,伊藤　優汰,大黒　将志",
"away_shoot": 4,
"home_director": "川勝　良一",
"away_team": "水戸ホーリーホック",
"weather": "雨",
"series_number": 25,
"temperature": 26.6,
"away_score": 1,
"away_start_member": "本間　幸司,新里　亮,冨田　大介,田中　雄大,石神　幸征,中里　崇宏,広瀬　陸斗,鈴木　雄斗,小澤　司,船谷　圭祐,三島　康平",
"home_score": 1,
"home_shoot": 10,
"game_id": "16247",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/08/03 19:04",
"referee": "吉田　寿光"
},
{
"teams": [
"清水エスパルス",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "櫛引　政敏,吉田　豊,平岡　康裕,杉山　浩太,イ　キジェ,本田　拓也,六平　光成,大前　元紀,河井　陽介,高木　俊幸,ノヴァコヴィッチ",
"away_shoot": 10,
"home_director": "大榎　克己",
"away_team": "徳島ヴォルティス",
"weather": "曇時々雨",
"series_number": 19,
"temperature": 26,
"away_score": 0,
"away_start_member": "長谷川　徹,藤原　広太朗,福元　洋平,那須川　将大,アレックス,斉藤　大介,濱田　武,衛藤　裕,大﨑　淳矢,佐々木　一輝,高崎　寛之",
"home_score": 1,
"home_shoot": 13,
"game_id": "15835",
"home_team": "清水エスパルス",
"game_start_at": "2014/08/09 18:04",
"referee": "松尾　一"
},
{
"teams": [
"ヴァンフォーレ甲府",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,ジウシーニョ,新井　涼平,稲垣　祥,阿部　翔平,石原　克哉,阿部　拓馬,クリスティアーノ",
"away_shoot": 13,
"home_director": "城福　浩",
"away_team": "ベガルタ仙台",
"weather": "曇",
"series_number": 19,
"temperature": 25.3,
"away_score": 0,
"away_start_member": "関　憲太郎,菅井　直樹,渡辺　広大,鎌田　次郎,石川　直樹,太田　吉彰,富田　晋伍,角田　誠,梁　勇基,赤嶺　真吾,武藤　雄樹",
"home_score": 0,
"home_shoot": 15,
"game_id": "15834",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/08/09 18:34",
"referee": "村上　伸次"
},
{
"teams": [
"大宮アルディージャ",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "江角　浩司,中村　北斗,今井　智基,横山　知伸,高橋　祥平,橋本　晃司,和田　拓也,家長　昭博,富山　貴光,ムルジャ,ズラタン",
"away_shoot": 13,
"home_director": "大熊　清",
"away_team": "ガンバ大阪",
"weather": "雨のち曇",
"series_number": 19,
"temperature": 23.1,
"away_score": 2,
"away_start_member": "東口　順昭,米倉　恒貴,西野　貴治,岩下　敬輔,オ　ジェソク,今野　泰幸,遠藤　保仁,阿部　浩之,倉田　秋,宇佐美　貴史,パトリック",
"home_score": 0,
"home_shoot": 13,
"game_id": "15831",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/08/09 19:04",
"referee": "廣瀬　格"
},
{
"teams": [
"川崎フロンターレ",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "杉山　力裕,小宮山　尊信,實藤　友紀,谷口　彰悟,登里　享平,大島　僚太,中村　憲剛,森谷　賢太郎,レナト,小林　悠,大久保　嘉人",
"away_shoot": 10,
"home_director": "風間　八宏",
"away_team": "浦和レッズ",
"weather": "曇",
"series_number": 19,
"temperature": 24.1,
"away_score": 1,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,鈴木　啓太,阿部　勇樹,宇賀神　友弥,柏木　陽介,梅崎　司,興梠　慎三",
"home_score": 2,
"home_shoot": 11,
"game_id": "15832",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/08/09 19:04",
"referee": "飯田　淳平"
},
{
"teams": [
"横浜Ｆ・マリノス",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "榎本　哲也,奈良輪　雄太,栗原　勇蔵,中澤　佑二,下平　匠,三門　雄大,中町　公祐,兵藤　慎剛,中村　俊輔,齋藤　学,ラフィーニャ",
"away_shoot": 10,
"home_director": "樋口　靖洋",
"away_team": "柏レイソル",
"weather": "曇",
"series_number": 19,
"temperature": 24.4,
"away_score": 2,
"away_start_member": "菅野　孝憲,藤田　優人,鈴木　大輔,増嶋　竜也,橋本　和,秋野　央樹,栗澤　僚一,大谷　秀和,高山　薫,レアンドロ,工藤　壮人",
"home_score": 2,
"home_shoot": 15,
"game_id": "15833",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/08/09 19:04",
"referee": "西村　雄一"
},
{
"teams": [
"名古屋グランパス",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,レアンドロ　ドミンゲス,ダニルソン,田口　泰士,矢田　旭,ケネディ,永井　謙佑",
"away_shoot": 15,
"home_director": "西野　朗",
"away_team": "鹿島アントラーズ",
"weather": "曇時々雨",
"series_number": 19,
"temperature": 27.3,
"away_score": 3,
"away_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,カイオ,中村　充孝,土居　聖真,ダヴィ",
"home_score": 2,
"home_shoot": 7,
"game_id": "15836",
"home_team": "名古屋グランパス",
"game_start_at": "2014/08/09 19:04",
"referee": "福島　孝一郎"
},
{
"teams": [
"セレッソ大阪",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "キム　ジンヒョン,藤本　康太,丸橋　祐介,安藤　淳,山下　達也,長谷川　アーリアジャスール,山口　蛍,楠神　順平,フォルラン,南野　拓実,杉本　健勇",
"away_shoot": 7,
"home_director": "マルコ　ペッツァイオリ",
"away_team": "ＦＣ東京",
"weather": "雨のち曇一時雨",
"series_number": 19,
"temperature": 26.8,
"away_score": 0,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,東　慶悟,河野　広貴,エドゥー,武藤　嘉紀",
"home_score": 0,
"home_shoot": 9,
"game_id": "15837",
"home_team": "セレッソ大阪",
"game_start_at": "2014/08/09 19:04",
"referee": "窪田　陽輔"
},
{
"teams": [
"ヴィッセル神戸",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "山本　海人,河本　裕之,岩波　拓也,奥井　諒,橋本　英郎,チョン　ウヨン,杉浦　恭平,シンプリシオ,森岡　亮太,ペドロ　ジュニオール,マルキーニョス",
"away_shoot": 13,
"home_director": "安達　亮",
"away_team": "アルビレックス新潟",
"weather": "屋内",
"series_number": 19,
"temperature": 26.3,
"away_score": 0,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,李　明載,レオ　シルバ,小林　裕紀,山本　康裕,田中　亜土夢,田中　達也,岡本　英也",
"home_score": 1,
"home_shoot": 9,
"game_id": "15838",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/08/09 19:04",
"referee": "山本　雄大"
},
{
"teams": [
"コンサドーレ札幌",
"京都サンガF.C."
],
"away_director": "川勝　良一",
"home_start_member": "金山　隼樹,石井　謙伍,パウロン,奈良　竜樹,上原　慎也,深井　一希,上里　一将,荒野　拓馬,宮澤　裕樹,小野　伸二,内村　圭宏",
"away_shoot": 5,
"home_director": "財前　恵一",
"away_team": "京都サンガF.C.",
"weather": "屋内",
"series_number": 26,
"temperature": 24,
"away_score": 1,
"away_start_member": "オ　スンフン,駒井　善成,内野　貴志,酒井　隆介,石櫃　洋祐,田森　大己,田中　英雄,山瀬　功治,石田　雅俊,中山　博貴,大黒　将志",
"home_score": 0,
"home_shoot": 16,
"game_id": "16250",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/08/10 14:03",
"referee": "前田　拓哉"
},
{
"teams": [
"大分トリニータ",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "武田　洋平,安川　有,若狭　大志,高木　和道,伊藤　大介,キム　ジョンヒョン,松本　怜,為田　大貴,松本　昌也,風間　宏矢,ラドンチッチ",
"away_shoot": 19,
"home_director": "田坂　和昭",
"away_team": "東京ヴェルディ",
"weather": "曇時々晴",
"series_number": 26,
"temperature": 25.7,
"away_score": 2,
"away_start_member": "キローラン　菜入,田村　直也,金　鐘必,井林　章,安在　和樹,ニウド,鈴木　惇,澤井　直人,南　秀仁,杉本　竜士,常盤　聡",
"home_score": 3,
"home_shoot": 16,
"game_id": "16257",
"home_team": "大分トリニータ",
"game_start_at": "2014/08/10 18:03",
"referee": "塚田　健太"
},
{
"teams": [
"水戸ホーリーホック",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "本間　幸司,新里　亮,冨田　大介,田中　雄大,石神　幸征,西岡　謙太,広瀬　陸斗,小澤　司,船谷　圭祐,吉田　眞紀人,鈴木　隆行",
"away_shoot": 6,
"home_director": "柱谷　哲二",
"away_team": "ギラヴァンツ北九州",
"weather": "雨のち曇",
"series_number": 26,
"temperature": 26.7,
"away_score": 1,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"home_score": 1,
"home_shoot": 13,
"game_id": "16251",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/08/10 18:04",
"referee": "森川　浩次"
},
{
"teams": [
"松本山雅ＦＣ",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,多々良　敦斗,岩沼　俊介,岩間　雄大,岩上　祐三,喜山　康平,船山　貴之,サビア",
"away_shoot": 10,
"home_director": "反町　康治",
"away_team": "栃木ＳＣ",
"weather": "雨のち曇",
"series_number": 26,
"temperature": 24.5,
"away_score": 1,
"away_start_member": "鈴木　智幸,赤井　秀行,チャ　ヨンファン,ドゥドゥ,鈴木　隆雅,廣瀬　浩二,西澤　代志也,小野寺　達也,近藤　祐介,瀬沼　優司,大久保　哲哉",
"home_score": 2,
"home_shoot": 13,
"game_id": "16253",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/08/10 18:04",
"referee": "今村　義朗"
},
{
"teams": [
"カターレ富山",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "柴田　大地,御厨　貴文,秋本　倫孝,高　准翼,木村　勝太,井澤　惇,平出　涼,内田　健太,白崎　凌兵,中島　翔哉,宮吉　拓実",
"away_shoot": 12,
"home_director": "安間　貴義",
"away_team": "モンテディオ山形",
"weather": "曇",
"series_number": 26,
"temperature": 28.7,
"away_score": 1,
"away_start_member": "山岸　範宏,小林　亮,西河　翔吾,石井　秀典,石川　竜也,松岡　亮輔,ロメロ　フランク,宮阪　政樹,秋葉　勝,中島　裕希,伊東　俊",
"home_score": 1,
"home_shoot": 7,
"game_id": "16254",
"home_team": "カターレ富山",
"game_start_at": "2014/08/10 18:04",
"referee": "野田　祐樹"
},
{
"teams": [
"ザスパクサツ群馬",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "富居　大樹,小柳　達司,クォン　ハンジン,乾　大知,瀬川　和樹,坂井　洋平,黄　誠秀,小林　竜樹,青木　孝太,ダニエル　ロビーニョ,宮崎　泰右",
"away_shoot": 15,
"home_director": "秋葉　忠宏",
"away_team": "Ｖ・ファーレン長崎",
"weather": "曇のち晴",
"series_number": 26,
"temperature": 26.9,
"away_score": 4,
"away_start_member": "中村　隼,岡本　拓也,山口　貴弘,髙杉　亮太,金久保　彩,黒木　聖仁,三原　雅俊,古部　健太,小松　塁,東　浩史,イ　ヨンジェ",
"home_score": 2,
"home_shoot": 12,
"game_id": "16252",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/08/10 18:05",
"referee": "日高　晴樹"
},
{
"teams": [
"アビスパ福岡",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "神山　竜一,三島　勇太,山口　和樹,堤　俊輔,古賀　正紘,中原　秀人,武田　英二郎,石津　大介,坂田　大輔,城後　寿,平井　将生",
"away_shoot": 6,
"home_director": "マリヤン　プシュニク",
"away_team": "ジュビロ磐田",
"weather": "雨のち曇",
"series_number": 26,
"temperature": 22.7,
"away_score": 1,
"away_start_member": "八田　直樹,駒野　友一,菅沼　駿哉,伊野波　雅彦,森下　俊,フェルジナンド,藤田　義明,ペク　ソンドン,松浦　拓弥,チンガ,阿部　吉朗",
"home_score": 3,
"home_shoot": 10,
"game_id": "16256",
"home_team": "アビスパ福岡",
"game_start_at": "2014/08/10 18:05",
"referee": "井上　知大"
},
{
"teams": [
"カマタマーレ讃岐",
"ロアッソ熊本"
],
"away_director": "台風のため60分遅延",
"home_start_member": "石井　健太,藤田　浩平,藤井　航大,エブソン,沼田　圭悟,堀河　俊大,岡村　和哉,山本　翔平,小澤　雄希,古田　寛幸,我那覇　和樹",
"away_shoot": 8,
"home_director": "小野　剛",
"away_team": "ロアッソ熊本",
"weather": "曇",
"series_number": 26,
"temperature": 26.8,
"away_score": 1,
"away_start_member": "畑　実,片山　奨典,園田　拓也,篠原　弘次郎,藏川　洋平,橋本　拳人,養父　雄仁,キム　ビョンヨン,澤田　崇,齊藤　和樹,中山　雄登",
"home_score": 1,
"home_shoot": 10,
"game_id": "16255",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/08/10 19:03",
"referee": "小屋　幸栄"
},
{
"teams": [
"ファジアーノ岡山",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,片山　瑛一,石原　崇兆,清水　慎太郎",
"away_shoot": 18,
"home_director": "影山　雅永",
"away_team": "湘南ベルマーレ",
"weather": "曇",
"series_number": 26,
"temperature": 27.1,
"away_score": 0,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,菊地　俊介,岩尾　憲,亀川　諒史,菊池　大介,ウェリントン,武富　孝介",
"home_score": 0,
"home_shoot": 10,
"game_id": "16260",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/08/10 19:03",
"referee": "家本　政明"
},
{
"teams": [
"ジェフユナイテッド千葉",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,ケンペス,森本　貴幸",
"away_shoot": 15,
"home_director": "関塚　隆",
"away_team": "横浜ＦＣ",
"weather": "曇",
"series_number": 26,
"temperature": 28.6,
"away_score": 0,
"away_start_member": "南　雄太,市村　篤司,野上　結貴,ドウグラス,中島　崇典,寺田　紳一,松下　裕樹,松下　年宏,小池　純輝,野崎　陽介,パク　ソンホ",
"home_score": 0,
"home_shoot": 18,
"game_id": "16258",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/08/10 19:04",
"referee": "吉田　哲朗"
},
{
"teams": [
"ＦＣ岐阜",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "川口　能活,木谷　公亮,中村　英之,阿部　正紀,ヘニキ,宮沢　正史,益山　司,清本　拓己,田中　秀人,難波　宏明,ナザリト",
"away_shoot": 4,
"home_director": "ラモス　瑠偉",
"away_team": "愛媛ＦＣ",
"weather": "曇時々雨",
"series_number": 26,
"temperature": 25.7,
"away_score": 3,
"away_start_member": "児玉　剛,三原　向平,村上　佑介,ハン　ヒフン,代　健司,キム　ミンジェ,渡邊　一仁,村上　巧,原川　力,リカルド　ロボ,河原　和寿",
"home_score": 4,
"home_shoot": 15,
"game_id": "16259",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/08/10 19:04",
"referee": "長谷　拓"
},
{
"teams": [
"サンフレッチェ広島",
"サガン鳥栖"
],
"away_director": "吉田　恵",
"home_start_member": "増田　卓也,宮原　和也,千葉　和彦,水本　裕貴,清水　航平,柴﨑　晃誠,森﨑　和幸,柏　好文,森﨑　浩司,髙萩　洋次郎,石原　直樹",
"away_shoot": 2,
"home_director": "森保　一",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 19,
"temperature": 24.6,
"away_score": 0,
"away_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 1,
"home_shoot": 10,
"game_id": "15839",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/08/11 19:04",
"referee": "吉田　寿光"
},
{
"teams": [
"ガンバ大阪",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "東口　順昭,オ　ジェソク,西野　貴治,岩下　敬輔,藤春　廣輝,今野　泰幸,遠藤　保仁,阿部　浩之,倉田　秋,宇佐美　貴史,パトリック",
"away_shoot": 7,
"home_director": "長谷川　健太",
"away_team": "名古屋グランパス",
"weather": "雨のち曇一時雨",
"series_number": 20,
"temperature": 27.8,
"away_score": 1,
"away_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,レアンドロ　ドミンゲス,ダニルソン,田口　泰士,小川　佳純,永井　謙佑,ケネディ",
"home_score": 0,
"home_shoot": 10,
"game_id": "15845",
"home_team": "ガンバ大阪",
"game_start_at": "2014/08/16 18:03",
"referee": "前田　拓哉"
},
{
"teams": [
"浦和レッズ",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "西川　周作,森脇　良太,永田　充,槙野　智章,平川　忠亮,鈴木　啓太,阿部　勇樹,宇賀神　友弥,柏木　陽介,梅崎　司,興梠　慎三",
"away_shoot": 4,
"home_director": "ペトロヴィッチ",
"away_team": "サンフレッチェ広島",
"weather": "雨のち曇",
"series_number": 20,
"temperature": 24.4,
"away_score": 0,
"away_start_member": "増田　卓也,宮原　和也,千葉　和彦,水本　裕貴,清水　航平,柴﨑　晃誠,森﨑　和幸,柏　好文,森﨑　浩司,髙萩　洋次郎,石原　直樹",
"home_score": 1,
"home_shoot": 7,
"game_id": "15842",
"home_team": "浦和レッズ",
"game_start_at": "2014/08/16 18:04",
"referee": "村上　伸次"
},
{
"teams": [
"鹿島アントラーズ",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "曽ヶ端　準,西　大伍,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,カイオ,中村　充孝,土居　聖真,ダヴィ",
"away_shoot": 10,
"home_director": "トニーニョ　セレーゾ",
"away_team": "ヴァンフォーレ甲府",
"weather": "雨のち曇",
"series_number": 20,
"temperature": 21.9,
"away_score": 0,
"away_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,ジウシーニョ,新井　涼平,保坂　一成,阿部　翔平,福田　健介,石原　克哉,クリスティアーノ",
"home_score": 1,
"home_shoot": 7,
"game_id": "15841",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/08/16 18:33",
"referee": "高山　啓義"
},
{
"teams": [
"ベガルタ仙台",
"清水エスパルス"
],
"away_director": "大榎　克己",
"home_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,角田　誠,梁　勇基,野沢　拓也,武藤　雄樹",
"away_shoot": 7,
"home_director": "渡邉　晋",
"away_team": "清水エスパルス",
"weather": "曇",
"series_number": 20,
"temperature": 21.8,
"away_score": 2,
"away_start_member": "櫛引　政敏,吉田　豊,平岡　康裕,杉山　浩太,イ　キジェ,本田　拓也,六平　光成,大前　元紀,河井　陽介,高木　俊幸,ノヴァコヴィッチ",
"home_score": 3,
"home_shoot": 15,
"game_id": "15840",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/08/16 19:04",
"referee": "家本　政明"
},
{
"teams": [
"柏レイソル",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "菅野　孝憲,藤田　優人,鈴木　大輔,増嶋　竜也,橋本　和,高山　薫,栗澤　僚一,エドゥアルド,大谷　秀和,工藤　壮人,レアンドロ",
"away_shoot": 19,
"home_director": "ネルシーニョ",
"away_team": "ヴィッセル神戸",
"weather": "曇",
"series_number": 20,
"temperature": 22.1,
"away_score": 0,
"away_start_member": "山本　海人,奥井　諒,河本　裕之,増川　隆洋,橋本　英郎,チョン　ウヨン,大屋　翼,杉浦　恭平,ペドロ　ジュニオール,マルキーニョス,森岡　亮太",
"home_score": 2,
"home_shoot": 14,
"game_id": "15843",
"home_team": "柏レイソル",
"game_start_at": "2014/08/16 19:04",
"referee": "中村　太"
},
{
"teams": [
"アルビレックス新潟",
"大宮アルディージャ"
],
"away_director": "大熊　清",
"home_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,大野　和成,レオ　シルバ,小林　裕紀,山本　康裕,田中　亜土夢,成岡　翔,岡本　英也",
"away_shoot": 5,
"home_director": "柳下　正明",
"away_team": "大宮アルディージャ",
"weather": "曇",
"series_number": 20,
"temperature": 25.9,
"away_score": 1,
"away_start_member": "江角　浩司,中村　北斗,菊地　光将,横山　知伸,高橋　祥平,橋本　晃司,和田　拓也,家長　昭博,富山　貴光,ムルジャ,ズラタン",
"home_score": 2,
"home_shoot": 13,
"game_id": "15844",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/08/16 19:04",
"referee": "池内　明彦"
},
{
"teams": [
"徳島ヴォルティス",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "長谷川　徹,藤原　広太朗,千代反田　充,村松　大輔,アレックス,斉藤　大介,エステバン,濱田　武,衛藤　裕,大﨑　淳矢,高崎　寛之",
"away_shoot": 10,
"home_director": "小林　伸二",
"away_team": "横浜Ｆ・マリノス",
"weather": "雨のち曇",
"series_number": 20,
"temperature": 26.8,
"away_score": 3,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,小椋　祥平,兵藤　慎剛,中村　俊輔,齋藤　学,ラフィーニャ",
"home_score": 0,
"home_shoot": 5,
"game_id": "15846",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/08/16 19:04",
"referee": "木村　博之"
},
{
"teams": [
"サガン鳥栖",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 12,
"home_director": "吉田　恵",
"away_team": "ＦＣ東京",
"weather": "曇",
"series_number": 20,
"temperature": 26.1,
"away_score": 2,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,平山　相太,武藤　嘉紀,渡邉　千真",
"home_score": 0,
"home_shoot": 8,
"game_id": "15847",
"home_team": "サガン鳥栖",
"game_start_at": "2014/08/16 19:04",
"referee": "山本　雄大"
},
{
"teams": [
"川崎フロンターレ",
"セレッソ大阪"
],
"away_director": "マルコ　ペッツァイオリ",
"home_start_member": "杉山　力裕,小宮山　尊信,實藤　友紀,谷口　彰悟,登里　享平,大島　僚太,中村　憲剛,森谷　賢太郎,レナト,小林　悠,大久保　嘉人",
"away_shoot": 11,
"home_director": "風間　八宏",
"away_team": "セレッソ大阪",
"weather": "曇",
"series_number": 20,
"temperature": 25.9,
"away_score": 4,
"away_start_member": "キム　ジンヒョン,藤本　康太,丸橋　祐介,安藤　淳,山下　達也,長谷川　アーリアジャスール,楠神　順平,キム　ソンジュン,永井　龍,フォルラン,南野　拓実",
"home_score": 5,
"home_shoot": 22,
"game_id": "15848",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/08/16 19:04",
"referee": "吉田　寿光"
},
{
"teams": [
"栃木ＳＣ",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "鈴木　智幸,菅　和範,赤井　秀行,岡根　直哉,鈴木　隆雅,中美　慶哉,本間　勲,小野寺　達也,近藤　祐介,廣瀬　浩二,大久保　哲哉",
"away_shoot": 19,
"home_director": "阪倉　裕二",
"away_team": "湘南ベルマーレ",
"weather": "曇",
"series_number": 27,
"temperature": 24.8,
"away_score": 3,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,亀川　諒史,菊地　俊介,岩尾　憲,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"home_score": 0,
"home_shoot": 9,
"game_id": "16262",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/08/17 18:03",
"referee": "飯田　淳平"
},
{
"teams": [
"東京ヴェルディ",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "キローラン　菜入,安西　幸輝,田村　直也,金　鐘必,安在　和樹,ニウド,鈴木　惇,澤井　直人,南　秀仁,杉本　竜士,常盤　聡",
"away_shoot": 14,
"home_director": "三浦　泰年",
"away_team": "水戸ホーリーホック",
"weather": "晴",
"series_number": 27,
"temperature": 27.4,
"away_score": 0,
"away_start_member": "本間　幸司,新里　亮,冨田　大介,田中　雄大,内田　航平,西岡　謙太,広瀬　陸斗,小谷野　顕治,船谷　圭祐,吉田　眞紀人,鈴木　隆行",
"home_score": 1,
"home_shoot": 12,
"game_id": "16264",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/08/17 18:03",
"referee": "上田　益也"
},
{
"teams": [
"横浜ＦＣ",
"カマタマーレ讃岐"
],
"away_director": "90'+6 讃岐 30 エブソン選手 ゴールキーパーとしてプレー",
"home_start_member": "南　雄太,市村　篤司,野上　結貴,ドウグラス,中島　崇典,寺田　紳一,松下　裕樹,松下　年宏,野村　直輝,野崎　陽介,パク　ソンホ",
"away_shoot": 14,
"home_director": "北野　誠",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 27,
"temperature": 27.6,
"away_score": 2,
"away_start_member": "石井　健太,ソン　ハンキ,藤井　航大,エブソン,沼田　圭悟,堀河　俊大,山本　翔平,岡村　和哉,小澤　雄希,持留　新作,我那覇　和樹",
"home_score": 4,
"home_shoot": 7,
"game_id": "16265",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/08/17 18:03",
"referee": "河合　英治"
},
{
"teams": [
"ギラヴァンツ北九州",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"away_shoot": 11,
"home_director": "柱谷　幸一",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 27,
"temperature": 26.3,
"away_score": 1,
"away_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,島田　譲,上田　康太,三村　真,片山　瑛一,妹尾　隆佑,清水　慎太郎",
"home_score": 2,
"home_shoot": 11,
"game_id": "16267",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/08/17 18:03",
"referee": "松尾　一"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "中村　隼,岡本　拓也,山口　貴弘,髙杉　亮太,古部　健太,三原　雅俊,奥埜　博亮,野田　紘史,佐藤　洸一,東　浩史,イ　ヨンジェ",
"away_shoot": 10,
"home_director": "高木　琢也",
"away_team": "アビスパ福岡",
"weather": "晴",
"series_number": 27,
"temperature": 28.1,
"away_score": 0,
"away_start_member": "神山　竜一,パク　ゴン,堤　俊輔,イ　グァンソン,古賀　正紘,中原　秀人,武田　英二郎,三島　勇太,酒井　宣福,城後　寿,坂田　大輔",
"home_score": 0,
"home_shoot": 14,
"game_id": "16268",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/08/17 18:03",
"referee": "小屋　幸栄"
},
{
"teams": [
"モンテディオ山形",
"コンサドーレ札幌"
],
"away_director": "財前　恵一",
"home_start_member": "山岸　範宏,山田　拓巳,西河　翔吾,石井　秀典,石川　竜也,宮阪　政樹,ロメロ　フランク,松岡　亮輔,秋葉　勝,ディエゴ,中島　裕希",
"away_shoot": 11,
"home_director": "石﨑　信弘",
"away_team": "コンサドーレ札幌",
"weather": "曇",
"series_number": 27,
"temperature": 24.1,
"away_score": 1,
"away_start_member": "李　昊乗,石井　謙伍,パウロン,奈良　竜樹,上原　慎也,深井　一希,上里　一将,荒野　拓馬,宮澤　裕樹,菊岡　拓朗,内村　圭宏",
"home_score": 2,
"home_shoot": 15,
"game_id": "16261",
"home_team": "モンテディオ山形",
"game_start_at": "2014/08/17 18:04",
"referee": "西村　雄一"
},
{
"teams": [
"ザスパクサツ群馬",
"ＦＣ岐阜"
],
"away_director": "90'+2 退席 群馬 土屋　明大 （ＧＫコーチ）",
"home_start_member": "富居　大樹,小柳　達司,クォン　ハンジン,青木　良太,瀬川　和樹,坂井　洋平,黄　誠秀,小林　竜樹,青木　孝太,ダニエル　ロビーニョ,宮崎　泰右",
"away_shoot": 13,
"home_director": "ラモス　瑠偉",
"away_team": "ＦＣ岐阜",
"weather": "晴",
"series_number": 27,
"temperature": 26.2,
"away_score": 2,
"away_start_member": "川口　能活,木谷　公亮,中村　英之,阿部　正紀,益山　司,ヘニキ,宮沢　正史,田中　秀人,遠藤　純輝,髙地　系治,ナザリト",
"home_score": 2,
"home_shoot": 11,
"game_id": "16263",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/08/17 18:04",
"referee": "吉田　哲朗"
},
{
"teams": [
"愛媛ＦＣ",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "児玉　剛,村上　佑介,ハン　ヒフン,西岡　大輝,三原　向平,渡邊　一仁,吉村　圭司,堀米　勇輝,藤　直也,リカルド　ロボ,河原　和寿",
"away_shoot": 18,
"home_director": "石丸　清隆",
"away_team": "松本山雅ＦＣ",
"weather": "晴",
"series_number": 27,
"temperature": 27.1,
"away_score": 4,
"away_start_member": "村山　智彦,田中　隼磨,飯田　真輝,犬飼　智也,多々良　敦斗,岩上　祐三,岩間　雄大,喜山　康平,岩沼　俊介,船山　貴之,サビア",
"home_score": 1,
"home_shoot": 9,
"game_id": "16266",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/08/17 18:04",
"referee": "森川　浩次"
},
{
"teams": [
"ロアッソ熊本",
"ジェフユナイテッド千葉"
],
"away_director": "関塚　隆",
"home_start_member": "畑　実,藏川　洋平,篠原　弘次郎,園田　拓也,片山　奨典,澤田　崇,養父　雄仁,キム　ビョンヨン,仲間　隼斗,巻　誠一郎,齊藤　和樹",
"away_shoot": 12,
"home_director": "小野　剛",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 27,
"temperature": 27,
"away_score": 0,
"away_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,谷澤　達也,山中　亮輔,大塚　翔平,ケンペス",
"home_score": 0,
"home_shoot": 12,
"game_id": "16271",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/08/17 19:03",
"referee": "廣瀬　格"
},
{
"teams": [
"ジュビロ磐田",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "八田　直樹,駒野　友一,藤田　義明,森下　俊,坪内　秀介,フェルジナンド,小林　祐希,ペク　ソンドン,松井　大輔,山崎　亮平,前田　遼一",
"away_shoot": 11,
"home_director": "シャムスカ",
"away_team": "カターレ富山",
"weather": "曇",
"series_number": 27,
"temperature": 27.3,
"away_score": 2,
"away_start_member": "柴田　大地,池端　陽介,秋本　倫孝,高　准翼,木村　勝太,井澤　惇,平出　涼,内田　健太,宮吉　拓実,中島　翔哉,白崎　凌兵",
"home_score": 3,
"home_shoot": 16,
"game_id": "16269",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/08/17 19:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"京都サンガF.C.",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "オ　スンフン,駒井　善成,内野　貴志,酒井　隆介,石櫃　洋祐,中山　博貴,田中　英雄,山瀬　功治,石田　雅俊,工藤　浩平,大黒　将志",
"away_shoot": 10,
"home_director": "川勝　良一",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 27,
"temperature": 28.8,
"away_score": 2,
"away_start_member": "武田　洋平,安川　有,高木　和道,若狭　大志,伊藤　大介,松本　怜,為田　大貴,松本　昌也,風間　宏矢,木島　悠,林　容平",
"home_score": 2,
"home_shoot": 21,
"game_id": "16270",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/08/17 19:04",
"referee": "野田　祐樹"
},
{
"teams": [
"清水エスパルス",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "櫛引　政敏,吉田　豊,平岡　康裕,ヤコヴィッチ,イ　キジェ,本田　拓也,六平　光成,大前　元紀,河井　陽介,石毛　秀樹,ノヴァコヴィッチ",
"away_shoot": 10,
"home_director": "大榎　克己",
"away_team": "鹿島アントラーズ",
"weather": "曇",
"series_number": 21,
"temperature": 22.6,
"away_score": 3,
"away_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,カイオ,中村　充孝,土居　聖真,ダヴィ",
"home_score": 1,
"home_shoot": 10,
"game_id": "15853",
"home_team": "清水エスパルス",
"game_start_at": "2014/08/23 18:04",
"referee": "井上　知大"
},
{
"teams": [
"ＦＣ東京",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,河野　広貴,平山　相太,武藤　嘉紀",
"away_shoot": 16,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "浦和レッズ",
"weather": "晴",
"series_number": 21,
"temperature": 27,
"away_score": 4,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,鈴木　啓太,宇賀神　友弥,柏木　陽介,梅崎　司,興梠　慎三",
"home_score": 4,
"home_shoot": 11,
"game_id": "15850",
"home_team": "ＦＣ東京",
"game_start_at": "2014/08/23 18:34",
"referee": "岡部　拓人"
},
{
"teams": [
"ヴァンフォーレ甲府",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,ジウシーニョ,保坂　一成,稲垣　祥,阿部　翔平,下田　北斗,石原　克哉,盛田　剛平",
"away_shoot": 11,
"home_director": "城福　浩",
"away_team": "ガンバ大阪",
"weather": "曇",
"series_number": 21,
"temperature": 24.8,
"away_score": 3,
"away_start_member": "東口　順昭,米倉　恒貴,西野　貴治,岩下　敬輔,藤春　廣輝,今野　泰幸,遠藤　保仁,岡崎　建哉,倉田　秋,宇佐美　貴史,パトリック",
"home_score": 3,
"home_shoot": 13,
"game_id": "15851",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/08/23 18:34",
"referee": "榎本　一慶"
},
{
"teams": [
"ヴィッセル神戸",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "山本　海人,河本　裕之,増川　隆洋,チョン　ウヨン,枝村　匠馬,橋本　英郎,森岡　亮太,シンプリシオ,大屋　翼,ペドロ　ジュニオール,マルキーニョス",
"away_shoot": 17,
"home_director": "安達　亮",
"away_team": "ベガルタ仙台",
"weather": "晴",
"series_number": 21,
"temperature": 27.6,
"away_score": 1,
"away_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,角田　誠,梁　勇基,野沢　拓也,武藤　雄樹",
"home_score": 2,
"home_shoot": 8,
"game_id": "15855",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/08/23 19:03",
"referee": "西村　雄一"
},
{
"teams": [
"大宮アルディージャ",
"サガン鳥栖"
],
"away_director": "吉田　恵",
"home_start_member": "北野　貴之,趙　源熙,菊地　光将,横山　知伸,高橋　祥平,ズラタン,和田　拓也,金澤　慎,泉澤　仁,家長　昭博,ムルジャ",
"away_shoot": 8,
"home_director": "大熊　清",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 21,
"temperature": 27.3,
"away_score": 3,
"away_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,坂井　達弥,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 1,
"home_shoot": 12,
"game_id": "15849",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/08/23 19:04",
"referee": "今村　義朗"
},
{
"teams": [
"アルビレックス新潟",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,大野　和成,レオ　シルバ,小林　裕紀,山本　康裕,田中　亜土夢,成岡　翔,岡本　英也",
"away_shoot": 6,
"home_director": "柳下　正明",
"away_team": "徳島ヴォルティス",
"weather": "曇",
"series_number": 21,
"temperature": 27.4,
"away_score": 2,
"away_start_member": "長谷川　徹,藤原　広太朗,福元　洋平,村松　大輔,アレックス,エステバン,濱田　武,衛藤　裕,大﨑　淳矢,アドリアーノ,高崎　寛之",
"home_score": 1,
"home_shoot": 7,
"game_id": "15852",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/08/23 19:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"名古屋グランパス",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,川又　堅碁,田口　泰士,ダニルソン,レアンドロ　ドミンゲス,ケネディ,永井　謙佑",
"away_shoot": 13,
"home_director": "西野　朗",
"away_team": "柏レイソル",
"weather": "雨",
"series_number": 21,
"temperature": 24.3,
"away_score": 1,
"away_start_member": "菅野　孝憲,藤田　優人,鈴木　大輔,増嶋　竜也,橋本　和,小林　祐介,エドゥアルド,大谷　秀和,高山　薫,工藤　壮人,レアンドロ",
"home_score": 1,
"home_shoot": 13,
"game_id": "15854",
"home_team": "名古屋グランパス",
"game_start_at": "2014/08/23 19:04",
"referee": "松尾　一"
},
{
"teams": [
"横浜Ｆ・マリノス",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,小椋　祥平,藤本　淳吾,中村　俊輔,齋藤　学,ラフィーニャ",
"away_shoot": 10,
"home_director": "樋口　靖洋",
"away_team": "川崎フロンターレ",
"weather": "晴",
"series_number": 21,
"temperature": 26.4,
"away_score": 0,
"away_start_member": "杉山　力裕,小宮山　尊信,實藤　友紀,ジェシ,大島　僚太,中村　憲剛,森谷　賢太郎,登里　享平,小林　悠,レナト,大久保　嘉人",
"home_score": 2,
"home_shoot": 17,
"game_id": "15856",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/08/23 19:04",
"referee": "家本　政明"
},
{
"teams": [
"サンフレッチェ広島",
"セレッソ大阪"
],
"away_director": "マルコ　ペッツァイオリ",
"home_start_member": "林　卓人,宮原　和也,千葉　和彦,水本　裕貴,ミキッチ,柴﨑　晃誠,森﨑　和幸,柏　好文,森﨑　浩司,髙萩　洋次郎,皆川　佑介",
"away_shoot": 12,
"home_director": "森保　一",
"away_team": "セレッソ大阪",
"weather": "晴",
"series_number": 21,
"temperature": 25.6,
"away_score": 0,
"away_start_member": "キム　ジンヒョン,藤本　康太,丸橋　祐介,安藤　淳,山下　達也,扇原　貴宏,長谷川　アーリアジャスール,キム　ソンジュン,フォルラン,平野　甲斐,カカウ",
"home_score": 0,
"home_shoot": 3,
"game_id": "15857",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/08/23 19:04",
"referee": "飯田　淳平"
},
{
"teams": [
"東京ヴェルディ",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "キローラン　菜入,安西　幸輝,田村　直也,井林　章,安在　和樹,ニウド,鈴木　惇,澤井　直人,南　秀仁,杉本　竜士,常盤　聡",
"away_shoot": 10,
"home_director": "三浦　泰年",
"away_team": "横浜ＦＣ",
"weather": "曇",
"series_number": 28,
"temperature": 28.1,
"away_score": 1,
"away_start_member": "南　雄太,市村　篤司,野上　結貴,ドウグラス,中島　崇典,寺田　紳一,松下　裕樹,松下　年宏,小池　純輝,野崎　陽介,パク　ソンホ",
"home_score": 1,
"home_shoot": 13,
"game_id": "16273",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/08/24 18:03",
"referee": "塚田　智宏"
},
{
"teams": [
"松本山雅ＦＣ",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "村山　智彦,田中　隼磨,飯田　真輝,多々良　敦斗,犬飼　智也,岩上　祐三,岩間　雄大,岩沼　俊介,喜山　康平,船山　貴之,サビア",
"away_shoot": 15,
"home_director": "反町　康治",
"away_team": "モンテディオ山形",
"weather": "曇時々雨",
"series_number": 28,
"temperature": 21.6,
"away_score": 0,
"away_start_member": "山岸　範宏,山田　拓巳,石井　秀典,西河　翔吾,石川　竜也,宮阪　政樹,ロメロ　フランク,松岡　亮輔,秋葉　勝,ディエゴ,中島　裕希",
"home_score": 0,
"home_shoot": 18,
"game_id": "16274",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/08/24 18:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"カマタマーレ讃岐",
"京都サンガF.C."
],
"away_director": "川勝　良一",
"home_start_member": "瀬口　拓弥,武田　有祐,藤井　航大,エブソン,沼田　圭悟,綱田　大志,山本　翔平,岡村　和哉,小澤　雄希,西野　泰正,木島　良輔",
"away_shoot": 11,
"home_director": "北野　誠",
"away_team": "京都サンガF.C.",
"weather": "曇",
"series_number": 28,
"temperature": 28,
"away_score": 2,
"away_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,内野　貴志,駒井　善成,中山　博貴,田中　英雄,山瀬　功治,石田　雅俊,工藤　浩平,大黒　将志",
"home_score": 2,
"home_shoot": 9,
"game_id": "16276",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/08/24 18:03",
"referee": "篠藤　巧"
},
{
"teams": [
"ギラヴァンツ北九州",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"away_shoot": 13,
"home_director": "柱谷　幸一",
"away_team": "Ｖ・ファーレン長崎",
"weather": "曇",
"series_number": 28,
"temperature": 26.3,
"away_score": 1,
"away_start_member": "大久保　択生,岡本　拓也,山口　貴弘,髙杉　亮太,古部　健太,黒木　聖仁,三原　雅俊,野田　紘史,東　浩史,奥埜　博亮,イ　ヨンジェ",
"home_score": 2,
"home_shoot": 7,
"game_id": "16278",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/08/24 18:03",
"referee": "高山　啓義"
},
{
"teams": [
"大分トリニータ",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "武田　洋平,安川　有,高木　和道,若狭　大志,松本　怜,土岐田　洸平,為田　大貴,伊藤　大介,風間　宏矢,木島　悠,林　容平",
"away_shoot": 15,
"home_director": "田坂　和昭",
"away_team": "ザスパクサツ群馬",
"weather": "曇",
"series_number": 28,
"temperature": 27.1,
"away_score": 1,
"away_start_member": "富居　大樹,小柳　達司,クォン　ハンジン,青木　良太,瀬川　和樹,坂井　洋平,黄　誠秀,小林　竜樹,青木　孝太,ダニエル　ロビーニョ,宮崎　泰右",
"home_score": 2,
"home_shoot": 10,
"game_id": "16279",
"home_team": "大分トリニータ",
"game_start_at": "2014/08/24 18:03",
"referee": "長谷　拓"
},
{
"teams": [
"水戸ホーリーホック",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "本間　幸司,新里　亮,冨田　大介,細川　淳矢,田中　雄大,内田　航平,中里　崇宏,広瀬　陸斗,吉田　眞紀人,三島　康平,馬場　賢治",
"away_shoot": 9,
"home_director": "柱谷　哲二",
"away_team": "愛媛ＦＣ",
"weather": "曇",
"series_number": 28,
"temperature": 27.4,
"away_score": 0,
"away_start_member": "大西　勝俉,三原　向平,村上　佑介,林堂　眞,浦田　延尚,キム　ミンジェ,渡邊　一仁,吉村　圭司,堀米　勇輝,リカルド　ロボ,河原　和寿",
"home_score": 0,
"home_shoot": 15,
"game_id": "16272",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/08/24 18:04",
"referee": "岡　宏道"
},
{
"teams": [
"カターレ富山",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "廣永　遼太郎,木村　勝太,秋本　倫孝,高　准翼,前　貴之,井澤　惇,平出　涼,國吉　貴博,宮吉　拓実,中島　翔哉,白崎　凌兵",
"away_shoot": 11,
"home_director": "安間　貴義",
"away_team": "ロアッソ熊本",
"weather": "雨",
"series_number": 28,
"temperature": 24.8,
"away_score": 2,
"away_start_member": "畑　実,藏川　洋平,園田　拓也,橋本　拳人,片山　奨典,髙柳　一誠,養父　雄仁,キム　ビョンヨン,仲間　隼斗,澤田　崇,齊藤　和樹",
"home_score": 0,
"home_shoot": 9,
"game_id": "16275",
"home_team": "カターレ富山",
"game_start_at": "2014/08/24 18:04",
"referee": "塚田　健太"
},
{
"teams": [
"アビスパ福岡",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "神山　竜一,阿部　巧,パク　ゴン,堤　俊輔,古賀　正紘,中原　秀人,三島　勇太,武田　英二郎,坂田　大輔,城後　寿,金森　健志",
"away_shoot": 10,
"home_director": "マリヤン　プシュニク",
"away_team": "ＦＣ岐阜",
"weather": "雨のち曇",
"series_number": 28,
"temperature": 26.4,
"away_score": 0,
"away_start_member": "川口　能活,木谷　公亮,中村　英之,阿部　正紀,ヘニキ,水野　泰輔,益山　司,髙地　系治,森　勇介,遠藤　純輝,ナザリト",
"home_score": 1,
"home_shoot": 7,
"game_id": "16277",
"home_team": "アビスパ福岡",
"game_start_at": "2014/08/24 18:04",
"referee": "三上　正一郎"
},
{
"teams": [
"ファジアーノ岡山",
"ジェフユナイテッド千葉"
],
"away_director": "関塚　隆",
"home_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,押谷　祐樹,石原　崇兆,清水　慎太郎",
"away_shoot": 9,
"home_director": "影山　雅永",
"away_team": "ジェフユナイテッド千葉",
"weather": "雨",
"series_number": 28,
"temperature": 24.8,
"away_score": 0,
"away_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,幸野　志有人,ケンペス",
"home_score": 1,
"home_shoot": 15,
"game_id": "16281",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/08/24 19:03",
"referee": "村上　伸次"
},
{
"teams": [
"湘南ベルマーレ",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,菊池　大介,菊地　俊介,岩尾　憲,亀川　諒史,岡田　翔平,ウェリントン,武富　孝介",
"away_shoot": 3,
"home_director": "曺　貴裁",
"away_team": "ジュビロ磐田",
"weather": "晴",
"series_number": 28,
"temperature": 27.9,
"away_score": 1,
"away_start_member": "八田　直樹,櫻内　渚,坪内　秀介,森下　俊,宮崎　智彦,小林　祐希,フェルジナンド,藤田　義明,ペク　ソンドン,山崎　亮平,前田　遼一",
"home_score": 1,
"home_shoot": 13,
"game_id": "16280",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/08/24 19:04",
"referee": "吉田　寿光"
},
{
"teams": [
"コンサドーレ札幌",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "金山　隼樹,石井　謙伍,パウロン,奈良　竜樹,上原　慎也,河合　竜二,宮澤　裕樹,荒野　拓馬,前田　俊介,小野　伸二,内村　圭宏",
"away_shoot": 10,
"home_director": "財前　恵一",
"away_team": "栃木ＳＣ",
"weather": "屋内",
"series_number": 28,
"temperature": 23.7,
"away_score": 1,
"away_start_member": "鈴木　智幸,イ　ミンス,チャ　ヨンファン,赤井　秀行,荒堀　謙次,廣瀬　浩二,小野寺　達也,本間　勲,近藤　祐介,西川　優大,大久保　哲哉",
"home_score": 1,
"home_shoot": 13,
"game_id": "16282",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/08/25 19:03",
"referee": "窪田　陽輔"
},
{
"teams": [
"浦和レッズ",
"大宮アルディージャ"
],
"away_director": "大熊　清",
"home_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,鈴木　啓太,宇賀神　友弥,柏木　陽介,梅崎　司,興梠　慎三",
"away_shoot": 15,
"home_director": "ペトロヴィッチ",
"away_team": "大宮アルディージャ",
"weather": "晴",
"series_number": 22,
"temperature": 22.8,
"away_score": 0,
"away_start_member": "北野　貴之,中村　北斗,菊地　光将,高橋　祥平,高瀬　優孝,金澤　慎,和田　拓也,渡邉　大剛,家長　昭博,ズラタン,ムルジャ",
"home_score": 4,
"home_shoot": 13,
"game_id": "15859",
"home_team": "浦和レッズ",
"game_start_at": "2014/08/30 18:04",
"referee": "吉田　寿光"
},
{
"teams": [
"ガンバ大阪",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "東口　順昭,米倉　恒貴,西野　貴治,岩下　敬輔,藤春　廣輝,今野　泰幸,遠藤　保仁,倉田　秋,二川　孝広,宇佐美　貴史,パトリック",
"away_shoot": 12,
"home_director": "長谷川　健太",
"away_team": "アルビレックス新潟",
"weather": "晴",
"series_number": 22,
"temperature": 25.3,
"away_score": 0,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,宋　株熏,大野　和成,小林　裕紀,小泉　慶,山本　康裕,田中　亜土夢,岡本　英也,指宿　洋史",
"home_score": 5,
"home_shoot": 12,
"game_id": "15861",
"home_team": "ガンバ大阪",
"game_start_at": "2014/08/30 18:04",
"referee": "福島　孝一郎"
},
{
"teams": [
"徳島ヴォルティス",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "長谷川　徹,藤原　広太朗,福元　洋平,村松　大輔,アレックス,濱田　武,エステバン,衛藤　裕,大﨑　淳矢,高崎　寛之,アドリアーノ",
"away_shoot": 8,
"home_director": "小林　伸二",
"away_team": "サンフレッチェ広島",
"weather": "晴",
"series_number": 22,
"temperature": 26.2,
"away_score": 1,
"away_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,ミキッチ,柴﨑　晃誠,森﨑　和幸,柏　好文,森﨑　浩司,髙萩　洋次郎,皆川　佑介",
"home_score": 0,
"home_shoot": 7,
"game_id": "15866",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/08/30 18:34",
"referee": "窪田　陽輔"
},
{
"teams": [
"柏レイソル",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "菅野　孝憲,鈴木　大輔,近藤　直也,エドゥアルド,橋本　和,太田　徹郎,茨田　陽生,大谷　秀和,高山　薫,レアンドロ,工藤　壮人",
"away_shoot": 8,
"home_director": "ネルシーニョ",
"away_team": "ヴァンフォーレ甲府",
"weather": "曇",
"series_number": 22,
"temperature": 22.8,
"away_score": 0,
"away_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,ジウシーニョ,新井　涼平,マルキーニョス　パラナ,阿部　翔平,稲垣　祥,石原　克哉,クリスティアーノ",
"home_score": 3,
"home_shoot": 9,
"game_id": "15860",
"home_team": "柏レイソル",
"game_start_at": "2014/08/30 19:03",
"referee": "廣瀬　格"
},
{
"teams": [
"鹿島アントラーズ",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "曽ヶ端　準,西　大伍,山村　和也,昌子　源,山本　脩斗,梅鉢　貴秀,柴崎　岳,カイオ,ジョルジ　ワグネル,土居　聖真,ダヴィ",
"away_shoot": 10,
"home_director": "トニーニョ　セレーゾ",
"away_team": "ＦＣ東京",
"weather": "曇",
"series_number": 22,
"temperature": 22.2,
"away_score": 2,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,河野　広貴,渡邉　千真,武藤　嘉紀",
"home_score": 2,
"home_shoot": 17,
"game_id": "15858",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/08/30 19:04",
"referee": "飯田　淳平"
},
{
"teams": [
"サガン鳥栖",
"清水エスパルス"
],
"away_director": "大榎　克己",
"home_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,坂井　達弥,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 8,
"home_director": "吉田　恵",
"away_team": "清水エスパルス",
"weather": "晴",
"series_number": 22,
"temperature": 25.6,
"away_score": 2,
"away_start_member": "櫛引　政敏,ヤコヴィッチ,平岡　康裕,三浦　弦太,吉田　豊,本田　拓也,六平　光成,石毛　秀樹,大前　元紀,ノヴァコヴィッチ,高木　俊幸",
"home_score": 2,
"home_shoot": 11,
"game_id": "15862",
"home_team": "サガン鳥栖",
"game_start_at": "2014/08/30 19:04",
"referee": "村上　伸次"
},
{
"teams": [
"ベガルタ仙台",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,角田　誠,梁　勇基,武藤　雄樹,ウイルソン",
"away_shoot": 14,
"home_director": "渡邉　晋",
"away_team": "横浜Ｆ・マリノス",
"weather": "曇",
"series_number": 22,
"temperature": 23,
"away_score": 2,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,中町　公祐,小椋　祥平,藤本　淳吾,中村　俊輔,兵藤　慎剛,伊藤　翔",
"home_score": 1,
"home_shoot": 9,
"game_id": "15863",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/08/30 19:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"名古屋グランパス",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,矢田　旭,田口　泰士,ダニルソン,永井　謙佑,玉田　圭司,川又　堅碁",
"away_shoot": 13,
"home_director": "西野　朗",
"away_team": "川崎フロンターレ",
"weather": "曇",
"series_number": 22,
"temperature": 24.9,
"away_score": 1,
"away_start_member": "杉山　力裕,實藤　友紀,谷口　彰悟,井川　祐輔,大島　僚太,中村　憲剛,森谷　賢太郎,小宮山　尊信,小林　悠,レナト,大久保　嘉人",
"home_score": 1,
"home_shoot": 11,
"game_id": "15864",
"home_team": "名古屋グランパス",
"game_start_at": "2014/08/30 19:04",
"referee": "岡部　拓人"
},
{
"teams": [
"セレッソ大阪",
"ヴィッセル神戸"
],
"away_director": "*** Ｃ大阪 21 キム　ジンヒョンの警告は試合終了後の警告",
"home_start_member": "キム　ジンヒョン,藤本　康太,丸橋　祐介,安藤　淳,山下　達也,扇原　貴宏,長谷川　アーリアジャスール,フォルラン,南野　拓実,平野　甲斐,カカウ",
"away_shoot": 10,
"home_director": "安達　亮",
"away_team": "ヴィッセル神戸",
"weather": "晴",
"series_number": 22,
"temperature": 26.4,
"away_score": 2,
"away_start_member": "山本　海人,高橋　峻希,岩波　拓也,増川　隆洋,シンプリシオ,チョン　ウヨン,枝村　匠馬,橋本　英郎,森岡　亮太,マルキーニョス,ペドロ　ジュニオール",
"home_score": 1,
"home_shoot": 10,
"game_id": "15865",
"home_team": "セレッソ大阪",
"game_start_at": "2014/08/30 19:04",
"referee": "木村　博之"
},
{
"teams": [
"横浜ＦＣ",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "南　雄太,市村　篤司,野上　結貴,松下　裕樹,中島　崇典,寺田　紳一,安　英学,松下　年宏,小池　純輝,野村　直輝,パク　ソンホ",
"away_shoot": 6,
"home_director": "山口　素弘",
"away_team": "アビスパ福岡",
"weather": "晴",
"series_number": 29,
"temperature": 23.9,
"away_score": 0,
"away_start_member": "神山　竜一,阿部　巧,パク　ゴン,堤　俊輔,古賀　正紘,中原　秀人,武田　英二郎,三島　勇太,坂田　大輔,城後　寿,金森　健志",
"home_score": 2,
"home_shoot": 11,
"game_id": "16284",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/08/31 18:03",
"referee": "森川　浩次"
},
{
"teams": [
"カマタマーレ讃岐",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "瀬口　拓弥,武田　有祐,エブソン,藤井　航大,沼田　圭悟,関原　凌河,岡村　和哉,山本　翔平,小澤　雄希,木島　良輔,高橋　泰",
"away_shoot": 12,
"home_director": "北野　誠",
"away_team": "ファジアーノ岡山",
"weather": "曇",
"series_number": 29,
"temperature": 27.7,
"away_score": 1,
"away_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,押谷　祐樹,石原　崇兆,清水　慎太郎",
"home_score": 2,
"home_shoot": 9,
"game_id": "16286",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/08/31 18:03",
"referee": "岡　宏道"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "大久保　択生,岡本　拓也,山口　貴弘,髙杉　亮太,古部　健太,三原　雅俊,前田　悠佑,野田　紘史,東　浩史,スティッペ,イ　ヨンジェ",
"away_shoot": 4,
"home_director": "高木　琢也",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 29,
"temperature": 27.7,
"away_score": 0,
"away_start_member": "廣永　遼太郎,木村　勝太,御厨　貴文,高　准翼,平出　涼,井澤　惇,前　貴之,國吉　貴博,白崎　凌兵,宮吉　拓実,木本　敬介",
"home_score": 2,
"home_shoot": 12,
"game_id": "16287",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/08/31 18:03",
"referee": "三上　正一郎"
},
{
"teams": [
"モンテディオ山形",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "山岸　範宏,山田　拓巳,石井　秀典,西河　翔吾,石川　竜也,宮阪　政樹,ロメロ　フランク,松岡　亮輔,秋葉　勝,ディエゴ,中島　裕希",
"away_shoot": 20,
"home_director": "石﨑　信弘",
"away_team": "湘南ベルマーレ",
"weather": "晴",
"series_number": 29,
"temperature": 22.3,
"away_score": 3,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,岩尾　憲,菊地　俊介,菊池　大介,岡田　翔平,ウェリントン,樋口　寛規",
"home_score": 1,
"home_shoot": 10,
"game_id": "16283",
"home_team": "モンテディオ山形",
"game_start_at": "2014/08/31 18:04",
"referee": "東城　穣"
},
{
"teams": [
"ＦＣ岐阜",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "川口　能活,ヘニキ,田中　秀人,阿部　正紀,水野　泰輔,宮沢　正史,益山　司,髙地　系治,太田　圭輔,難波　宏明,ナザリト",
"away_shoot": 5,
"home_director": "ラモス　瑠偉",
"away_team": "東京ヴェルディ",
"weather": "晴",
"series_number": 29,
"temperature": 26,
"away_score": 0,
"away_start_member": "ポープ　ウィリアム,田村　直也,金　鐘必,井林　章,安在　和樹,ニウド,楠美　圭史,安西　幸輝,南　秀仁,杉本　竜士,常盤　聡",
"home_score": 3,
"home_shoot": 9,
"game_id": "16285",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/08/31 18:04",
"referee": "家本　政明"
},
{
"teams": [
"ジェフユナイテッド千葉",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,オナイウ　阿道,森本　貴幸",
"away_shoot": 22,
"home_director": "関塚　隆",
"away_team": "水戸ホーリーホック",
"weather": "晴",
"series_number": 29,
"temperature": 22.8,
"away_score": 0,
"away_start_member": "本間　幸司,細川　淳矢,冨田　大介,新里　亮,田中　雄大,西岡　謙太,内田　航平,広瀬　陸斗,小澤　司,吉田　眞紀人,三島　康平",
"home_score": 1,
"home_shoot": 7,
"game_id": "16288",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/08/31 19:03",
"referee": "井上　知大"
},
{
"teams": [
"ロアッソ熊本",
"コンサドーレ札幌"
],
"away_director": "名塚　善寛",
"home_start_member": "畑　実,藏川　洋平,園田　拓也,橋本　拳人,片山　奨典,中山　雄登,養父　雄仁,髙柳　一誠,仲間　隼斗,澤田　崇,巻　誠一郎",
"away_shoot": 9,
"home_director": "小野　剛",
"away_team": "コンサドーレ札幌",
"weather": "曇",
"series_number": 29,
"temperature": 25.2,
"away_score": 2,
"away_start_member": "金山　隼樹,上原　慎也,櫛引　一紀,奈良　竜樹,上原　拓郎,河合　竜二,宮澤　裕樹,中原　彰吾,前田　俊介,砂川　誠,都倉　賢",
"home_score": 0,
"home_shoot": 8,
"game_id": "16292",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/08/31 19:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"ジュビロ磐田",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "八田　直樹,坪内　秀介,藤田　義明,森下　俊,櫻内　渚,フェルジナンド,小林　祐希,宮崎　智彦,チンガ,前田　遼一,ペク　ソンドン",
"away_shoot": 7,
"home_director": "シャムスカ",
"away_team": "栃木ＳＣ",
"weather": "曇",
"series_number": 29,
"temperature": 22.7,
"away_score": 3,
"away_start_member": "鈴木　智幸,イ　ミンス,赤井　秀行,チャ　ヨンファン,荒堀　謙次,中美　慶哉,西澤　代志也,小野寺　達也,近藤　祐介,杉本　真,西川　優大",
"home_score": 2,
"home_shoot": 17,
"game_id": "16289",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/08/31 19:04",
"referee": "上田　益也"
},
{
"teams": [
"京都サンガF.C.",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,駒井　善成,田中　英雄,中山　博貴,山瀬　功治,横谷　繁,ドウグラス,大黒　将志",
"away_shoot": 6,
"home_director": "川勝　良一",
"away_team": "ギラヴァンツ北九州",
"weather": "晴",
"series_number": 29,
"temperature": 26,
"away_score": 1,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"home_score": 1,
"home_shoot": 14,
"game_id": "16290",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/08/31 19:04",
"referee": "西村　雄一"
},
{
"teams": [
"愛媛ＦＣ",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "大西　勝俉,村上　佑介,林堂　眞,浦田　延尚,三原　向平,渡邊　一仁,村上　巧,堀米　勇輝,藤　直也,リカルド　ロボ,河原　和寿",
"away_shoot": 9,
"home_director": "石丸　清隆",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 29,
"temperature": 24.6,
"away_score": 2,
"away_start_member": "武田　洋平,安川　有,高木　和道,若狭　大志,土岐田　洸平,伊藤　大介,為田　大貴,松本　昌也,風間　宏矢,木島　悠,林　容平",
"home_score": 1,
"home_shoot": 13,
"game_id": "16291",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/08/31 19:04",
"referee": "高山　啓義"
},
{
"teams": [
"ザスパクサツ群馬",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "富居　大樹,小柳　達司,クォン　ハンジン,青木　良太,瀬川　和樹,小林　竜樹,加藤　弘堅,坂井　洋平,宮崎　泰右,エデル,青木　孝太",
"away_shoot": 12,
"home_director": "秋葉　忠宏",
"away_team": "松本山雅ＦＣ",
"weather": "曇のち雨",
"series_number": 29,
"temperature": 23.4,
"away_score": 3,
"away_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,多々良　敦斗,岩間　雄大,喜山　康平,岩上　祐三,岩沼　俊介,船山　貴之,サビア",
"home_score": 1,
"home_shoot": 5,
"game_id": "16293",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/08/31 19:34",
"referee": "松尾　一"
},
{
"teams": [
"水戸ホーリーホック",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "本間　幸司,新里　亮,冨田　大介,細川　淳矢,田中　雄大,西岡　謙太,船谷　圭祐,広瀬　陸斗,吉田　眞紀人,三島　康平,馬場　賢治",
"away_shoot": 17,
"home_director": "柱谷　哲二",
"away_team": "モンテディオ山形",
"weather": "晴",
"series_number": 30,
"temperature": 24.2,
"away_score": 1,
"away_start_member": "山岸　範宏,舩津　徹也,當間　建文,石井　秀典,石川　竜也,宮阪　政樹,ロメロ　フランク,松岡　亮輔,比嘉　厚平,萬代　宏樹,中島　裕希",
"home_score": 0,
"home_shoot": 5,
"game_id": "16295",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/09/06 18:03",
"referee": "長谷　拓"
},
{
"teams": [
"栃木ＳＣ",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "鈴木　智幸,イ　ミンス,赤井　秀行,チャ　ヨンファン,荒堀　謙次,中美　慶哉,西澤　代志也,小野寺　達也,近藤　祐介,杉本　真,西川　優大",
"away_shoot": 9,
"home_director": "阪倉　裕二",
"away_team": "愛媛ＦＣ",
"weather": "晴一時雨",
"series_number": 30,
"temperature": 26.5,
"away_score": 3,
"away_start_member": "大西　勝俉,三原　向平,村上　佑介,林堂　眞,浦田　延尚,キム　ミンジェ,原川　力,江口　直生,堀米　勇輝,西田　剛,河原　和寿",
"home_score": 3,
"home_shoot": 13,
"game_id": "16296",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/09/06 18:03",
"referee": "小屋　幸栄"
},
{
"teams": [
"東京ヴェルディ",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "佐藤　優也,田村　直也,金　鐘必,井林　章,安在　和樹,ニウド,鈴木　惇,澤井　直人,南　秀仁,杉本　竜士,常盤　聡",
"away_shoot": 9,
"home_director": "三浦　泰年",
"away_team": "カマタマーレ讃岐",
"weather": "雨",
"series_number": 30,
"temperature": 26.3,
"away_score": 1,
"away_start_member": "瀬口　拓弥,藤井　大輔,藤井　航大,エブソン,沼田　圭悟,堀河　俊大,山本　翔平,岡村　和哉,小澤　雄希,西野　泰正,木島　良輔",
"home_score": 0,
"home_shoot": 11,
"game_id": "16297",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/09/06 18:03",
"referee": "井上　知大"
},
{
"teams": [
"横浜ＦＣ",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "南　雄太,小池　純輝,野上　結貴,松下　裕樹,中島　崇典,寺田　紳一,安　英学,松下　年宏,内田　智也,野村　直輝,パク　ソンホ",
"away_shoot": 5,
"home_director": "山口　素弘",
"away_team": "ザスパクサツ群馬",
"weather": "曇一時雨",
"series_number": 30,
"temperature": 26.5,
"away_score": 0,
"away_start_member": "富居　大樹,有薗　真吾,青木　良太,黄　誠秀,小柳　達司,加藤　弘堅,青木　孝太,宮崎　泰右,瀬川　和樹,平繁　龍一,小林　竜樹",
"home_score": 1,
"home_shoot": 10,
"game_id": "16298",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/09/06 18:03",
"referee": "野田　祐樹"
},
{
"teams": [
"ギラヴァンツ北九州",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,市川　恵多,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"away_shoot": 20,
"home_director": "柱谷　幸一",
"away_team": "アビスパ福岡",
"weather": "曇",
"series_number": 30,
"temperature": 24.4,
"away_score": 5,
"away_start_member": "神山　竜一,パク　ゴン,堤　俊輔,イ　グァンソン,古賀　正紘,中原　秀人,三島　勇太,武田　英二郎,城後　寿,酒井　宣福,金森　健志",
"home_score": 3,
"home_shoot": 13,
"game_id": "16303",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/09/06 18:03",
"referee": "飯田　淳平"
},
{
"teams": [
"カターレ富山",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "廣永　遼太郎,御厨　貴文,秋本　倫孝,内田　錬平,前　貴之,大西　容平,井澤　惇,内田　健太,木本　敬介,宮吉　拓実,苔口　卓也",
"away_shoot": 7,
"home_director": "安間　貴義",
"away_team": "ＦＣ岐阜",
"weather": "曇のち雨",
"series_number": 30,
"temperature": 25.1,
"away_score": 0,
"away_start_member": "川口　能活,ヘニキ,阿部　正紀,田中　秀人,森　勇介,水野　泰輔,髙地　系治,宮沢　正史,太田　圭輔,難波　宏明,ナザリト",
"home_score": 0,
"home_shoot": 9,
"game_id": "16300",
"home_team": "カターレ富山",
"game_start_at": "2014/09/06 18:04",
"referee": "河合　英治"
},
{
"teams": [
"ファジアーノ岡山",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,片山　瑛一,押谷　祐樹,石原　崇兆,清水　慎太郎",
"away_shoot": 9,
"home_director": "影山　雅永",
"away_team": "ジュビロ磐田",
"weather": "雨",
"series_number": 30,
"temperature": 20.8,
"away_score": 1,
"away_start_member": "八田　直樹,坪内　秀介,藤田　義明,森下　俊,櫻内　渚,フェルジナンド,小林　祐希,宮崎　智彦,松井　大輔,前田　遼一,ペク　ソンドン",
"home_score": 1,
"home_shoot": 12,
"game_id": "16302",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/09/06 18:34",
"referee": "廣瀬　格"
},
{
"teams": [
"コンサドーレ札幌",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "金山　隼樹,上原　慎也,櫛引　一紀,奈良　竜樹,上原　拓郎,河合　竜二,宮澤　裕樹,中原　彰吾,前田　俊介,砂川　誠,都倉　賢",
"away_shoot": 13,
"home_director": "名塚　善寛",
"away_team": "Ｖ・ファーレン長崎",
"weather": "屋内",
"series_number": 30,
"temperature": 24,
"away_score": 1,
"away_start_member": "大久保　択生,岡本　拓也,山口　貴弘,髙杉　亮太,古部　健太,前田　悠佑,三原　雅俊,野田　紘史,佐藤　洸一,東　浩史,スティッペ",
"home_score": 2,
"home_shoot": 6,
"game_id": "16294",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/09/06 19:03",
"referee": "塚田　健太"
},
{
"teams": [
"大分トリニータ",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "武田　洋平,若狭　大志,高木　和道,安川　有,土岐田　洸平,伊藤　大介,為田　大貴,松本　昌也,風間　宏矢,林　容平,ラドンチッチ",
"away_shoot": 14,
"home_director": "田坂　和昭",
"away_team": "ロアッソ熊本",
"weather": "屋内",
"series_number": 30,
"temperature": 25.7,
"away_score": 1,
"away_start_member": "畑　実,大迫　希,園田　拓也,橋本　拳人,片山　奨典,中山　雄登,養父　雄仁,髙柳　一誠,仲間　隼斗,アンデルソン,齊藤　和樹",
"home_score": 0,
"home_shoot": 8,
"game_id": "16304",
"home_team": "大分トリニータ",
"game_start_at": "2014/09/06 19:03",
"referee": "岡　宏道"
},
{
"teams": [
"湘南ベルマーレ",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,亀川　諒史,菊地　俊介,永木　亮太,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"away_shoot": 9,
"home_director": "曺　貴裁",
"away_team": "松本山雅ＦＣ",
"weather": "曇",
"series_number": 30,
"temperature": 27,
"away_score": 1,
"away_start_member": "村山　智彦,多々良　敦斗,犬飼　智也,飯田　真輝,田中　隼磨,岩沼　俊介,岩間　雄大,岩上　祐三,喜山　康平,船山　貴之,サビア",
"home_score": 1,
"home_shoot": 14,
"game_id": "16299",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/09/06 19:04",
"referee": "家本　政明"
},
{
"teams": [
"京都サンガF.C.",
"ジェフユナイテッド千葉"
],
"away_director": "関塚　隆",
"home_start_member": "杉本　大地,石櫃　洋祐,酒井　隆介,バヤリッツァ,駒井　善成,田中　英雄,田森　大己,山瀬　功治,工藤　浩平,ドウグラス,大黒　将志",
"away_shoot": 16,
"home_director": "川勝　良一",
"away_team": "ジェフユナイテッド千葉",
"weather": "雨",
"series_number": 30,
"temperature": 21.8,
"away_score": 3,
"away_start_member": "岡本　昌弘,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,谷澤　達也,オナイウ　阿道,森本　貴幸",
"home_score": 3,
"home_shoot": 15,
"game_id": "16301",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/09/06 19:04",
"referee": "松尾　一"
},
{
"teams": [
"清水エスパルス",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "櫛引　政敏,吉田　豊,ブエノ,平岡　康裕,水谷　拓磨,六平　光成,本田　拓也,高木　俊幸,石毛　秀樹,大前　元紀,ノヴァコヴィッチ",
"away_shoot": 5,
"home_director": "大榎　克己",
"away_team": "浦和レッズ",
"weather": "晴",
"series_number": 23,
"temperature": 24.9,
"away_score": 4,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,鈴木　啓太,宇賀神　友弥,柏木　陽介,李　忠成,興梠　慎三",
"home_score": 1,
"home_shoot": 8,
"game_id": "15873",
"home_team": "清水エスパルス",
"game_start_at": "2014/09/13 15:06",
"referee": "木村　博之"
},
{
"teams": [
"大宮アルディージャ",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "北野　貴之,今井　智基,横山　知伸,高橋　祥平,中村　北斗,金澤　慎,カルリーニョス,家長　昭博,泉澤　仁,ムルジャ,ズラタン",
"away_shoot": 18,
"home_director": "渋谷　洋樹",
"away_team": "鹿島アントラーズ",
"weather": "晴のち曇",
"series_number": 23,
"temperature": 20.8,
"away_score": 1,
"away_start_member": "曽ヶ端　準,西　大伍,山村　和也,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,カイオ,ジョルジ　ワグネル,土居　聖真,ダヴィ",
"home_score": 2,
"home_shoot": 7,
"game_id": "15867",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/09/13 18:05",
"referee": "村上　伸次"
},
{
"teams": [
"ＦＣ東京",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,エドゥー,武藤　嘉紀,河野　広貴",
"away_shoot": 10,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "ヴィッセル神戸",
"weather": "晴",
"series_number": 23,
"temperature": 24,
"away_score": 1,
"away_start_member": "山本　海人,高橋　峻希,河本　裕之,増川　隆洋,橋本　英郎,シンプリシオ,枝村　匠馬,チョン　ウヨン,田代　有三,マルキーニョス,森岡　亮太",
"home_score": 1,
"home_shoot": 7,
"game_id": "15868",
"home_team": "ＦＣ東京",
"game_start_at": "2014/09/13 18:34",
"referee": "佐藤　隆治"
},
{
"teams": [
"ヴァンフォーレ甲府",
"サガン鳥栖"
],
"away_director": "吉田　恵",
"home_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,松橋　優,新井　涼平,保坂　一成,阿部　翔平,河本　明人,盛田　剛平,クリスティアーノ",
"away_shoot": 6,
"home_director": "城福　浩",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 23,
"temperature": 23.1,
"away_score": 0,
"away_start_member": "林　彰洋,丹羽　竜平,小林　久晃,坂井　達弥,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,早坂　良太,豊田　陽平",
"home_score": 1,
"home_shoot": 3,
"game_id": "15871",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/09/13 18:34",
"referee": "吉田　寿光"
},
{
"teams": [
"横浜Ｆ・マリノス",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "榎本　哲也,小林　祐三,中澤　佑二,ファビオ,下平　匠,富澤　清太郎,小椋　祥平,藤本　淳吾,中村　俊輔,齋藤　学,矢島　卓郎",
"away_shoot": 6,
"home_director": "樋口　靖洋",
"away_team": "名古屋グランパス",
"weather": "晴",
"series_number": 23,
"temperature": 24,
"away_score": 2,
"away_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,矢田　旭,ダニルソン,田口　泰士,レアンドロ　ドミンゲス,川又　堅碁,永井　謙佑",
"home_score": 0,
"home_shoot": 9,
"game_id": "15870",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/09/13 19:03",
"referee": "山本　雄大"
},
{
"teams": [
"アルビレックス新潟",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,大野　和成,レオ　シルバ,小林　裕紀,山本　康裕,田中　亜土夢,成岡　翔,指宿　洋史",
"away_shoot": 5,
"home_director": "柳下　正明",
"away_team": "ベガルタ仙台",
"weather": "曇のち雨",
"series_number": 23,
"temperature": 21.9,
"away_score": 0,
"away_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,武井　択也,梁　勇基,赤嶺　真吾,武藤　雄樹",
"home_score": 1,
"home_shoot": 9,
"game_id": "15872",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/09/13 19:04",
"referee": "今村　義朗"
},
{
"teams": [
"セレッソ大阪",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "キム　ジンヒョン,染谷　悠太,丸橋　祐介,酒本　憲幸,山下　達也,扇原　貴宏,楠神　順平,南野　拓実,キム　ソンジュン,永井　龍,杉本　健勇",
"away_shoot": 11,
"home_director": "大熊　裕司",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 23,
"temperature": 23.4,
"away_score": 0,
"away_start_member": "菅野　孝憲,鈴木　大輔,近藤　直也,エドゥアルド,橋本　和,太田　徹郎,茨田　陽生,大谷　秀和,高山　薫,レアンドロ,工藤　壮人",
"home_score": 2,
"home_shoot": 11,
"game_id": "15874",
"home_team": "セレッソ大阪",
"game_start_at": "2014/09/13 19:04",
"referee": "池内　明彦"
},
{
"teams": [
"サンフレッチェ広島",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,清水　航平,青山　敏弘,森﨑　和幸,山岸　智,茶島　雄介,髙萩　洋次郎,皆川　佑介",
"away_shoot": 11,
"home_director": "森保　一",
"away_team": "ガンバ大阪",
"weather": "晴",
"series_number": 23,
"temperature": 21.4,
"away_score": 1,
"away_start_member": "東口　順昭,オ　ジェソク,丹羽　大輝,岩下　敬輔,藤春　廣輝,明神　智和,今野　泰幸,阿部　浩之,遠藤　保仁,宇佐美　貴史,佐藤　晃大",
"home_score": 0,
"home_shoot": 8,
"game_id": "15875",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/09/13 19:04",
"referee": "松尾　一"
},
{
"teams": [
"川崎フロンターレ",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "西部　洋平,田中　裕介,ジェシ,井川　祐輔,小宮山　尊信,稲本　潤一,谷口　彰悟,中村　憲剛,小林　悠,安　柄俊,レナト",
"away_shoot": 6,
"home_director": "風間　八宏",
"away_team": "徳島ヴォルティス",
"weather": "晴",
"series_number": 23,
"temperature": 23.4,
"away_score": 0,
"away_start_member": "長谷川　徹,藤原　広太朗,青山　隼,村松　大輔,アレックス,エステバン,濱田　武,大﨑　淳矢,津田　知宏,アドリアーノ,高崎　寛之",
"home_score": 4,
"home_shoot": 20,
"game_id": "15869",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/09/13 19:05",
"referee": "上田　益也"
},
{
"teams": [
"栃木ＳＣ",
"東京ヴェルディ"
],
"away_director": "三浦　泰年",
"home_start_member": "鈴木　智幸,イ　ミンス,赤井　秀行,チャ　ヨンファン,荒堀　謙次,湯澤　洋介,西澤　代志也,小野寺　達也,近藤　祐介,杉本　真,西川　優大",
"away_shoot": 18,
"home_director": "阪倉　裕二",
"away_team": "東京ヴェルディ",
"weather": "曇",
"series_number": 31,
"temperature": 20.1,
"away_score": 2,
"away_start_member": "佐藤　優也,田村　直也,金　鐘必,キローラン　木鈴,安在　和樹,安西　幸輝,澤井　直人,鈴木　惇,南　秀仁,前田　直輝,杉本　竜士",
"home_score": 3,
"home_shoot": 9,
"game_id": "16305",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/09/14 18:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"ザスパクサツ群馬",
"京都サンガF.C."
],
"away_director": "川勝　良一",
"home_start_member": "富居　大樹,久富　良輔,有薗　真吾,クォン　ハンジン,瀬川　和樹,小林　竜樹,金沢　浄,黄　誠秀,宮崎　泰右,ダニエル　ロビーニョ,平繁　龍一",
"away_shoot": 11,
"home_director": "秋葉　忠宏",
"away_team": "京都サンガF.C.",
"weather": "晴",
"series_number": 31,
"temperature": 23.8,
"away_score": 1,
"away_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,駒井　善成,田中　英雄,中山　博貴,山瀬　功治,横谷　繁,ドウグラス,大黒　将志",
"home_score": 0,
"home_shoot": 9,
"game_id": "16306",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/09/14 18:04",
"referee": "廣瀬　格"
},
{
"teams": [
"カマタマーレ讃岐",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "瀬口　拓弥,武田　有祐,エブソン,藤井　航大,沼田　圭悟,大沢　朋也,岡村　和哉,高木　和正,西野　泰正,木島　良輔,小澤　雄希",
"away_shoot": 11,
"home_director": "北野　誠",
"away_team": "湘南ベルマーレ",
"weather": "晴",
"series_number": 31,
"temperature": 25.3,
"away_score": 2,
"away_start_member": "秋元　陽太,菊地　俊介,丸山　祐市,三竿　雄斗,藤田　征也,岩尾　憲,永木　亮太,亀川　諒史,大竹　洋平,ウェリントン,武富　孝介",
"home_score": 0,
"home_shoot": 2,
"game_id": "16311",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/09/14 18:04",
"referee": "前田　拓哉"
},
{
"teams": [
"松本山雅ＦＣ",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "村山　智彦,多々良　敦斗,犬飼　智也,飯田　真輝,田中　隼磨,喜山　康平,岩間　雄大,ユン　ソンヨル,岩沼　俊介,船山　貴之,サビア",
"away_shoot": 12,
"home_director": "反町　康治",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 31,
"temperature": 19.7,
"away_score": 2,
"away_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,島田　譲,片山　瑛一,押谷　祐樹,石原　崇兆,清水　慎太郎",
"home_score": 1,
"home_shoot": 18,
"game_id": "16308",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/09/14 18:05",
"referee": "岡部　拓人"
},
{
"teams": [
"カターレ富山",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "廣永　遼太郎,パク　テホン,秋本　倫孝,高　准翼,前　貴之,キム　ヨングン,井澤　惇,内田　健太,木本　敬介,宮吉　拓実,苔口　卓也",
"away_shoot": 12,
"home_director": "安間　貴義",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 31,
"temperature": 22.3,
"away_score": 1,
"away_start_member": "武田　洋平,若狭　大志,高木　和道,安川　有,西　弘則,キム　ジョンヒョン,伊藤　大介,為田　大貴,木村　祐志,伊佐　耕平,林　容平",
"home_score": 1,
"home_shoot": 13,
"game_id": "16309",
"home_team": "カターレ富山",
"game_start_at": "2014/09/14 18:05",
"referee": "日高　晴樹"
},
{
"teams": [
"アビスパ福岡",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "神山　竜一,阿部　巧,武田　英二郎,イ　グァンソン,堤　俊輔,パク　ゴン,中原　秀人,三島　勇太,平井　将生,城後　寿,酒井　宣福",
"away_shoot": 6,
"home_director": "マリヤン　プシュニク",
"away_team": "水戸ホーリーホック",
"weather": "晴のち曇",
"series_number": 31,
"temperature": 23.5,
"away_score": 1,
"away_start_member": "本間　幸司,新里　亮,冨田　大介,細川　淳矢,田中　雄大,西岡　謙太,船谷　圭祐,広瀬　陸斗,吉田　眞紀人,三島　康平,山村　佑樹",
"home_score": 0,
"home_shoot": 12,
"game_id": "16313",
"home_team": "アビスパ福岡",
"game_start_at": "2014/09/14 18:06",
"referee": "吉田　哲朗"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "植草　裕樹,髙杉　亮太,山口　貴弘,野田　紘史,古部　健太,奥埜　博亮,三原　雅俊,石神　直哉,佐藤　洸一,東　浩史,スティッペ",
"away_shoot": 5,
"home_director": "高木　琢也",
"away_team": "ジュビロ磐田",
"weather": "曇",
"series_number": 31,
"temperature": 25.7,
"away_score": 1,
"away_start_member": "八田　直樹,坪内　秀介,藤田　義明,森下　俊,櫻内　渚,フェルジナンド,小林　祐希,宮崎　智彦,チンガ,松井　大輔,前田　遼一",
"home_score": 1,
"home_shoot": 12,
"game_id": "16314",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/09/14 18:06",
"referee": "井上　知大"
},
{
"teams": [
"ジェフユナイテッド千葉",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "岡本　昌弘,山口　慶,キム　ヒョヌン,大岩　一貴,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,幸野　志有人,谷澤　達也,森本　貴幸",
"away_shoot": 8,
"home_director": "関塚　隆",
"away_team": "ギラヴァンツ北九州",
"weather": "曇",
"series_number": 31,
"temperature": 22.4,
"away_score": 3,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"home_score": 1,
"home_shoot": 24,
"game_id": "16307",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/09/14 19:03",
"referee": "榎本　一慶"
},
{
"teams": [
"ロアッソ熊本",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "畑　実,大迫　希,橋本　拳人,キム　ビョンヨン,片山　奨典,仲間　隼斗,養父　雄仁,髙柳　一誠,澤田　崇,アンデルソン,齊藤　和樹",
"away_shoot": 8,
"home_director": "小野　剛",
"away_team": "横浜ＦＣ",
"weather": "曇",
"series_number": 31,
"temperature": 24.7,
"away_score": 2,
"away_start_member": "南　雄太,小池　純輝,野上　結貴,ドウグラス,中島　崇典,寺田　紳一,松下　裕樹,松下　年宏,内田　智也,野村　直輝,パク　ソンホ",
"home_score": 2,
"home_shoot": 13,
"game_id": "16315",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/09/14 19:04",
"referee": "窪田　陽輔"
},
{
"teams": [
"ＦＣ岐阜",
"コンサドーレ札幌"
],
"away_director": "バルバリッチ",
"home_start_member": "川口　能活,益山　司,ヘニキ,阿部　正紀,森　勇介,宮沢　正史,髙地　系治,太田　圭輔,クレイトン　ドミンゲス,水野　泰輔,難波　宏明",
"away_shoot": 4,
"home_director": "ラモス　瑠偉",
"away_team": "コンサドーレ札幌",
"weather": "晴",
"series_number": 31,
"temperature": 23.8,
"away_score": 1,
"away_start_member": "金山　隼樹,上原　慎也,パウロン,櫛引　一紀,上原　拓郎,宮澤　裕樹,河合　竜二,中原　彰吾,前田　俊介,砂川　誠,都倉　賢",
"home_score": 1,
"home_shoot": 12,
"game_id": "16310",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/09/14 19:05",
"referee": "森川　浩次"
},
{
"teams": [
"愛媛ＦＣ",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "児玉　剛,ハン　ヒフン,村上　佑介,林堂　眞,浦田　延尚,三原　向平,渡邊　一仁,村上　巧,堀米　勇輝,西田　剛,河原　和寿",
"away_shoot": 10,
"home_director": "石丸　清隆",
"away_team": "モンテディオ山形",
"weather": "晴",
"series_number": 31,
"temperature": 21.4,
"away_score": 0,
"away_start_member": "山岸　範宏,山田　拓巳,舩津　徹也,石井　秀典,當間　建文,松岡　亮輔,宮阪　政樹,石川　竜也,中島　裕希,ディエゴ,ロメロ　フランク",
"home_score": 4,
"home_shoot": 11,
"game_id": "16312",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/09/14 19:05",
"referee": "三上　正一郎"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "植草　裕樹,髙杉　亮太,山口　貴弘,野田　紘史,古部　健太,前田　悠佑,三原　雅俊,石神　直哉,奥埜　博亮,東　浩史,佐藤　洸一",
"away_shoot": 10,
"home_director": "高木　琢也",
"away_team": "横浜ＦＣ",
"weather": "雨",
"series_number": 32,
"temperature": 19,
"away_score": 0,
"away_start_member": "南　雄太,野上　結貴,松下　裕樹,ドウグラス,中島　崇典,寺田　紳一,佐藤　謙介,松下　年宏,内田　智也,野崎　陽介,パク　ソンホ",
"home_score": 1,
"home_shoot": 9,
"game_id": "16316",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/09/19 19:04",
"referee": "岡　宏道"
},
{
"teams": [
"東京ヴェルディ",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "佐藤　優也,安西　幸輝,金　鐘必,井林　章,安在　和樹,中後　雅喜,鈴木　惇,澤井　直人,常盤　聡,菅嶋　弘希,杉本　竜士",
"away_shoot": 9,
"home_director": "冨樫　剛一",
"away_team": "カターレ富山",
"weather": "曇",
"series_number": 32,
"temperature": 21,
"away_score": 1,
"away_start_member": "廣永　遼太郎,池端　陽介,秋本　倫孝,パク　テホン,前　貴之,キム　ヨングン,井澤　惇,内田　健太,木本　敬介,宮吉　拓実,苔口　卓也",
"home_score": 0,
"home_shoot": 16,
"game_id": "16320",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/09/20 13:03",
"referee": "村上　伸次"
},
{
"teams": [
"松本山雅ＦＣ",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,多々良　敦斗,岩間　雄大,ユン　ソンヨル,岩上　祐三,飯尾　竜太朗,船山　貴之,サビア",
"away_shoot": 3,
"home_director": "反町　康治",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 32,
"temperature": 21.1,
"away_score": 0,
"away_start_member": "瀬口　拓弥,西野　泰正,エブソン,藤井　航大,武田　有祐,古田　寛幸,堀河　俊大,沼田　圭悟,アンドレア,木島　良輔,小澤　雄希",
"home_score": 0,
"home_shoot": 16,
"game_id": "16322",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/09/20 13:03",
"referee": "長谷　拓"
},
{
"teams": [
"モンテディオ山形",
"京都サンガF.C."
],
"away_director": "川勝　良一",
"home_start_member": "山岸　範宏,小林　亮,舩津　徹也,石井　秀典,石川　竜也,松岡　亮輔,宮阪　政樹,キム　ボムヨン,山﨑　雅人,ディエゴ,川西　翔太",
"away_shoot": 9,
"home_director": "石﨑　信弘",
"away_team": "京都サンガF.C.",
"weather": "晴",
"series_number": 32,
"temperature": 24.6,
"away_score": 0,
"away_start_member": "オ　スンフン,駒井　善成,酒井　隆介,バヤリッツァ,石櫃　洋祐,田中　英雄,中山　博貴,山瀬　功治,石田　雅俊,横谷　繁,大黒　将志",
"home_score": 1,
"home_shoot": 14,
"game_id": "16317",
"home_team": "モンテディオ山形",
"game_start_at": "2014/09/20 13:04",
"referee": "福島　孝一郎"
},
{
"teams": [
"名古屋グランパス",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,矢田　旭,磯村　亮太,田口　泰士,レアンドロ　ドミンゲス,川又　堅碁,永井　謙佑",
"away_shoot": 6,
"home_director": "西野　朗",
"away_team": "ヴァンフォーレ甲府",
"weather": "曇",
"series_number": 24,
"temperature": 22.9,
"away_score": 0,
"away_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,松橋　優,保坂　一成,新井　涼平,阿部　翔平,河本　明人,盛田　剛平,クリスティアーノ",
"home_score": 2,
"home_shoot": 9,
"game_id": "15879",
"home_team": "名古屋グランパス",
"game_start_at": "2014/09/20 15:04",
"referee": "中村　太"
},
{
"teams": [
"ロアッソ熊本",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "畑　実,大迫　希,園田　拓也,橋本　拳人,片山　奨典,中山　雄登,養父　雄仁,髙柳　一誠,仲間　隼斗,澤田　崇,齊藤　和樹",
"away_shoot": 11,
"home_director": "小野　剛",
"away_team": "栃木ＳＣ",
"weather": "曇",
"series_number": 32,
"temperature": 20.3,
"away_score": 1,
"away_start_member": "鈴木　智幸,イ　ミンス,赤井　秀行,チャ　ヨンファン,荒堀　謙次,湯澤　洋介,西澤　代志也,小野寺　達也,近藤　祐介,杉本　真,西川　優大",
"home_score": 2,
"home_shoot": 11,
"game_id": "16325",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/09/20 16:03",
"referee": "松尾　一"
},
{
"teams": [
"ガンバ大阪",
"セレッソ大阪"
],
"away_director": "大熊　裕司",
"home_start_member": "東口　順昭,米倉　恒貴,金　正也,丹羽　大輝,オ　ジェソク,今野　泰幸,遠藤　保仁,阿部　浩之,倉田　秋,宇佐美　貴史,パトリック",
"away_shoot": 10,
"home_director": "長谷川　健太",
"away_team": "セレッソ大阪",
"weather": "曇",
"series_number": 24,
"temperature": 22.8,
"away_score": 0,
"away_start_member": "キム　ジンヒョン,染谷　悠太,丸橋　祐介,酒本　憲幸,山下　達也,長谷川　アーリアジャスール,楠神　順平,南野　拓実,キム　ソンジュン,永井　龍,杉本　健勇",
"home_score": 2,
"home_shoot": 11,
"game_id": "15880",
"home_team": "ガンバ大阪",
"game_start_at": "2014/09/20 16:04",
"referee": "家本　政明"
},
{
"teams": [
"ジュビロ磐田",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "八田　直樹,櫻内　渚,藤田　義明,森下　俊,坪内　秀介,小林　祐希,フェルジナンド,チンガ,松井　大輔,山崎　亮平,前田　遼一",
"away_shoot": 9,
"home_director": "シャムスカ",
"away_team": "ギラヴァンツ北九州",
"weather": "曇",
"series_number": 32,
"temperature": 21.9,
"away_score": 1,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"home_score": 3,
"home_shoot": 15,
"game_id": "16323",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/09/20 16:04",
"referee": "高山　啓義"
},
{
"teams": [
"ヴィッセル神戸",
"清水エスパルス"
],
"away_director": "大榎　克己",
"home_start_member": "山本　海人,高橋　峻希,河本　裕之,増川　隆洋,橋本　英郎,チョン　ウヨン,シンプリシオ,森岡　亮太,ペドロ　ジュニオール,田代　有三,マルキーニョス",
"away_shoot": 11,
"home_director": "安達　亮",
"away_team": "清水エスパルス",
"weather": "曇",
"series_number": 24,
"temperature": 18.6,
"away_score": 1,
"away_start_member": "櫛引　政敏,吉田　豊,ブエノ,平岡　康裕,三浦　弦太,六平　光成,本田　拓也,高木　俊幸,イ　キジェ,大前　元紀,ノヴァコヴィッチ",
"home_score": 3,
"home_shoot": 7,
"game_id": "15881",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/09/20 19:03",
"referee": "窪田　陽輔"
},
{
"teams": [
"ジェフユナイテッド千葉",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "岡本　昌弘,山口　慶,キム　ヒョヌン,大岩　一貴,中村　太亮,佐藤　勇人,ナム　スンウ,井出　遥也,町田　也真人,谷澤　達也,森本　貴幸",
"away_shoot": 17,
"home_director": "関塚　隆",
"away_team": "ＦＣ岐阜",
"weather": "曇",
"series_number": 32,
"temperature": 19.9,
"away_score": 0,
"away_start_member": "川口　能活,益山　司,ヘニキ,阿部　正紀,森　勇介,宮沢　正史,髙地　系治,太田　圭輔,水野　泰輔,クレイトン　ドミンゲス,難波　宏明",
"home_score": 1,
"home_shoot": 11,
"game_id": "16319",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/09/20 19:03",
"referee": "吉田　寿光"
},
{
"teams": [
"ファジアーノ岡山",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,島田　譲,三村　真,押谷　祐樹,石原　崇兆,清水　慎太郎",
"away_shoot": 16,
"home_director": "影山　雅永",
"away_team": "愛媛ＦＣ",
"weather": "曇",
"series_number": 32,
"temperature": 19,
"away_score": 1,
"away_start_member": "児玉　剛,ハン　ヒフン,村上　佑介,林堂　眞,浦田　延尚,キム　ミンジェ,渡邊　一仁,江口　直生,堀米　勇輝,西田　剛,河原　和寿",
"home_score": 1,
"home_shoot": 7,
"game_id": "16324",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/09/20 19:03",
"referee": "塚田　健太"
},
{
"teams": [
"大分トリニータ",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "武田　洋平,安川　有,高木　和道,若狭　大志,西　弘則,末吉　隼也,伊藤　大介,ダニエル,為田　大貴,林　容平,伊佐　耕平",
"away_shoot": 16,
"home_director": "田坂　和昭",
"away_team": "アビスパ福岡",
"weather": "屋内",
"series_number": 32,
"temperature": 19.4,
"away_score": 0,
"away_start_member": "神山　竜一,パク　ゴン,堤　俊輔,イ　グァンソン,古賀　正紘,中原　秀人,森村　昂太,酒井　宣福,武田　英二郎,城後　寿,平井　将生",
"home_score": 3,
"home_shoot": 10,
"game_id": "16326",
"home_team": "大分トリニータ",
"game_start_at": "2014/09/20 19:03",
"referee": "上田　益也"
},
{
"teams": [
"鹿島アントラーズ",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "曽ヶ端　準,西　大伍,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,ダヴィ",
"away_shoot": 1,
"home_director": "トニーニョ　セレーゾ",
"away_team": "横浜Ｆ・マリノス",
"weather": "雨のち曇",
"series_number": 24,
"temperature": 20.7,
"away_score": 0,
"away_start_member": "榎本　哲也,奈良輪　雄太,栗原　勇蔵,中澤　佑二,下平　匠,三門　雄大,富澤　清太郎,藤本　淳吾,中村　俊輔,齋藤　学,伊藤　翔",
"home_score": 1,
"home_shoot": 15,
"game_id": "15876",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/09/20 19:04",
"referee": "今村　義朗"
},
{
"teams": [
"川崎フロンターレ",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "西部　洋平,田中　裕介,實藤　友紀,井川　祐輔,山越　享太郎,パウリーニョ,谷口　彰悟,中村　憲剛,小林　悠,レナト,安　柄俊",
"away_shoot": 8,
"home_director": "風間　八宏",
"away_team": "ＦＣ東京",
"weather": "晴のち曇",
"series_number": 24,
"temperature": 20.8,
"away_score": 0,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,河野　広貴,エドゥー,武藤　嘉紀",
"home_score": 0,
"home_shoot": 11,
"game_id": "15878",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/09/20 19:04",
"referee": "木村　博之"
},
{
"teams": [
"サンフレッチェ広島",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,ミキッチ,青山　敏弘,森﨑　和幸,柏　好文,石原　直樹,髙萩　洋次郎,皆川　佑介",
"away_shoot": 12,
"home_director": "森保　一",
"away_team": "アルビレックス新潟",
"weather": "晴",
"series_number": 24,
"temperature": 16.6,
"away_score": 0,
"away_start_member": "守田　達弥,川口　尚紀,大井　健太郎,舞行龍ジェームズ,大野　和成,レオ　シルバ,小林　裕紀,山本　康裕,小泉　慶,指宿　洋史,岡本　英也",
"home_score": 2,
"home_shoot": 11,
"game_id": "15882",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/09/20 19:04",
"referee": "岡部　拓人"
},
{
"teams": [
"徳島ヴォルティス",
"大宮アルディージャ"
],
"away_director": "渋谷　洋樹",
"home_start_member": "長谷川　徹,藤原　広太朗,斉藤　大介,村松　大輔,アレックス,エステバン,濱田　武,大﨑　淳矢,津田　知宏,佐々木　一輝,高崎　寛之",
"away_shoot": 11,
"home_director": "小林　伸二",
"away_team": "大宮アルディージャ",
"weather": "曇",
"series_number": 24,
"temperature": 20.8,
"away_score": 2,
"away_start_member": "北野　貴之,今井　智基,横山　知伸,高橋　祥平,中村　北斗,金澤　慎,カルリーニョス,泉澤　仁,家長　昭博,ムルジャ,ズラタン",
"home_score": 0,
"home_shoot": 12,
"game_id": "15883",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/09/20 19:04",
"referee": "井上　知大"
},
{
"teams": [
"サガン鳥栖",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "林　彰洋,丹羽　竜平,小林　久晃,坂井　達弥,安田　理大,早坂　良太,岡本　知剛,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 13,
"home_director": "吉田　恵",
"away_team": "ベガルタ仙台",
"weather": "曇",
"series_number": 24,
"temperature": 20.9,
"away_score": 1,
"away_start_member": "桜井　繁,村上　和弘,鎌田　次郎,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,梁　勇基,野沢　拓也,赤嶺　真吾,ウイルソン",
"home_score": 2,
"home_shoot": 9,
"game_id": "15884",
"home_team": "サガン鳥栖",
"game_start_at": "2014/09/20 19:04",
"referee": "飯田　淳平"
},
{
"teams": [
"湘南ベルマーレ",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "秋元　陽太,宇佐美　宏和,丸山　祐市,三竿　雄斗,藤田　征也,岩尾　憲,永木　亮太,菊池　大介,大竹　洋平,ウェリントン,武富　孝介",
"away_shoot": 8,
"home_director": "曺　貴裁",
"away_team": "水戸ホーリーホック",
"weather": "曇",
"series_number": 32,
"temperature": 20.1,
"away_score": 2,
"away_start_member": "本間　幸司,新里　亮,冨田　大介,細川　淳矢,田中　雄大,西岡　謙太,船谷　圭祐,広瀬　陸斗,吉田　眞紀人,山村　佑樹,三島　康平",
"home_score": 4,
"home_shoot": 21,
"game_id": "16321",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/09/20 19:04",
"referee": "野田　祐樹"
},
{
"teams": [
"浦和レッズ",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,鈴木　啓太,宇賀神　友弥,柏木　陽介,李　忠成,興梠　慎三",
"away_shoot": 3,
"home_director": "ペトロヴィッチ",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 24,
"temperature": 20.4,
"away_score": 1,
"away_start_member": "菅野　孝憲,藤田　優人,鈴木　大輔,増嶋　竜也,橋本　和,茨田　陽生,エドゥアルド,大谷　秀和,高山　薫,ドゥドゥ,工藤　壮人",
"home_score": 3,
"home_shoot": 13,
"game_id": "15877",
"home_team": "浦和レッズ",
"game_start_at": "2014/09/20 19:05",
"referee": "佐藤　隆治"
},
{
"teams": [
"ザスパクサツ群馬",
"コンサドーレ札幌"
],
"away_director": "バルバリッチ",
"home_start_member": "富居　大樹,久富　良輔,有薗　真吾,クォン　ハンジン,小柳　達司,小林　竜樹,加藤　弘堅,黄　誠秀,宮崎　泰右,ダニエル　ロビーニョ,平繁　龍一",
"away_shoot": 9,
"home_director": "秋葉　忠宏",
"away_team": "コンサドーレ札幌",
"weather": "晴",
"series_number": 32,
"temperature": 16.3,
"away_score": 0,
"away_start_member": "金山　隼樹,上原　慎也,櫛引　一紀,奈良　竜樹,上原　拓郎,宮澤　裕樹,上里　一将,中原　彰吾,内村　圭宏,砂川　誠,都倉　賢",
"home_score": 3,
"home_shoot": 13,
"game_id": "16318",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/09/20 19:34",
"referee": "小屋　幸栄"
},
{
"teams": [
"アビスパ福岡",
"東京ヴェルディ"
],
"away_director": "冨樫　剛一",
"home_start_member": "神山　竜一,阿部　巧,三島　勇太,イ　グァンソン,堤　俊輔,パク　ゴン,中原　秀人,武田　英二郎,平井　将生,城後　寿,酒井　宣福",
"away_shoot": 13,
"home_director": "マリヤン　プシュニク",
"away_team": "東京ヴェルディ",
"weather": "曇",
"series_number": 33,
"temperature": 28,
"away_score": 1,
"away_start_member": "佐藤　優也,安西　幸輝,井林　章,金　鐘必,安在　和樹,中後　雅喜,ニウド,常盤　聡,澤井　直人,平本　一樹,杉本　竜士",
"home_score": 0,
"home_shoot": 10,
"game_id": "16336",
"home_team": "アビスパ福岡",
"game_start_at": "2014/09/23 12:34",
"referee": "池内　明彦"
},
{
"teams": [
"コンサドーレ札幌",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "李　昊乗,石井　謙伍,パウロン,奈良　竜樹,上原　慎也,中原　彰吾,河合　竜二,上里　一将,宮澤　裕樹,前田　俊介,都倉　賢",
"away_shoot": 14,
"home_director": "バルバリッチ",
"away_team": "ファジアーノ岡山",
"weather": "屋内",
"series_number": 33,
"temperature": 23.8,
"away_score": 1,
"away_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,島田　譲,片山　瑛一,押谷　祐樹,清水　慎太郎,久保　裕一",
"home_score": 3,
"home_shoot": 12,
"game_id": "16327",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/09/23 13:03",
"referee": "榎本　一慶"
},
{
"teams": [
"栃木ＳＣ",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "鈴木　智幸,山形　辰徳,赤井　秀行,チャ　ヨンファン,荒堀　謙次,廣瀬　浩二,西澤　代志也,本間　勲,近藤　祐介,西川　優大,大久保　哲哉",
"away_shoot": 12,
"home_director": "阪倉　裕二",
"away_team": "モンテディオ山形",
"weather": "晴",
"series_number": 33,
"temperature": 25,
"away_score": 1,
"away_start_member": "山岸　範宏,舩津　徹也,當間　建文,石井　秀典,石川　竜也,松岡　亮輔,宮阪　政樹,キム　ボムヨン,山﨑　雅人,ディエゴ,川西　翔太",
"home_score": 1,
"home_shoot": 7,
"game_id": "16329",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/09/23 13:03",
"referee": "木村　博之"
},
{
"teams": [
"横浜ＦＣ",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "南　雄太,小池　純輝,ドウグラス,渡辺　匠,中島　崇典,寺田　紳一,佐藤　謙介,松下　年宏,内田　智也,野村　直輝,パク　ソンホ",
"away_shoot": 12,
"home_director": "山口　素弘",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 33,
"temperature": 25.4,
"away_score": 1,
"away_start_member": "武田　洋平,安川　有,高木　和道,若狭　大志,西　弘則,ダニエル,伊藤　大介,末吉　隼也,為田　大貴,林　容平,後藤　優介",
"home_score": 1,
"home_shoot": 11,
"game_id": "16330",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/09/23 13:03",
"referee": "三上　正一郎"
},
{
"teams": [
"カターレ富山",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "廣永　遼太郎,池端　陽介,秋本　倫孝,パク　テホン,木本　敬介,キム　ヨングン,井澤　惇,前　貴之,白崎　凌兵,宮吉　拓実,苔口　卓也",
"away_shoot": 8,
"home_director": "安間　貴義",
"away_team": "ザスパクサツ群馬",
"weather": "晴",
"series_number": 33,
"temperature": 25.2,
"away_score": 1,
"away_start_member": "富居　大樹,久富　良輔,有薗　真吾,クォン　ハンジン,小柳　達司,瀬川　和樹,加藤　弘堅,永田　亮太,青木　孝太,ダニエル　ロビーニョ,平繁　龍一",
"home_score": 0,
"home_shoot": 15,
"game_id": "16331",
"home_team": "カターレ富山",
"game_start_at": "2014/09/23 13:04",
"referee": "森川　浩次"
},
{
"teams": [
"ＦＣ岐阜",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "川口　能活,森　勇介,ヘニキ,阿部　正紀,田中　秀人,水野　泰輔,髙地　系治,比嘉　諒人,遠藤　純輝,クレイトン　ドミンゲス,難波　宏明",
"away_shoot": 8,
"home_director": "ラモス　瑠偉",
"away_team": "ロアッソ熊本",
"weather": "晴",
"series_number": 33,
"temperature": 27,
"away_score": 3,
"away_start_member": "畑　実,園田　拓也,篠原　弘次郎,橋本　拳人,片山　奨典,中山　雄登,養父　雄仁,髙柳　一誠,仲間　隼斗,齊藤　和樹,アンデルソン",
"home_score": 2,
"home_shoot": 12,
"game_id": "16332",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/09/23 13:04",
"referee": "篠藤　巧"
},
{
"teams": [
"ベガルタ仙台",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "関　憲太郎,村上　和弘,鎌田　次郎,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,梁　勇基,野沢　拓也,赤嶺　真吾,ウイルソン",
"away_shoot": 16,
"home_director": "渡邉　晋",
"away_team": "鹿島アントラーズ",
"weather": "晴",
"series_number": 25,
"temperature": 24.9,
"away_score": 1,
"away_start_member": "曽ヶ端　準,西　大伍,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,ダヴィ",
"home_score": 0,
"home_shoot": 9,
"game_id": "15885",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/09/23 14:04",
"referee": "岡部　拓人"
},
{
"teams": [
"清水エスパルス",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "櫛引　政敏,ブエノ,平岡　康裕,三浦　弦太,吉田　豊,石毛　秀樹,本田　拓也,六平　光成,水谷　拓磨,大前　元紀,ノヴァコヴィッチ",
"away_shoot": 12,
"home_director": "大榎　克己",
"away_team": "ガンバ大阪",
"weather": "晴",
"series_number": 25,
"temperature": 25.4,
"away_score": 3,
"away_start_member": "東口　順昭,オ　ジェソク,丹羽　大輝,岩下　敬輔,藤春　廣輝,今野　泰幸,遠藤　保仁,阿部　浩之,二川　孝広,宇佐美　貴史,佐藤　晃大",
"home_score": 0,
"home_shoot": 9,
"game_id": "15892",
"home_team": "清水エスパルス",
"game_start_at": "2014/09/23 14:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"愛媛ＦＣ",
"ジェフユナイテッド千葉"
],
"away_director": "関塚　隆",
"home_start_member": "児玉　剛,村上　佑介,林堂　眞,浦田　延尚,キム　ミンジェ,渡邊　一仁,村上　巧,堀米　勇輝,藤　直也,西田　剛,表原　玄太",
"away_shoot": 12,
"home_director": "石丸　清隆",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 33,
"temperature": 25,
"away_score": 2,
"away_start_member": "岡本　昌弘,山口　慶,キム　ヒョヌン,大岩　一貴,中村　太亮,佐藤　勇人,ナム　スンウ,井出　遥也,町田　也真人,谷澤　達也,森本　貴幸",
"home_score": 2,
"home_shoot": 11,
"game_id": "16335",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/09/23 14:04",
"referee": "上田　益也"
},
{
"teams": [
"アルビレックス新潟",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "守田　達弥,大井　健太郎,舞行龍ジェームズ,大野　和成,レオ　シルバ,小林　裕紀,松原　健,小泉　慶,山本　康裕,田中　亜土夢,指宿　洋史",
"away_shoot": 8,
"home_director": "柳下　正明",
"away_team": "浦和レッズ",
"weather": "晴",
"series_number": 25,
"temperature": 24.2,
"away_score": 2,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,関根　貴大,阿部　勇樹,鈴木　啓太,梅崎　司,柏木　陽介,李　忠成,興梠　慎三",
"home_score": 0,
"home_shoot": 10,
"game_id": "15891",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/09/23 14:31",
"referee": "村上　伸次"
},
{
"teams": [
"ＦＣ東京",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,河野　広貴,エドゥー,武藤　嘉紀",
"away_shoot": 2,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "徳島ヴォルティス",
"weather": "晴",
"series_number": 25,
"temperature": 25,
"away_score": 0,
"away_start_member": "長谷川　徹,藤原　広太朗,斉藤　大介,村松　大輔,アレックス,エステバン,濱田　武,大﨑　淳矢,津田　知宏,佐々木　一輝,高崎　寛之",
"home_score": 4,
"home_shoot": 13,
"game_id": "15888",
"home_team": "ＦＣ東京",
"game_start_at": "2014/09/23 15:03",
"referee": "山本　雄大"
},
{
"teams": [
"横浜Ｆ・マリノス",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "榎本　哲也,奈良輪　雄太,栗原　勇蔵,中澤　佑二,下平　匠,三門　雄大,小椋　祥平,兵藤　慎剛,中村　俊輔,齋藤　学,伊藤　翔",
"away_shoot": 8,
"home_director": "樋口　靖洋",
"away_team": "サンフレッチェ広島",
"weather": "晴",
"series_number": 25,
"temperature": 26,
"away_score": 0,
"away_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,ミキッチ,青山　敏弘,森﨑　和幸,柏　好文,石原　直樹,髙萩　洋次郎,皆川　佑介",
"home_score": 1,
"home_shoot": 9,
"game_id": "15889",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/09/23 15:04",
"referee": "廣瀬　格"
},
{
"teams": [
"大宮アルディージャ",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "北野　貴之,今井　智基,横山　知伸,高橋　祥平,片岡　洋介,カルリーニョス,金澤　慎,家長　昭博,泉澤　仁,ズラタン,ムルジャ",
"away_shoot": 10,
"home_director": "渋谷　洋樹",
"away_team": "川崎フロンターレ",
"weather": "晴のち曇",
"series_number": 25,
"temperature": 25.9,
"away_score": 3,
"away_start_member": "西部　洋平,田中　裕介,ジェシ,井川　祐輔,登里　享平,パウリーニョ,谷口　彰悟,中村　憲剛,小林　悠,レナト,大久保　嘉人",
"home_score": 1,
"home_shoot": 14,
"game_id": "15886",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/09/23 15:34",
"referee": "家本　政明"
},
{
"teams": [
"水戸ホーリーホック",
"ジュビロ磐田"
],
"away_director": "シャムスカ",
"home_start_member": "笠原　昂史,新里　亮,金　聖基,細川　淳矢,田中　雄大,石神　幸征,広瀬　陸斗,船谷　圭祐,吉田　眞紀人,山村　佑樹,鈴木　隆行",
"away_shoot": 5,
"home_director": "柱谷　哲二",
"away_team": "ジュビロ磐田",
"weather": "晴",
"series_number": 33,
"temperature": 21.9,
"away_score": 1,
"away_start_member": "八田　直樹,櫻内　渚,藤田　義明,森下　俊,坪内　秀介,フェルジナンド,小林　祐希,チンガ,松井　大輔,山崎　亮平,前田　遼一",
"home_score": 4,
"home_shoot": 10,
"game_id": "16328",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/09/23 16:03",
"referee": "吉田　寿光"
},
{
"teams": [
"カマタマーレ讃岐",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "瀬口　拓弥,武田　有祐,藤井　航大,エブソン,沼田　圭悟,古田　寛幸,西野　泰正,山本　翔平,小澤　雄希,木島　良輔,大沢　朋也",
"away_shoot": 12,
"home_director": "北野　誠",
"away_team": "Ｖ・ファーレン長崎",
"weather": "晴",
"series_number": 33,
"temperature": 26.2,
"away_score": 1,
"away_start_member": "植草　裕樹,髙杉　亮太,山口　貴弘,野田　紘史,古部　健太,前田　悠佑,三原　雅俊,石神　直哉,奥埜　博亮,東　浩史,佐藤　洸一",
"home_score": 0,
"home_shoot": 4,
"game_id": "16334",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/09/23 16:03",
"referee": "河合　英治"
},
{
"teams": [
"ギラヴァンツ北九州",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,多田　高行,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"away_shoot": 19,
"home_director": "柱谷　幸一",
"away_team": "松本山雅ＦＣ",
"weather": "雨",
"series_number": 33,
"temperature": 23.6,
"away_score": 0,
"away_start_member": "村山　智彦,鐡戸　裕史,飯田　真輝,犬飼　智也,多々良　敦斗,岩間　雄大,喜山　康平,岩上　祐三,田中　隼磨,船山　貴之,山本　大貴",
"home_score": 0,
"home_shoot": 5,
"game_id": "16337",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/09/23 18:03",
"referee": "窪田　陽輔"
},
{
"teams": [
"ヴァンフォーレ甲府",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,ジウシーニョ,稲垣　祥,新井　涼平,阿部　翔平,石原　克哉,下田　北斗,クリスティアーノ",
"away_shoot": 9,
"home_director": "城福　浩",
"away_team": "ヴィッセル神戸",
"weather": "晴のち曇",
"series_number": 25,
"temperature": 22.6,
"away_score": 0,
"away_start_member": "山本　海人,高橋　峻希,河本　裕之,増川　隆洋,橋本　英郎,チョン　ウヨン,シンプリシオ,枝村　匠馬,ペドロ　ジュニオール,森岡　亮太,マルキーニョス",
"home_score": 2,
"home_shoot": 9,
"game_id": "15890",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/09/23 18:04",
"referee": "西村　雄一"
},
{
"teams": [
"京都サンガF.C.",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "オ　スンフン,バヤリッツァ,酒井　隆介,福村　貴幸,石櫃　洋祐,駒井　善成,工藤　浩平,中山　博貴,田森　大己,田中　英雄,大黒　将志",
"away_shoot": 11,
"home_director": "川勝　良一",
"away_team": "湘南ベルマーレ",
"weather": "晴",
"series_number": 33,
"temperature": 24.8,
"away_score": 2,
"away_start_member": "秋元　陽太,宇佐美　宏和,丸山　祐市,島村　毅,藤田　征也,岩尾　憲,永木　亮太,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"home_score": 2,
"home_shoot": 14,
"game_id": "16333",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/09/23 18:04",
"referee": "飯田　淳平"
},
{
"teams": [
"柏レイソル",
"サガン鳥栖"
],
"away_director": "吉田　恵",
"home_start_member": "桐畑　和繁,藤田　優人,鈴木　大輔,近藤　直也,渡部　博文,高山　薫,茨田　陽生,大谷　秀和,橋本　和,レアンドロ,工藤　壮人",
"away_shoot": 6,
"home_director": "ネルシーニョ",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 25,
"temperature": 20.3,
"away_score": 0,
"away_start_member": "林　彰洋,丹羽　竜平,小林　久晃,坂井　達弥,安田　理大,早坂　良太,岡本　知剛,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 2,
"home_shoot": 11,
"game_id": "15887",
"home_team": "柏レイソル",
"game_start_at": "2014/09/23 19:04",
"referee": "松尾　一"
},
{
"teams": [
"セレッソ大阪",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "キム　ジンヒョン,染谷　悠太,丸橋　祐介,酒本　憲幸,山下　達也,扇原　貴宏,長谷川　アーリアジャスール,南野　拓実,キム　ソンジュン,永井　龍,杉本　健勇",
"away_shoot": 9,
"home_director": "大熊　裕司",
"away_team": "名古屋グランパス",
"weather": "晴",
"series_number": 25,
"temperature": 24.3,
"away_score": 2,
"away_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,矢田　旭,磯村　亮太,田口　泰士,レアンドロ　ドミンゲス,川又　堅碁,永井　謙佑",
"home_score": 1,
"home_shoot": 8,
"game_id": "15893",
"home_team": "セレッソ大阪",
"game_start_at": "2014/09/23 19:04",
"referee": "今村　義朗"
},
{
"teams": [
"横浜Ｆ・マリノス",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "榎本　哲也,奈良輪　雄太,栗原　勇蔵,中澤　佑二,下平　匠,三門　雄大,小椋　祥平,兵藤　慎剛,佐藤　優平,矢島　卓郎,伊藤　翔",
"away_shoot": 5,
"home_director": "樋口　靖洋",
"away_team": "ヴァンフォーレ甲府",
"weather": "曇",
"series_number": 26,
"temperature": 23,
"away_score": 0,
"away_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,ジウシーニョ,稲垣　祥,新井　涼平,阿部　翔平,河本　明人,下田　北斗,クリスティアーノ",
"home_score": 0,
"home_shoot": 6,
"game_id": "15900",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/09/27 14:04",
"referee": "池内　明彦"
},
{
"teams": [
"サンフレッチェ広島",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,ミキッチ,青山　敏弘,森﨑　和幸,柏　好文,浅野　拓磨,森﨑　浩司,佐藤　寿人",
"away_shoot": 16,
"home_director": "森保　一",
"away_team": "ヴィッセル神戸",
"weather": "晴",
"series_number": 26,
"temperature": 25.4,
"away_score": 1,
"away_start_member": "山本　海人,北本　久仁衛,増川　隆洋,チョン　ウヨン,シンプリシオ,森岡　亮太,ペドロ　ジュニオール,相馬　崇人,高橋　峻希,小川　慶治朗,マルキーニョス",
"home_score": 1,
"home_shoot": 15,
"game_id": "15902",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/09/27 15:34",
"referee": "高山　啓義"
},
{
"teams": [
"ＦＣ東京",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,河野　広貴,エドゥー,武藤　嘉紀",
"away_shoot": 7,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "柏レイソル",
"weather": "曇",
"series_number": 26,
"temperature": 21.5,
"away_score": 0,
"away_start_member": "桐畑　和繁,藤田　優人,鈴木　大輔,近藤　直也,渡部　博文,高山　薫,栗澤　僚一,大谷　秀和,橋本　和,レアンドロ,工藤　壮人",
"home_score": 4,
"home_shoot": 9,
"game_id": "15895",
"home_team": "ＦＣ東京",
"game_start_at": "2014/09/27 16:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"大宮アルディージャ",
"清水エスパルス"
],
"away_director": "大榎　克己",
"home_start_member": "北野　貴之,今井　智基,横山　知伸,高橋　祥平,中村　北斗,金澤　慎,カルリーニョス,家長　昭博,橋本　晃司,泉澤　仁,ズラタン",
"away_shoot": 12,
"home_director": "渋谷　洋樹",
"away_team": "清水エスパルス",
"weather": "晴",
"series_number": 26,
"temperature": 19.9,
"away_score": 1,
"away_start_member": "櫛引　政敏,ブエノ,平岡　康裕,三浦　弦太,河井　陽介,石毛　秀樹,本田　拓也,六平　光成,水谷　拓磨,大前　元紀,ノヴァコヴィッチ",
"home_score": 2,
"home_shoot": 13,
"game_id": "15894",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/09/27 18:04",
"referee": "松尾　一"
},
{
"teams": [
"ガンバ大阪",
"サガン鳥栖"
],
"away_director": "吉田　恵",
"home_start_member": "東口　順昭,米倉　恒貴,丹羽　大輝,岩下　敬輔,オ　ジェソク,今野　泰幸,遠藤　保仁,阿部　浩之,大森　晃太郎,宇佐美　貴史,パトリック",
"away_shoot": 7,
"home_director": "長谷川　健太",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 26,
"temperature": 24.5,
"away_score": 1,
"away_start_member": "林　彰洋,丹羽　竜平,小林　久晃,坂井　達弥,安田　理大,水沼　宏太,岡本　知剛,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 4,
"home_shoot": 14,
"game_id": "15897",
"home_team": "ガンバ大阪",
"game_start_at": "2014/09/27 18:05",
"referee": "西村　雄一"
},
{
"teams": [
"徳島ヴォルティス",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "川浪　吾郎,藤原　広太朗,斉藤　大介,村松　大輔,アレックス,エステバン,濱田　武,大﨑　淳矢,津田　知宏,佐々木　一輝,高崎　寛之",
"away_shoot": 18,
"home_director": "小林　伸二",
"away_team": "鹿島アントラーズ",
"weather": "晴",
"series_number": 26,
"temperature": 24.1,
"away_score": 5,
"away_start_member": "曽ヶ端　準,西　大伍,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,赤﨑　秀平",
"home_score": 0,
"home_shoot": 7,
"game_id": "15898",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/09/27 19:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"セレッソ大阪",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "キム　ジンヒョン,染谷　悠太,丸橋　祐介,酒本　憲幸,山下　達也,扇原　貴宏,長谷川　アーリアジャスール,南野　拓実,キム　ソンジュン,杉本　健勇,カカウ",
"away_shoot": 15,
"home_director": "大熊　裕司",
"away_team": "浦和レッズ",
"weather": "晴",
"series_number": 26,
"temperature": 24.9,
"away_score": 0,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,鈴木　啓太,宇賀神　友弥,柏木　陽介,李　忠成,興梠　慎三",
"home_score": 1,
"home_shoot": 7,
"game_id": "15901",
"home_team": "セレッソ大阪",
"game_start_at": "2014/09/27 19:04",
"referee": "岡部　拓人"
},
{
"teams": [
"川崎フロンターレ",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "西部　洋平,田中　裕介,ジェシ,井川　祐輔,登里　享平,パウリーニョ,谷口　彰悟,中村　憲剛,小林　悠,レナト,大久保　嘉人",
"away_shoot": 11,
"home_director": "風間　八宏",
"away_team": "ベガルタ仙台",
"weather": "曇",
"series_number": 26,
"temperature": 20.6,
"away_score": 1,
"away_start_member": "関　憲太郎,菅井　直樹,角田　誠,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,梁　勇基,野沢　拓也,赤嶺　真吾,ウイルソン",
"home_score": 1,
"home_shoot": 14,
"game_id": "15899",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/09/27 19:05",
"referee": "榎本　一慶"
},
{
"teams": [
"名古屋グランパス",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,矢田　旭,中村　直志,田口　泰士,レアンドロ　ドミンゲス,川又　堅碁,永井　謙佑",
"away_shoot": 14,
"home_director": "西野　朗",
"away_team": "アルビレックス新潟",
"weather": "晴",
"series_number": 26,
"temperature": 23.1,
"away_score": 1,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,大野　和成,レオ　シルバ,小林　裕紀,山本　康裕,田中　亜土夢,ラファエル　シルバ,指宿　洋史",
"home_score": 0,
"home_shoot": 15,
"game_id": "15896",
"home_team": "名古屋グランパス",
"game_start_at": "2014/09/27 19:34",
"referee": "吉田　寿光"
},
{
"teams": [
"松本山雅ＦＣ",
"コンサドーレ札幌"
],
"away_director": "バルバリッチ",
"home_start_member": "村山　智彦,田中　隼磨,犬飼　智也,飯田　真輝,多々良　敦斗,喜山　康平,岩間　雄大,岩上　祐三,玉林　睦実,船山　貴之,山本　大貴",
"away_shoot": 8,
"home_director": "反町　康治",
"away_team": "コンサドーレ札幌",
"weather": "晴",
"series_number": 34,
"temperature": 23.8,
"away_score": 2,
"away_start_member": "李　昊乗,パウロン,河合　竜二,奈良　竜樹,石井　謙伍,宮澤　裕樹,上里　一将,上原　慎也,前田　俊介,中原　彰吾,都倉　賢",
"home_score": 1,
"home_shoot": 10,
"game_id": "16342",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/09/28 13:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"大分トリニータ",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "武田　洋平,若狭　大志,高木　和道,安川　有,西　弘則,為田　大貴,伊藤　大介,ダニエル,末吉　隼也,林　容平,伊佐　耕平",
"away_shoot": 14,
"home_director": "田坂　和昭",
"away_team": "Ｖ・ファーレン長崎",
"weather": "晴",
"series_number": 34,
"temperature": 27.3,
"away_score": 1,
"away_start_member": "植草　裕樹,髙杉　亮太,山口　貴弘,野田　紘史,古部　健太,前田　悠佑,三原　雅俊,石神　直哉,奥埜　博亮,東　浩史,佐藤　洸一",
"home_score": 1,
"home_shoot": 4,
"game_id": "16348",
"home_team": "大分トリニータ",
"game_start_at": "2014/09/28 13:03",
"referee": "家本　政明"
},
{
"teams": [
"カターレ富山",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "廣永　遼太郎,池端　陽介,秋本　倫孝,パク　テホン,前　貴之,キム　ヨングン,大西　容平,内田　健太,木本　敬介,宮吉　拓実,苔口　卓也",
"away_shoot": 14,
"home_director": "安間　貴義",
"away_team": "アビスパ福岡",
"weather": "晴",
"series_number": 34,
"temperature": 26,
"away_score": 2,
"away_start_member": "神山　竜一,山口　和樹,パク　ゴン,イ　グァンソン,堤　俊輔,中原　秀人,武田　英二郎,鍋田　亜人夢,三島　勇太,城後　寿,酒井　宣福",
"home_score": 1,
"home_shoot": 10,
"game_id": "16343",
"home_team": "カターレ富山",
"game_start_at": "2014/09/28 13:04",
"referee": "長谷　拓"
},
{
"teams": [
"ファジアーノ岡山",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "中林　洋次,久木田　紳吾,竹田　忠嗣,後藤　圭太,田中　奏一,千明　聖典,上田　康太,田所　諒,片山　瑛一,押谷　祐樹,久保　裕一",
"away_shoot": 8,
"home_director": "影山　雅永",
"away_team": "水戸ホーリーホック",
"weather": "晴",
"series_number": 34,
"temperature": 28.1,
"away_score": 1,
"away_start_member": "笠原　昂史,新里　亮,金　聖基,尾本　敬,田中　雄大,石神　幸征,船谷　圭祐,広瀬　陸斗,吉田　眞紀人,鈴木　隆行,山村　佑樹",
"home_score": 1,
"home_shoot": 8,
"game_id": "16346",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/09/28 13:05",
"referee": "三上　正一郎"
},
{
"teams": [
"ロアッソ熊本",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "畑　実,藏川　洋平,篠原　弘次郎,橋本　拳人,園田　拓也,澤田　崇,中山　雄登,髙柳　一誠,仲間　隼斗,巻　誠一郎,齊藤　和樹",
"away_shoot": 7,
"home_director": "小野　剛",
"away_team": "ギラヴァンツ北九州",
"weather": "晴",
"series_number": 34,
"temperature": 30.8,
"away_score": 1,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,多田　高行,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"home_score": 0,
"home_shoot": 10,
"game_id": "16347",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/09/28 13:05",
"referee": "前田　拓哉"
},
{
"teams": [
"モンテディオ山形",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "山岸　範宏,舩津　徹也,當間　建文,石井　秀典,石川　竜也,松岡　亮輔,宮阪　政樹,キム　ボムヨン,山﨑　雅人,ディエゴ,川西　翔太",
"away_shoot": 9,
"home_director": "石﨑　信弘",
"away_team": "カマタマーレ讃岐",
"weather": "晴",
"series_number": 34,
"temperature": 22.8,
"away_score": 0,
"away_start_member": "瀬口　拓弥,武田　有祐,藤井　大輔,藤井　航大,小澤　雄希,西野　泰正,山本　翔平,岡村　和哉,関原　凌河,古田　寛幸,アンドレア",
"home_score": 4,
"home_shoot": 17,
"game_id": "16338",
"home_team": "モンテディオ山形",
"game_start_at": "2014/09/28 16:04",
"referee": "塚田　智宏"
},
{
"teams": [
"ジュビロ磐田",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "八田　直樹,櫻内　渚,伊野波　雅彦,森下　俊,駒野　友一,フェルジナンド,藤田　義明,松浦　拓弥,小林　祐希,松井　大輔,前田　遼一",
"away_shoot": 2,
"home_director": "名波　浩",
"away_team": "愛媛ＦＣ",
"weather": "晴",
"series_number": 34,
"temperature": 24.1,
"away_score": 0,
"away_start_member": "児玉　剛,代　健司,林堂　眞,浦田　延尚,キム　ミンジェ,渡邊　一仁,村上　巧,堀米　勇輝,藤　直也,西田　剛,河原　和寿",
"home_score": 2,
"home_shoot": 15,
"game_id": "16344",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/09/28 16:04",
"referee": "野田　祐樹"
},
{
"teams": [
"ザスパクサツ群馬",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "富居　大樹,久富　良輔,有薗　真吾,クォン　ハンジン,小柳　達司,永田　亮太,加藤　弘堅,黄　誠秀,小林　竜樹,ダニエル　ロビーニョ,平繁　龍一",
"away_shoot": 4,
"home_director": "秋葉　忠宏",
"away_team": "栃木ＳＣ",
"weather": "晴",
"series_number": 34,
"temperature": 23.8,
"away_score": 0,
"away_start_member": "鈴木　智幸,山形　辰徳,赤井　秀行,チャ　ヨンファン,荒堀　謙次,廣瀬　浩二,小野寺　達也,中美　慶哉,近藤　祐介,西川　優大,杉本　真",
"home_score": 2,
"home_shoot": 12,
"game_id": "16339",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/09/28 18:04",
"referee": "村上　伸次"
},
{
"teams": [
"京都サンガF.C.",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,福村　貴幸,田森　大己,工藤　浩平,中山　博貴,田中　英雄,駒井　善成,大黒　将志",
"away_shoot": 6,
"home_director": "川勝　良一",
"away_team": "横浜ＦＣ",
"weather": "晴",
"series_number": 34,
"temperature": 22.6,
"away_score": 1,
"away_start_member": "南　雄太,野上　結貴,松下　裕樹,ドウグラス,中島　崇典,佐藤　謙介,寺田　紳一,小池　純輝,松下　年宏,小野瀬　康介,パク　ソンホ",
"home_score": 2,
"home_shoot": 8,
"game_id": "16345",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/09/28 18:04",
"referee": "井上　知大"
},
{
"teams": [
"ジェフユナイテッド千葉",
"東京ヴェルディ"
],
"away_director": "冨樫　剛一",
"home_start_member": "高木　駿,大岩　一貴,キム　ヒョヌン,山口　智,中村　太亮,佐藤　勇人,佐藤　健太郎,幸野　志有人,町田　也真人,谷澤　達也,森本　貴幸",
"away_shoot": 14,
"home_director": "関塚　隆",
"away_team": "東京ヴェルディ",
"weather": "晴",
"series_number": 34,
"temperature": 20.3,
"away_score": 0,
"away_start_member": "佐藤　優也,安西　幸輝,金　鐘必,井林　章,安在　和樹,中後　雅喜,ニウド,澤井　直人,鈴木　惇,平本　一樹,杉本　竜士",
"home_score": 0,
"home_shoot": 15,
"game_id": "16340",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/09/28 19:03",
"referee": "小屋　幸栄"
},
{
"teams": [
"湘南ベルマーレ",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "秋元　陽太,島村　毅,丸山　祐市,三竿　雄斗,亀川　諒史,岩尾　憲,永木　亮太,菊池　大介,大竹　洋平,ウェリントン,岡田　翔平",
"away_shoot": 2,
"home_director": "曺　貴裁",
"away_team": "ＦＣ岐阜",
"weather": "晴",
"series_number": 34,
"temperature": 22.5,
"away_score": 0,
"away_start_member": "川口　能活,深谷　友基,中村　英之,阿部　正紀,益山　司,須藤　右介,髙地　系治,森　勇介,清本　拓己,ナザリト,難波　宏明",
"home_score": 0,
"home_shoot": 14,
"game_id": "16341",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/09/28 19:04",
"referee": "中村　太"
},
{
"teams": [
"栃木ＳＣ",
"京都サンガF.C."
],
"away_director": "川勝　良一",
"home_start_member": "鈴木　智幸,山形　辰徳,赤井　秀行,チャ　ヨンファン,荒堀　謙次,廣瀬　浩二,岡根　直哉,本間　勲,近藤　祐介,杉本　真,大久保　哲哉",
"away_shoot": 12,
"home_director": "阪倉　裕二",
"away_team": "京都サンガF.C.",
"weather": "曇一時雨",
"series_number": 35,
"temperature": 22.6,
"away_score": 1,
"away_start_member": "オ　スンフン,酒井　隆介,内野　貴志,石櫃　洋祐,福村　貴幸,田中　英雄,田森　大己,中山　博貴,駒井　善成,ドウグラス,大黒　将志",
"home_score": 2,
"home_shoot": 8,
"game_id": "16350",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/10/04 13:03",
"referee": "塚田　健太"
},
{
"teams": [
"東京ヴェルディ",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "佐藤　優也,安西　幸輝,井林　章,金　鐘必,安在　和樹,ニウド,中後　雅喜,澤井　直人,鈴木　惇,平本　一樹,杉本　竜士",
"away_shoot": 7,
"home_director": "冨樫　剛一",
"away_team": "ロアッソ熊本",
"weather": "曇",
"series_number": 35,
"temperature": 25.1,
"away_score": 0,
"away_start_member": "畑　実,黒木　晃平,園田　拓也,橋本　拳人,片山　奨典,澤田　崇,中山　雄登,髙柳　一誠,仲間　隼斗,岡本　賢明,齊藤　和樹",
"home_score": 1,
"home_shoot": 8,
"game_id": "16352",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/10/04 13:03",
"referee": "野田　祐樹"
},
{
"teams": [
"横浜ＦＣ",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "南　雄太,野上　結貴,渡辺　匠,ドウグラス,中島　崇典,松下　裕樹,寺田　紳一,松下　年宏,小池　純輝,野崎　陽介,パク　ソンホ",
"away_shoot": 20,
"home_director": "山口　素弘",
"away_team": "松本山雅ＦＣ",
"weather": "曇",
"series_number": 35,
"temperature": 26,
"away_score": 2,
"away_start_member": "村山　智彦,犬飼　智也,大久保　裕樹,飯田　真輝,田中　隼磨,岩沼　俊介,岩間　雄大,岩上　祐三,喜山　康平,船山　貴之,山本　大貴",
"home_score": 0,
"home_shoot": 8,
"game_id": "16358",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/10/04 13:03",
"referee": "山本　雄大"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "植草　裕樹,前田　悠佑,山口　貴弘,髙杉　亮太,古部　健太,三原　雅俊,井上　裕大,石神　直哉,奥埜　博亮,東　浩史,佐藤　洸一",
"away_shoot": 4,
"home_director": "高木　琢也",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 35,
"temperature": 23.1,
"away_score": 1,
"away_start_member": "中林　洋次,久木田　紳吾,竹田　忠嗣,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,片山　瑛一,久保　裕一,ウーゴ",
"home_score": 1,
"home_shoot": 14,
"game_id": "16359",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/10/04 13:03",
"referee": "森川　浩次"
},
{
"teams": [
"大分トリニータ",
"ジュビロ磐田"
],
"away_director": "名波　浩",
"home_start_member": "武田　洋平,若狭　大志,高木　和道,阪田　章裕,土岐田　洸平,木村　祐志,ダニエル,末吉　隼也,西　弘則,為田　大貴,林　容平",
"away_shoot": 9,
"home_director": "田坂　和昭",
"away_team": "ジュビロ磐田",
"weather": "晴時々曇",
"series_number": 35,
"temperature": 23.4,
"away_score": 0,
"away_start_member": "八田　直樹,櫻内　渚,伊野波　雅彦,森下　俊,駒野　友一,藤田　義明,宮崎　智彦,松浦　拓弥,松井　大輔,阿部　吉朗,前田　遼一",
"home_score": 2,
"home_shoot": 6,
"game_id": "16357",
"home_team": "大分トリニータ",
"game_start_at": "2014/10/04 14:03",
"referee": "松尾　一"
},
{
"teams": [
"カマタマーレ讃岐",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "瀬口　拓弥,武田　有祐,エブソン,藤井　航大,小澤　雄希,西野　泰正,岡村　和哉,山本　翔平,高木　和正,古田　寛幸,高橋　泰",
"away_shoot": 6,
"home_director": "北野　誠",
"away_team": "ザスパクサツ群馬",
"weather": "曇時々晴",
"series_number": 35,
"temperature": 25.5,
"away_score": 0,
"away_start_member": "富居　大樹,黄　誠秀,クォン　ハンジン,有薗　真吾,久富　良輔,加藤　弘堅,永田　亮太,瀬川　和樹,ダニエル　ロビーニョ,平繁　龍一,宮崎　泰右",
"home_score": 1,
"home_shoot": 13,
"game_id": "16355",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/10/04 15:01",
"referee": "吉田　哲朗"
},
{
"teams": [
"水戸ホーリーホック",
"コンサドーレ札幌"
],
"away_director": "バルバリッチ",
"home_start_member": "笠原　昂史,新里　亮,金　聖基,細川　淳矢,田中　雄大,石神　幸征,船谷　圭祐,鈴木　雄斗,吉田　眞紀人,鈴木　隆行,山村　佑樹",
"away_shoot": 10,
"home_director": "柱谷　哲二",
"away_team": "コンサドーレ札幌",
"weather": "曇",
"series_number": 35,
"temperature": 22,
"away_score": 0,
"away_start_member": "金山　隼樹,パウロン,薗田　淳,奈良　竜樹,石井　謙伍,宮澤　裕樹,上里　一将,上原　慎也,荒野　拓馬,中原　彰吾,都倉　賢",
"home_score": 0,
"home_shoot": 8,
"game_id": "16349",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/10/04 16:03",
"referee": "河合　英治"
},
{
"teams": [
"ジェフユナイテッド千葉",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "高木　駿,山口　慶,キム　ヒョヌン,山口　智,中村　太亮,佐藤　勇人,佐藤　健太郎,幸野　志有人,町田　也真人,谷澤　達也,森本　貴幸",
"away_shoot": 12,
"home_director": "関塚　隆",
"away_team": "アビスパ福岡",
"weather": "曇",
"series_number": 35,
"temperature": 24.4,
"away_score": 0,
"away_start_member": "神山　竜一,三島　勇太,パク　ゴン,イ　グァンソン,堤　俊輔,中原　秀人,鍋田　亜人夢,武田　英二郎,金森　健志,城後　寿,酒井　宣福",
"home_score": 3,
"home_shoot": 22,
"game_id": "16351",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/10/04 16:03",
"referee": "佐藤　隆治"
},
{
"teams": [
"ＦＣ岐阜",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "川口　能活,田中　秀人,中村　英之,阿部　正紀,須藤　右介,宮沢　正史,益山　司,太田　圭輔,森　勇介,難波　宏明,ナザリト",
"away_shoot": 9,
"home_director": "ラモス　瑠偉",
"away_team": "モンテディオ山形",
"weather": "曇",
"series_number": 35,
"temperature": 23.5,
"away_score": 0,
"away_start_member": "山岸　範宏,小林　亮,舩津　徹也,石井　秀典,石川　竜也,松岡　亮輔,宮阪　政樹,キム　ボムヨン,山﨑　雅人,ディエゴ,川西　翔太",
"home_score": 1,
"home_shoot": 9,
"game_id": "16354",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/10/04 16:04",
"referee": "前田　拓哉"
},
{
"teams": [
"ギラヴァンツ北九州",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,多田　高行,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"away_shoot": 11,
"home_director": "柱谷　幸一",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 35,
"temperature": 20.6,
"away_score": 2,
"away_start_member": "廣永　遼太郎,池端　陽介,秋本　倫孝,パク　テホン,前　貴之,キム　ヨングン,大西　容平,内田　健太,木本　敬介,宮吉　拓実,苔口　卓也",
"home_score": 2,
"home_shoot": 16,
"game_id": "16356",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/10/04 18:03",
"referee": "篠藤　巧"
},
{
"teams": [
"湘南ベルマーレ",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,宇佐美　宏和,熊谷　アンドリュー,永木　亮太,菊池　大介,大竹　洋平,ウェリントン,武富　孝介",
"away_shoot": 14,
"home_director": "曺　貴裁",
"away_team": "愛媛ＦＣ",
"weather": "曇",
"series_number": 35,
"temperature": 23.1,
"away_score": 0,
"away_start_member": "児玉　剛,浦田　延尚,代　健司,林堂　眞,村上　佑介,渡邊　一仁,原川　力,堀米　勇輝,キム　ミンジェ,渡辺　亮太,河原　和寿",
"home_score": 3,
"home_shoot": 19,
"game_id": "16353",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/10/04 19:04",
"referee": "東城　穣"
},
{
"teams": [
"鹿島アントラーズ",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "曽ヶ端　準,西　大伍,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,赤﨑　秀平",
"away_shoot": 12,
"home_director": "トニーニョ　セレーゾ",
"away_team": "ガンバ大阪",
"weather": "雨",
"series_number": 27,
"temperature": 17.8,
"away_score": 3,
"away_start_member": "東口　順昭,米倉　恒貴,丹羽　大輝,岩下　敬輔,オ　ジェソク,今野　泰幸,遠藤　保仁,阿部　浩之,大森　晃太郎,宇佐美　貴史,パトリック",
"home_score": 2,
"home_shoot": 20,
"game_id": "15904",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/10/05 12:34",
"referee": "吉田　寿光"
},
{
"teams": [
"浦和レッズ",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,鈴木　啓太,宇賀神　友弥,柏木　陽介,李　忠成,興梠　慎三",
"away_shoot": 1,
"home_director": "ペトロヴィッチ",
"away_team": "徳島ヴォルティス",
"weather": "雨",
"series_number": 27,
"temperature": 16.4,
"away_score": 1,
"away_start_member": "長谷川　徹,藤原　広太朗,福元　洋平,橋内　優也,アレックス,エステバン,濱田　武,大﨑　淳矢,衛藤　裕,佐々木　一輝,高崎　寛之",
"home_score": 2,
"home_shoot": 13,
"game_id": "15905",
"home_team": "浦和レッズ",
"game_start_at": "2014/10/05 14:04",
"referee": "廣瀬　格"
},
{
"teams": [
"清水エスパルス",
"セレッソ大阪"
],
"away_director": "大熊　裕司",
"home_start_member": "櫛引　政敏,河井　陽介,ヤコヴィッチ,平岡　康裕,吉田　豊,本田　拓也,大前　元紀,六平　光成,石毛　秀樹,ノヴァコヴィッチ,高木　俊幸",
"away_shoot": 8,
"home_director": "大榎　克己",
"away_team": "セレッソ大阪",
"weather": "雨",
"series_number": 27,
"temperature": 19.1,
"away_score": 0,
"away_start_member": "キム　ジンヒョン,藤本　康太,新井場　徹,酒本　憲幸,山下　達也,扇原　貴宏,永井　龍,楠神　順平,キム　ソンジュン,杉本　健勇,カカウ",
"home_score": 3,
"home_shoot": 18,
"game_id": "15909",
"home_team": "清水エスパルス",
"game_start_at": "2014/10/05 14:04",
"referee": "榎本　一慶"
},
{
"teams": [
"ヴィッセル神戸",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "山本　海人,チョン　ウヨン,増川　隆洋,岩波　拓也,枝村　匠馬,シンプリシオ,森岡　亮太,高橋　峻希,相馬　崇人,マルキーニョス,ペドロ　ジュニオール",
"away_shoot": 14,
"home_director": "安達　亮",
"away_team": "名古屋グランパス",
"weather": "屋内",
"series_number": 27,
"temperature": 24.8,
"away_score": 3,
"away_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,松田　力,ダニルソン,田口　泰士,矢田　旭,川又　堅碁,永井　謙佑",
"home_score": 1,
"home_shoot": 15,
"game_id": "15910",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/10/05 15:03",
"referee": "家本　政明"
},
{
"teams": [
"サガン鳥栖",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 11,
"home_director": "吉田　恵",
"away_team": "横浜Ｆ・マリノス",
"weather": "曇",
"series_number": 27,
"temperature": 22.1,
"away_score": 0,
"away_start_member": "榎本　哲也,奈良輪　雄太,中澤　佑二,ファビオ,下平　匠,三門　雄大,富澤　清太郎,藤本　淳吾,佐藤　優平,兵藤　慎剛,伊藤　翔",
"home_score": 1,
"home_shoot": 11,
"game_id": "15911",
"home_team": "サガン鳥栖",
"game_start_at": "2014/10/05 15:04",
"referee": "村上　伸次"
},
{
"teams": [
"ベガルタ仙台",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,梁　勇基,野沢　拓也,赤嶺　真吾,ウイルソン",
"away_shoot": 7,
"home_director": "渡邉　晋",
"away_team": "ＦＣ東京",
"weather": "雨",
"series_number": 27,
"temperature": 15.6,
"away_score": 0,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,河野　広貴,エドゥー,武藤　嘉紀",
"home_score": 1,
"home_shoot": 11,
"game_id": "15903",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/10/05 15:34",
"referee": "窪田　陽輔"
},
{
"teams": [
"柏レイソル",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "桐畑　和繁,藤田　優人,鈴木　大輔,増嶋　竜也,橋本　和,小林　祐介,エドゥアルド,大谷　秀和,高山　薫,レアンドロ,工藤　壮人",
"away_shoot": 6,
"home_director": "ネルシーニョ",
"away_team": "サンフレッチェ広島",
"weather": "雨",
"series_number": 27,
"temperature": 16.3,
"away_score": 0,
"away_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,清水　航平,青山　敏弘,森﨑　和幸,柏　好文,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"home_score": 0,
"home_shoot": 7,
"game_id": "15906",
"home_team": "柏レイソル",
"game_start_at": "2014/10/05 15:34",
"referee": "木村　博之"
},
{
"teams": [
"ヴァンフォーレ甲府",
"大宮アルディージャ"
],
"away_director": "渋谷　洋樹",
"home_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,ジウシーニョ,保坂　一成,新井　涼平,阿部　翔平,河本　明人,阿部　拓馬,クリスティアーノ",
"away_shoot": 9,
"home_director": "城福　浩",
"away_team": "大宮アルディージャ",
"weather": "雨",
"series_number": 27,
"temperature": 16.9,
"away_score": 1,
"away_start_member": "北野　貴之,今井　智基,横山　知伸,高橋　祥平,和田　拓也,カルリーニョス,金澤　慎,泉澤　仁,家長　昭博,富山　貴光,ズラタン",
"home_score": 0,
"home_shoot": 8,
"game_id": "15907",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/10/05 17:04",
"referee": "飯田　淳平"
},
{
"teams": [
"アルビレックス新潟",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "守田　達弥,松原　健,大井　健太郎,大野　和成,小泉　慶,レオ　シルバ,小林　裕紀,山本　康裕,田中　亜土夢,ラファエル　シルバ,指宿　洋史",
"away_shoot": 8,
"home_director": "柳下　正明",
"away_team": "川崎フロンターレ",
"weather": "雨のち曇",
"series_number": 27,
"temperature": 18.6,
"away_score": 0,
"away_start_member": "西部　洋平,田中　裕介,ジェシ,井川　祐輔,小宮山　尊信,谷口　彰悟,大島　僚太,中村　憲剛,森谷　賢太郎,小林　悠,大久保　嘉人",
"home_score": 3,
"home_shoot": 14,
"game_id": "15908",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/10/05 19:04",
"referee": "西村　雄一"
},
{
"teams": [
"コンサドーレ札幌",
"ジェフユナイテッド千葉"
],
"away_director": "関塚　隆",
"home_start_member": "金山　隼樹,櫛引　一紀,奈良　竜樹,薗田　淳,荒野　拓馬,宮澤　裕樹,上里　一将,石井　謙伍,菊岡　拓朗,中原　彰吾,都倉　賢",
"away_shoot": 9,
"home_director": "バルバリッチ",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 36,
"temperature": 14.3,
"away_score": 2,
"away_start_member": "高木　駿,山口　慶,キム　ヒョヌン,山口　智,中村　太亮,佐藤　勇人,佐藤　健太郎,幸野　志有人,町田　也真人,谷澤　達也,森本　貴幸",
"home_score": 0,
"home_shoot": 17,
"game_id": "16360",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/10/11 13:03",
"referee": "村上　伸次"
},
{
"teams": [
"松本山雅ＦＣ",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "村山　智彦,犬飼　智也,大久保　裕樹,飯田　真輝,田中　隼磨,岩沼　俊介,岩間　雄大,岩上　祐三,喜山　康平,船山　貴之,山本　大貴",
"away_shoot": 9,
"home_director": "反町　康治",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 36,
"temperature": 22.3,
"away_score": 0,
"away_start_member": "武田　洋平,若狭　大志,高木　和道,安川　有,為田　大貴,ダニエル,伊藤　大介,土岐田　洸平,末吉　隼也,木村　祐志,林　容平",
"home_score": 2,
"home_shoot": 12,
"game_id": "16366",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/10/11 13:03",
"referee": "岡部　拓人"
},
{
"teams": [
"アビスパ福岡",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "神山　竜一,パク　ゴン,イ　グァンソン,堤　俊輔,三島　勇太,阿部　巧,中原　秀人,武田　英二郎,酒井　宣福,城後　寿,金森　健志",
"away_shoot": 8,
"home_director": "マリヤン　プシュニク",
"away_team": "カマタマーレ讃岐",
"weather": "晴のち曇",
"series_number": 36,
"temperature": 24.2,
"away_score": 2,
"away_start_member": "瀬口　拓弥,武田　有祐,エブソン,藤井　航大,小澤　雄希,古田　寛幸,西野　泰正,山本　翔平,高木　和正,高橋　泰,アンドレア",
"home_score": 1,
"home_shoot": 18,
"game_id": "16370",
"home_team": "アビスパ福岡",
"game_start_at": "2014/10/11 13:04",
"referee": "日高　晴樹"
},
{
"teams": [
"ザスパクサツ群馬",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "富居　大樹,久富　良輔,有薗　真吾,クォン　ハンジン,小柳　達司,永田　亮太,加藤　弘堅,黄　誠秀,小林　竜樹,青木　孝太,平繁　龍一",
"away_shoot": 14,
"home_director": "秋葉　忠宏",
"away_team": "ファジアーノ岡山",
"weather": "晴",
"series_number": 36,
"temperature": 23.3,
"away_score": 2,
"away_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,田所　諒,田中　奏一,千明　聖典,上田　康太,三村　真,押谷　祐樹,妹尾　隆佑,久保　裕一",
"home_score": 3,
"home_shoot": 11,
"game_id": "16364",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/10/11 13:05",
"referee": "野田　祐樹"
},
{
"teams": [
"栃木ＳＣ",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "鈴木　智幸,山形　辰徳,赤井　秀行,岡根　直哉,荒堀　謙次,廣瀬　浩二,本間　勲,小野寺　達也,近藤　祐介,杉本　真,大久保　哲哉",
"away_shoot": 8,
"home_director": "阪倉　裕二",
"away_team": "ギラヴァンツ北九州",
"weather": "晴",
"series_number": 36,
"temperature": 22.6,
"away_score": 1,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,多田　高行,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"home_score": 1,
"home_shoot": 13,
"game_id": "16363",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/10/11 14:03",
"referee": "長谷　拓"
},
{
"teams": [
"モンテディオ山形",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "山岸　範宏,小林　亮,舩津　徹也,石井　秀典,石川　竜也,松岡　亮輔,宮阪　政樹,キム　ボムヨン,山﨑　雅人,ディエゴ,川西　翔太",
"away_shoot": 8,
"home_director": "石﨑　信弘",
"away_team": "Ｖ・ファーレン長崎",
"weather": "晴",
"series_number": 36,
"temperature": 18.6,
"away_score": 1,
"away_start_member": "植草　裕樹,前田　悠佑,山口　貴弘,髙杉　亮太,古部　健太,三原　雅俊,井上　裕大,石神　直哉,奥埜　博亮,東　浩史,佐藤　洸一",
"home_score": 2,
"home_shoot": 12,
"game_id": "16361",
"home_team": "モンテディオ山形",
"game_start_at": "2014/10/11 14:04",
"referee": "上田　益也"
},
{
"teams": [
"ジュビロ磐田",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "八田　直樹,櫻内　渚,伊野波　雅彦,森下　俊,駒野　友一,藤田　義明,宮崎　智彦,松浦　拓弥,小林　祐希,松井　大輔,前田　遼一",
"away_shoot": 14,
"home_director": "名波　浩",
"away_team": "ＦＣ岐阜",
"weather": "曇",
"series_number": 36,
"temperature": 22,
"away_score": 1,
"away_start_member": "川口　能活,田中　秀人,木谷　公亮,阿部　正紀,益山　司,ヘニキ,髙地　系治,森　勇介,クレイトン　ドミンゲス,遠藤　純輝,難波　宏明",
"home_score": 3,
"home_shoot": 8,
"game_id": "16367",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/10/11 15:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"水戸ホーリーホック",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "本間　幸司,田向　泰輝,金　聖基,新里　亮,田中　雄大,船谷　圭祐,石神　幸征,鈴木　雄斗,小澤　司,三島　康平,吉田　眞紀人",
"away_shoot": 8,
"home_director": "柱谷　哲二",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 36,
"temperature": 17.3,
"away_score": 3,
"away_start_member": "廣永　遼太郎,池端　陽介,パク　テホン,平出　涼,前　貴之,井澤　惇,大西　容平,内田　健太,木本　敬介,宮吉　拓実,苔口　卓也",
"home_score": 2,
"home_shoot": 12,
"game_id": "16362",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/10/11 16:03",
"referee": "井上　知大"
},
{
"teams": [
"東京ヴェルディ",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "佐藤　優也,安西　幸輝,金　鐘必,井林　章,安在　和樹,ニウド,中後　雅喜,澤井　直人,鈴木　惇,平本　一樹,常盤　聡",
"away_shoot": 7,
"home_director": "冨樫　剛一",
"away_team": "湘南ベルマーレ",
"weather": "晴",
"series_number": 36,
"temperature": 21.7,
"away_score": 0,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,宇佐美　宏和,岩尾　憲,永木　亮太,菊池　大介,大竹　洋平,ウェリントン,武富　孝介",
"home_score": 0,
"home_shoot": 10,
"game_id": "16365",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/10/11 16:03",
"referee": "岡　宏道"
},
{
"teams": [
"京都サンガF.C.",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "杉本　大地,石櫃　洋祐,バヤリッツァ,酒井　隆介,福村　貴幸,田森　大己,駒井　善成,工藤　浩平,ドウグラス,磐瀬　剛,大黒　将志",
"away_shoot": 5,
"home_director": "川勝　良一",
"away_team": "ロアッソ熊本",
"weather": "曇時々晴",
"series_number": 36,
"temperature": 23.1,
"away_score": 0,
"away_start_member": "畑　実,片山　奨典,橋本　拳人,園田　拓也,キム　ビョンヨン,岡本　賢明,髙柳　一誠,養父　雄仁,中山　雄登,齊藤　和樹,澤田　崇",
"home_score": 0,
"home_shoot": 8,
"game_id": "16368",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/10/11 16:04",
"referee": "池内　明彦"
},
{
"teams": [
"愛媛ＦＣ",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "児玉　剛,ハン　ヒフン,村上　佑介,林堂　眞,浦田　延尚,三原　向平,渡邊　一仁,原川　力,堀米　勇輝,西田　剛,河原　和寿",
"away_shoot": 5,
"home_director": "石丸　清隆",
"away_team": "横浜ＦＣ",
"weather": "晴",
"series_number": 36,
"temperature": 21.2,
"away_score": 1,
"away_start_member": "南　雄太,小池　純輝,野上　結貴,ドウグラス,中島　崇典,松下　裕樹,寺田　紳一,松下　年宏,内田　智也,野崎　陽介,黒津　勝",
"home_score": 2,
"home_shoot": 12,
"game_id": "16369",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/10/11 19:04",
"referee": "小屋　幸栄"
},
{
"teams": [
"徳島ヴォルティス",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "長谷川　徹,藤原　広太朗,福元　洋平,橋内　優也,アレックス,斉藤　大介,濱田　武,大﨑　淳矢,衛藤　裕,佐々木　一輝,高崎　寛之",
"away_shoot": 20,
"home_director": "小林　伸二",
"away_team": "ヴィッセル神戸",
"weather": "晴",
"series_number": 28,
"temperature": 19.4,
"away_score": 2,
"away_start_member": "徳重　健太,高橋　峻希,岩波　拓也,増川　隆洋,相馬　崇人,チョン　ウヨン,枝村　匠馬,小川　慶治朗,ペドロ　ジュニオール,シンプリシオ,マルキーニョス",
"home_score": 2,
"home_shoot": 6,
"game_id": "15919",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/10/18 13:04",
"referee": "中村　太"
},
{
"teams": [
"ベガルタ仙台",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,梁　勇基,野沢　拓也,赤嶺　真吾,ウイルソン",
"away_shoot": 9,
"home_director": "渡邉　晋",
"away_team": "浦和レッズ",
"weather": "晴",
"series_number": 28,
"temperature": 19.8,
"away_score": 2,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,鈴木　啓太,宇賀神　友弥,柏木　陽介,李　忠成,興梠　慎三",
"home_score": 4,
"home_shoot": 11,
"game_id": "15912",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/10/18 14:04",
"referee": "家本　政明"
},
{
"teams": [
"鹿島アントラーズ",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,ダヴィ",
"away_shoot": 11,
"home_director": "トニーニョ　セレーゾ",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 28,
"temperature": 18.4,
"away_score": 3,
"away_start_member": "桐畑　和繁,増嶋　竜也,渡部　博文,鈴木　大輔,輪湖　直樹,藤田　優人,茨田　陽生,大谷　秀和,ドゥドゥ,レアンドロ,工藤　壮人",
"home_score": 2,
"home_shoot": 19,
"game_id": "15913",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/10/18 14:04",
"referee": "村上　伸次"
},
{
"teams": [
"ガンバ大阪",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "東口　順昭,米倉　恒貴,丹羽　大輝,岩下　敬輔,オ　ジェソク,内田　達也,遠藤　保仁,阿部　浩之,大森　晃太郎,宇佐美　貴史,パトリック",
"away_shoot": 9,
"home_director": "長谷川　健太",
"away_team": "川崎フロンターレ",
"weather": "晴",
"series_number": 28,
"temperature": 22.3,
"away_score": 0,
"away_start_member": "杉山　力裕,田中　裕介,實藤　友紀,谷口　彰悟,登里　享平,大島　僚太,中村　憲剛,小林　悠,レナト,森島　康仁,大久保　嘉人",
"home_score": 1,
"home_shoot": 8,
"game_id": "15917",
"home_team": "ガンバ大阪",
"game_start_at": "2014/10/18 14:04",
"referee": "今村　義朗"
},
{
"teams": [
"横浜Ｆ・マリノス",
"清水エスパルス"
],
"away_director": "大榎　克己",
"home_start_member": "榎本　哲也,小林　祐三,中澤　佑二,ファビオ,下平　匠,兵藤　慎剛,富澤　清太郎,藤本　淳吾,中村　俊輔,佐藤　優平,伊藤　翔",
"away_shoot": 4,
"home_director": "樋口　靖洋",
"away_team": "清水エスパルス",
"weather": "晴",
"series_number": 28,
"temperature": 20.3,
"away_score": 0,
"away_start_member": "櫛引　政敏,河井　陽介,ヤコヴィッチ,平岡　康裕,吉田　豊,六平　光成,本田　拓也,石毛　秀樹,高木　俊幸,大前　元紀,ノヴァコヴィッチ",
"home_score": 1,
"home_shoot": 15,
"game_id": "15915",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/10/18 15:03",
"referee": "東城　穣"
},
{
"teams": [
"アルビレックス新潟",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,小泉　慶,レオ　シルバ,小林　裕紀,山本　康裕,田中　亜土夢,指宿　洋史,鈴木　武蔵",
"away_shoot": 5,
"home_director": "柳下　正明",
"away_team": "ヴァンフォーレ甲府",
"weather": "晴",
"series_number": 28,
"temperature": 19.3,
"away_score": 0,
"away_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,ジウシーニョ,新井　涼平,マルキーニョス　パラナ,阿部　翔平,河本　明人,阿部　拓馬,キリノ",
"home_score": 0,
"home_shoot": 1,
"game_id": "15916",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/10/18 15:03",
"referee": "井上　知大"
},
{
"teams": [
"サンフレッチェ広島",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,柏　好文,青山　敏弘,柴﨑　晃誠,山岸　智,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"away_shoot": 10,
"home_director": "森保　一",
"away_team": "名古屋グランパス",
"weather": "晴",
"series_number": 28,
"temperature": 17.3,
"away_score": 0,
"away_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,松田　力,田口　泰士,ダニルソン,矢田　旭,川又　堅碁,永井　謙佑",
"home_score": 4,
"home_shoot": 11,
"game_id": "15918",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/10/18 16:04",
"referee": "窪田　陽輔"
},
{
"teams": [
"大宮アルディージャ",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "北野　貴之,今井　智基,横山　知伸,高橋　祥平,和田　拓也,カルリーニョス,金澤　慎,家長　昭博,泉澤　仁,ズラタン,ムルジャ",
"away_shoot": 15,
"home_director": "渋谷　洋樹",
"away_team": "ＦＣ東京",
"weather": "晴",
"series_number": 28,
"temperature": 19.1,
"away_score": 0,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,カニーニ,太田　宏介,高橋　秀人,米本　拓司,三田　啓貴,河野　広貴,渡邉　千真,武藤　嘉紀",
"home_score": 1,
"home_shoot": 3,
"game_id": "15914",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/10/18 17:04",
"referee": "上田　益也"
},
{
"teams": [
"サガン鳥栖",
"セレッソ大阪"
],
"away_director": "大熊　裕司",
"home_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 8,
"home_director": "吉田　恵",
"away_team": "セレッソ大阪",
"weather": "晴",
"series_number": 28,
"temperature": 20.1,
"away_score": 0,
"away_start_member": "キム　ジンヒョン,染谷　悠太,丸橋　祐介,酒本　憲幸,山下　達也,扇原　貴宏,長谷川　アーリアジャスール,平野　甲斐,キム　ソンジュン,永井　龍,杉本　健勇",
"home_score": 1,
"home_shoot": 8,
"game_id": "15920",
"home_team": "サガン鳥栖",
"game_start_at": "2014/10/18 19:05",
"referee": "高山　啓義"
},
{
"teams": [
"ファジアーノ岡山",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "中林　洋次,鎌田　翔雅,後藤　圭太,田所　諒,澤口　雅彦,千明　聖典,上田　康太,久木田　紳吾,清水　慎太郎,押谷　祐樹,ウーゴ",
"away_shoot": 13,
"home_director": "影山　雅永",
"away_team": "モンテディオ山形",
"weather": "晴",
"series_number": 37,
"temperature": 23.6,
"away_score": 4,
"away_start_member": "山岸　範宏,山田　拓巳,舩津　徹也,石井　秀典,當間　建文,松岡　亮輔,宮阪　政樹,キム　ボムヨン,山﨑　雅人,ディエゴ,川西　翔太",
"home_score": 1,
"home_shoot": 6,
"game_id": "16380",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/10/19 13:03",
"referee": "岡部　拓人"
},
{
"teams": [
"横浜ＦＣ",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "南　雄太,野上　結貴,松下　裕樹,ドウグラス,永田　拓也,安　英学,寺田　紳一,小池　純輝,松下　年宏,野崎　陽介,黒津　勝",
"away_shoot": 8,
"home_director": "山口　素弘",
"away_team": "栃木ＳＣ",
"weather": "晴",
"series_number": 37,
"temperature": 23.4,
"away_score": 0,
"away_start_member": "鈴木　智幸,山形　辰徳,岡根　直哉,赤井　秀行,荒堀　謙次,近藤　祐介,小野寺　達也,本間　勲,湯澤　洋介,廣瀬　浩二,西川　優大",
"home_score": 3,
"home_shoot": 12,
"game_id": "16372",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/10/19 13:04",
"referee": "篠藤　巧"
},
{
"teams": [
"カターレ富山",
"コンサドーレ札幌"
],
"away_director": "バルバリッチ",
"home_start_member": "廣永　遼太郎,池端　陽介,パク　テホン,平出　涼,田中　寛己,井澤　惇,大西　容平,内田　健太,木本　敬介,宮吉　拓実,苔口　卓也",
"away_shoot": 11,
"home_director": "安間　貴義",
"away_team": "コンサドーレ札幌",
"weather": "晴",
"series_number": 37,
"temperature": 22.3,
"away_score": 2,
"away_start_member": "李　昊乗,パウロン,奈良　竜樹,薗田　淳,荒野　拓馬,宮澤　裕樹,上里　一将,石井　謙伍,中原　彰吾,前田　俊介,都倉　賢",
"home_score": 0,
"home_shoot": 2,
"game_id": "16374",
"home_team": "カターレ富山",
"game_start_at": "2014/10/19 13:04",
"referee": "塚田　智宏"
},
{
"teams": [
"京都サンガF.C.",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "杉本　大地,石櫃　洋祐,バヤリッツァ,酒井　隆介,福村　貴幸,駒井　善成,田森　大己,山瀬　功治,工藤　浩平,三平　和司,大黒　将志",
"away_shoot": 4,
"home_director": "川勝　良一",
"away_team": "松本山雅ＦＣ",
"weather": "晴",
"series_number": 37,
"temperature": 28.3,
"away_score": 0,
"away_start_member": "村山　智彦,田中　隼磨,大久保　裕樹,飯田　真輝,犬飼　智也,岩沼　俊介,岩間　雄大,岩上　祐三,喜山　康平,船山　貴之,山本　大貴",
"home_score": 0,
"home_shoot": 11,
"game_id": "16375",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/10/19 13:04",
"referee": "野田　祐樹"
},
{
"teams": [
"アビスパ福岡",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "神山　竜一,パク　ゴン,イ　グァンソン,堤　俊輔,阿部　巧,武田　英二郎,三島　勇太,森村　昂太,平井　将生,城後　寿,金森　健志",
"away_shoot": 8,
"home_director": "マリヤン　プシュニク",
"away_team": "ザスパクサツ群馬",
"weather": "晴",
"series_number": 37,
"temperature": 25.2,
"away_score": 1,
"away_start_member": "富居　大樹,久富　良輔,有薗　真吾,クォン　ハンジン,夛田　凌輔,永田　亮太,加藤　弘堅,小林　竜樹,青木　孝太,平繁　龍一,ダニエル　ロビーニョ",
"home_score": 1,
"home_shoot": 8,
"game_id": "16377",
"home_team": "アビスパ福岡",
"game_start_at": "2014/10/19 13:04",
"referee": "河合　英治"
},
{
"teams": [
"ジェフユナイテッド千葉",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "高木　駿,山口　慶,キム　ヒョヌン,山口　智,中村　太亮,佐藤　勇人,佐藤　健太郎,幸野　志有人,町田　也真人,谷澤　達也,森本　貴幸",
"away_shoot": 13,
"home_director": "関塚　隆",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 37,
"temperature": 20.6,
"away_score": 1,
"away_start_member": "武田　洋平,若狭　大志,安川　有,高木　和道,阪田　章裕,ダニエル,伊藤　大介,松本　怜,為田　大貴,末吉　隼也,林　容平",
"home_score": 2,
"home_shoot": 9,
"game_id": "16371",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/10/19 16:03",
"referee": "西村　雄一"
},
{
"teams": [
"ロアッソ熊本",
"ジュビロ磐田"
],
"away_director": "名波　浩",
"home_start_member": "畑　実,キム　ビョンヨン,園田　拓也,橋本　拳人,片山　奨典,中山　雄登,養父　雄仁,髙柳　一誠,嶋田　慎太郎,澤田　崇,齊藤　和樹",
"away_shoot": 8,
"home_director": "小野　剛",
"away_team": "ジュビロ磐田",
"weather": "晴",
"series_number": 37,
"temperature": 23.8,
"away_score": 0,
"away_start_member": "八田　直樹,櫻内　渚,坪内　秀介,森下　俊,駒野　友一,藤田　義明,宮崎　智彦,松浦　拓弥,小林　祐希,松井　大輔,前田　遼一",
"home_score": 0,
"home_shoot": 8,
"game_id": "16379",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/10/19 16:03",
"referee": "三上　正一郎"
},
{
"teams": [
"湘南ベルマーレ",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "秋元　陽太,遠藤　航,岩尾　憲,島村　毅,藤田　征也,三竿　雄斗,永木　亮太,亀川　諒史,樋口　寛規,武富　孝介,菊池　大介",
"away_shoot": 5,
"home_director": "曺　貴裁",
"away_team": "Ｖ・ファーレン長崎",
"weather": "晴",
"series_number": 37,
"temperature": 20.3,
"away_score": 2,
"away_start_member": "植草　裕樹,岡本　拓也,髙杉　亮太,武内　大,古部　健太,三原　雅俊,黒木　聖仁,石神　直哉,佐藤　洸一,小松　塁,イ　ヨンジェ",
"home_score": 1,
"home_shoot": 13,
"game_id": "16373",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/10/19 16:04",
"referee": "榎本　一慶"
},
{
"teams": [
"カマタマーレ讃岐",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "瀬口　拓弥,武田　有祐,エブソン,藤井　航大,小澤　雄希,古田　寛幸,山本　翔平,岡村　和哉,高木　和正,高橋　泰,アンドレア",
"away_shoot": 10,
"home_director": "北野　誠",
"away_team": "愛媛ＦＣ",
"weather": "晴",
"series_number": 37,
"temperature": 24,
"away_score": 2,
"away_start_member": "児玉　剛,ハン　ヒフン,村上　佑介,林堂　眞,浦田　延尚,三原　向平,渡邊　一仁,原川　力,堀米　勇輝,西田　剛,河原　和寿",
"home_score": 1,
"home_shoot": 10,
"game_id": "16376",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/10/19 16:04",
"referee": "前田　拓哉"
},
{
"teams": [
"ギラヴァンツ北九州",
"東京ヴェルディ"
],
"away_director": "冨樫　剛一",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,井上　翔太,原　一樹,池元　友樹",
"away_shoot": 10,
"home_director": "柱谷　幸一",
"away_team": "東京ヴェルディ",
"weather": "晴",
"series_number": 37,
"temperature": 21.3,
"away_score": 1,
"away_start_member": "佐藤　優也,安西　幸輝,金　鐘必,井林　章,安在　和樹,ニウド,田村　直也,前田　直輝,澤井　直人,南　秀仁,平本　一樹",
"home_score": 2,
"home_shoot": 8,
"game_id": "16378",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/10/19 16:05",
"referee": "吉田　哲朗"
},
{
"teams": [
"ＦＣ岐阜",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "川口　能活,田中　秀人,木谷　公亮,阿部　正紀,岩﨑　陽平,益山　司,ヘニキ,髙地　系治,クレイトン　ドミンゲス,遠藤　純輝,難波　宏明",
"away_shoot": 10,
"home_director": "ラモス　瑠偉",
"away_team": "水戸ホーリーホック",
"weather": "晴",
"series_number": 37,
"temperature": 18.2,
"away_score": 2,
"away_start_member": "笠原　昂史,新里　亮,金　聖基,尾本　敬,石神　幸征,船谷　圭祐,内田　航平,田中　雄大,吉田　眞紀人,馬場　賢治,オズマール",
"home_score": 0,
"home_shoot": 6,
"game_id": "16381",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/10/19 19:04",
"referee": "森川　浩次"
},
{
"teams": [
"柏レイソル",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "桐畑　和繁,藤田　優人,渡部　博文,増嶋　竜也,中谷　進之介,茨田　陽生,大谷　秀和,ドゥドゥ,輪湖　直樹,レアンドロ,工藤　壮人",
"away_shoot": 9,
"home_director": "ネルシーニョ",
"away_team": "ガンバ大阪",
"weather": "雨",
"series_number": 29,
"temperature": 13.9,
"away_score": 0,
"away_start_member": "東口　順昭,米倉　恒貴,丹羽　大輝,岩下　敬輔,藤春　廣輝,明神　智和,今野　泰幸,遠藤　保仁,阿部　浩之,宇佐美　貴史,佐藤　晃大",
"home_score": 1,
"home_shoot": 10,
"game_id": "15922",
"home_team": "柏レイソル",
"game_start_at": "2014/10/22 19:03",
"referee": "岡部　拓人"
},
{
"teams": [
"川崎フロンターレ",
"サガン鳥栖"
],
"away_director": "吉田　恵",
"home_start_member": "杉山　力裕,田中　裕介,實藤　友紀,谷口　彰悟,登里　享平,山本　真希,大島　僚太,森谷　賢太郎,レナト,小林　悠,大久保　嘉人",
"away_shoot": 7,
"home_director": "風間　八宏",
"away_team": "サガン鳥栖",
"weather": "雨",
"series_number": 29,
"temperature": 15.4,
"away_score": 0,
"away_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 2,
"home_shoot": 20,
"game_id": "15928",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/10/22 19:03",
"referee": "吉田　寿光"
},
{
"teams": [
"浦和レッズ",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,鈴木　啓太,梅崎　司,柏木　陽介,李　忠成,興梠　慎三",
"away_shoot": 5,
"home_director": "ペトロヴィッチ",
"away_team": "ヴァンフォーレ甲府",
"weather": "雨",
"series_number": 29,
"temperature": 15.1,
"away_score": 0,
"away_start_member": "荻　晃太,畑尾　大翔,山本　英臣,佐々木　翔,ジウシーニョ,新井　涼平,マルキーニョス　パラナ,阿部　翔平,石原　克哉,阿部　拓馬,キリノ",
"home_score": 0,
"home_shoot": 10,
"game_id": "15921",
"home_team": "浦和レッズ",
"game_start_at": "2014/10/22 19:04",
"referee": "高山　啓義"
},
{
"teams": [
"清水エスパルス",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "櫛引　政敏,河井　陽介,ヤコヴィッチ,平岡　康裕,吉田　豊,本田　拓也,大前　元紀,六平　光成,石毛　秀樹,高木　俊幸,ノヴァコヴィッチ",
"away_shoot": 10,
"home_director": "大榎　克己",
"away_team": "アルビレックス新潟",
"weather": "雨",
"series_number": 29,
"temperature": 15.6,
"away_score": 1,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,小泉　慶,レオ　シルバ,小林　裕紀,田中　亜土夢,山本　康裕,鈴木　武蔵,指宿　洋史",
"home_score": 2,
"home_shoot": 6,
"game_id": "15923",
"home_team": "清水エスパルス",
"game_start_at": "2014/10/22 19:04",
"referee": "家本　政明"
},
{
"teams": [
"名古屋グランパス",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,小川　佳純,田口　泰士,矢田　旭,永井　謙佑,松田　力,川又　堅碁",
"away_shoot": 6,
"home_director": "西野　朗",
"away_team": "ベガルタ仙台",
"weather": "雨のち曇",
"series_number": 29,
"temperature": 17,
"away_score": 0,
"away_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,梁　勇基,野沢　拓也,赤嶺　真吾,ウイルソン",
"home_score": 0,
"home_shoot": 20,
"game_id": "15924",
"home_team": "名古屋グランパス",
"game_start_at": "2014/10/22 19:04",
"referee": "東城　穣"
},
{
"teams": [
"ヴィッセル神戸",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "徳重　健太,高橋　峻希,河本　裕之,増川　隆洋,相馬　崇人,チョン　ウヨン,シンプリシオ,小川　慶治朗,ペドロ　ジュニオール,森岡　亮太,マルキーニョス",
"away_shoot": 14,
"home_director": "安達　亮",
"away_team": "鹿島アントラーズ",
"weather": "屋内",
"series_number": 29,
"temperature": 21.1,
"away_score": 0,
"away_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,豊川　雄太,土居　聖真,赤﨑　秀平",
"home_score": 0,
"home_shoot": 10,
"game_id": "15925",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/10/22 19:04",
"referee": "今村　義朗"
},
{
"teams": [
"大宮アルディージャ",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "北野　貴之,趙　源熙,横山　知伸,高橋　祥平,和田　拓也,カルリーニョス,増田　誓志,渡邉　大剛,泉澤　仁,ズラタン,ムルジャ",
"away_shoot": 10,
"home_director": "渋谷　洋樹",
"away_team": "横浜Ｆ・マリノス",
"weather": "雨",
"series_number": 29,
"temperature": 14.3,
"away_score": 3,
"away_start_member": "榎本　哲也,小林　祐三,中澤　佑二,ファビオ,下平　匠,兵藤　慎剛,富澤　清太郎,藤本　淳吾,中村　俊輔,佐藤　優平,伊藤　翔",
"home_score": 2,
"home_shoot": 12,
"game_id": "15926",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/10/22 19:04",
"referee": "西村　雄一"
},
{
"teams": [
"ＦＣ東京",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,カニーニ,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,渡邉　千真,エドゥー,武藤　嘉紀",
"away_shoot": 14,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "サンフレッチェ広島",
"weather": "雨",
"series_number": 29,
"temperature": 14.1,
"away_score": 1,
"away_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,清水　航平,青山　敏弘,柴﨑　晃誠,柏　好文,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"home_score": 2,
"home_shoot": 10,
"game_id": "15927",
"home_team": "ＦＣ東京",
"game_start_at": "2014/10/22 19:04",
"referee": "榎本　一慶"
},
{
"teams": [
"セレッソ大阪",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "キム　ジンヒョン,染谷　悠太,丸橋　祐介,酒本　憲幸,山下　達也,扇原　貴宏,長谷川　アーリアジャスール,楠神　順平,南野　拓実,永井　龍,杉本　健勇",
"away_shoot": 9,
"home_director": "大熊　裕司",
"away_team": "徳島ヴォルティス",
"weather": "曇時々雨",
"series_number": 29,
"temperature": 17.9,
"away_score": 1,
"away_start_member": "長谷川　徹,藤原　広太朗,福元　洋平,橋内　優也,アレックス,エステバン,濱田　武,大﨑　淳矢,衛藤　裕,アドリアーノ,高崎　寛之",
"home_score": 3,
"home_shoot": 11,
"game_id": "15929",
"home_team": "セレッソ大阪",
"game_start_at": "2014/10/22 19:04",
"referee": "福島　孝一郎"
},
{
"teams": [
"コンサドーレ札幌",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "李　昊乗,パウロン,河合　竜二,奈良　竜樹,荒野　拓馬,宮澤　裕樹,上里　一将,石井　謙伍,前田　俊介,中原　彰吾,都倉　賢",
"away_shoot": 18,
"home_director": "バルバリッチ",
"away_team": "湘南ベルマーレ",
"weather": "屋内",
"series_number": 38,
"temperature": 21.8,
"away_score": 0,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,島村　毅,藤田　征也,熊谷　アンドリュー,岩尾　憲,三竿　雄斗,大竹　洋平,岡田　翔平,武富　孝介",
"home_score": 2,
"home_shoot": 8,
"game_id": "16382",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/10/26 13:03",
"referee": "前田　拓哉"
},
{
"teams": [
"水戸ホーリーホック",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "笠原　昂史,新里　亮,金　聖基,尾本　敬,田中　雄大,西岡　謙太,広瀬　陸斗,船谷　圭祐,吉田　眞紀人,鈴木　隆行,馬場　賢治",
"away_shoot": 12,
"home_director": "柱谷　哲二",
"away_team": "カマタマーレ讃岐",
"weather": "曇時々晴",
"series_number": 38,
"temperature": 22.3,
"away_score": 0,
"away_start_member": "瀬口　拓弥,武田　有祐,岡村　和哉,藤井　航大,小澤　雄希,西野　泰正,山本　翔平,高木　和正,沼田　圭悟,高橋　泰,アンドレア",
"home_score": 0,
"home_shoot": 6,
"game_id": "16384",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/10/26 13:03",
"referee": "小屋　幸栄"
},
{
"teams": [
"栃木ＳＣ",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "鈴木　智幸,山形　辰徳,チャ　ヨンファン,岡根　直哉,荒堀　謙次,廣瀬　浩二,小野寺　達也,本間　勲,近藤　祐介,杉本　真,大久保　哲哉",
"away_shoot": 10,
"home_director": "阪倉　裕二",
"away_team": "アビスパ福岡",
"weather": "曇",
"series_number": 38,
"temperature": 21.6,
"away_score": 1,
"away_start_member": "神山　竜一,イ　グァンソン,パク　ゴン,堤　俊輔,古賀　正紘,中原　秀人,金森　健志,阿部　巧,平井　将生,城後　寿,酒井　宣福",
"home_score": 1,
"home_shoot": 19,
"game_id": "16385",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/10/26 13:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"東京ヴェルディ",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "佐藤　優也,安西　幸輝,金　鐘必,井林　章,安在　和樹,ニウド,中後　雅喜,澤井　直人,鈴木　惇,常盤　聡,平本　一樹",
"away_shoot": 6,
"home_director": "冨樫　剛一",
"away_team": "愛媛ＦＣ",
"weather": "晴のち曇",
"series_number": 38,
"temperature": 23.1,
"away_score": 1,
"away_start_member": "児玉　剛,ハン　ヒフン,村上　佑介,林堂　眞,浦田　延尚,三原　向平,渡邊　一仁,原川　力,堀米　勇輝,西田　剛,河原　和寿",
"home_score": 1,
"home_shoot": 13,
"game_id": "16387",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/10/26 13:03",
"referee": "塚田　健太"
},
{
"teams": [
"松本山雅ＦＣ",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "村山　智彦,犬飼　智也,飯田　真輝,大久保　裕樹,田中　隼磨,岩沼　俊介,岩間　雄大,喜山　康平,岩上　祐三,山本　大貴,船山　貴之",
"away_shoot": 9,
"home_director": "反町　康治",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 38,
"temperature": 20.6,
"away_score": 1,
"away_start_member": "廣永　遼太郎,池端　陽介,平出　涼,パク　テホン,前　貴之,井澤　惇,大西　容平,白崎　凌兵,内田　健太,宮吉　拓実,苔口　卓也",
"home_score": 2,
"home_shoot": 14,
"game_id": "16388",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/10/26 13:03",
"referee": "上田　益也"
},
{
"teams": [
"ベガルタ仙台",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "関　憲太郎,村上　和弘,鎌田　次郎,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,梁　勇基,野沢　拓也,赤嶺　真吾,武藤　雄樹",
"away_shoot": 11,
"home_director": "渡邉　晋",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 30,
"temperature": 20.1,
"away_score": 2,
"away_start_member": "桐畑　和繁,鈴木　大輔,増嶋　竜也,渡部　博文,橋本　和,キム　チャンス,栗澤　僚一,秋野　央樹,ドゥドゥ,レアンドロ,工藤　壮人",
"home_score": 1,
"home_shoot": 9,
"game_id": "15930",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/10/26 13:04",
"referee": "廣瀬　格"
},
{
"teams": [
"モンテディオ山形",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "山岸　範宏,山田　拓巳,舩津　徹也,石井　秀典,當間　建文,松岡　亮輔,宮阪　政樹,キム　ボムヨン,山﨑　雅人,ディエゴ,川西　翔太",
"away_shoot": 13,
"home_director": "石﨑　信弘",
"away_team": "横浜ＦＣ",
"weather": "晴",
"series_number": 38,
"temperature": 20.1,
"away_score": 4,
"away_start_member": "南　雄太,野上　結貴,松下　裕樹,ドウグラス,永田　拓也,安　英学,寺田　紳一,小池　純輝,松下　年宏,野崎　陽介,黒津　勝",
"home_score": 2,
"home_shoot": 11,
"game_id": "16383",
"home_team": "モンテディオ山形",
"game_start_at": "2014/10/26 13:04",
"referee": "中村　太"
},
{
"teams": [
"ザスパクサツ群馬",
"ジェフユナイテッド千葉"
],
"away_director": "関塚　隆",
"home_start_member": "富居　大樹,久富　良輔,有薗　真吾,クォン　ハンジン,小柳　達司,小林　竜樹,永田　亮太,加藤　弘堅,青木　孝太,平繁　龍一,ダニエル　ロビーニョ",
"away_shoot": 12,
"home_director": "秋葉　忠宏",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 38,
"temperature": 22.8,
"away_score": 2,
"away_start_member": "高木　駿,山口　慶,キム　ヒョヌン,山口　智,中村　太亮,佐藤　勇人,佐藤　健太郎,幸野　志有人,町田　也真人,谷澤　達也,森本　貴幸",
"home_score": 1,
"home_shoot": 9,
"game_id": "16386",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/10/26 13:04",
"referee": "井上　知大"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "植草　裕樹,岡本　拓也,髙杉　亮太,前田　悠佑,古部　健太,奥埜　博亮,黒木　聖仁,石神　直哉,佐藤　洸一,小松　塁,イ　ヨンジェ",
"away_shoot": 3,
"home_director": "高木　琢也",
"away_team": "ロアッソ熊本",
"weather": "晴",
"series_number": 38,
"temperature": 25,
"away_score": 1,
"away_start_member": "畑　実,キム　ビョンヨン,園田　拓也,橋本　拳人,片山　奨典,中山　雄登,養父　雄仁,髙柳　一誠,嶋田　慎太郎,澤田　崇,齊藤　和樹",
"home_score": 0,
"home_shoot": 11,
"game_id": "16391",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/10/26 14:03",
"referee": "長谷　拓"
},
{
"teams": [
"ジュビロ磐田",
"京都サンガF.C."
],
"away_director": "川勝　良一",
"home_start_member": "八田　直樹,小川　大貴,伊野波　雅彦,森下　俊,駒野　友一,藤田　義明,宮崎　智彦,松浦　拓弥,小林　祐希,松井　大輔,前田　遼一",
"away_shoot": 12,
"home_director": "名波　浩",
"away_team": "京都サンガF.C.",
"weather": "雨のち曇",
"series_number": 38,
"temperature": 20,
"away_score": 2,
"away_start_member": "杉本　大地,石櫃　洋祐,バヤリッツァ,酒井　隆介,福村　貴幸,田森　大己,横谷　繁,山瀬　功治,工藤　浩平,ドウグラス,大黒　将志",
"home_score": 2,
"home_shoot": 13,
"game_id": "16389",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/10/26 15:04",
"referee": "西村　雄一"
},
{
"teams": [
"ギラヴァンツ北九州",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "大谷　幸輝,宮本　亨,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"away_shoot": 12,
"home_director": "柱谷　幸一",
"away_team": "ＦＣ岐阜",
"weather": "晴",
"series_number": 38,
"temperature": 21.3,
"away_score": 0,
"away_start_member": "太田　岳志,益山　司,ヘニキ,阿部　正紀,田中　秀人,水野　泰輔,髙地　系治,清本　拓己,クレイトン　ドミンゲス,難波　宏明,ナザリト",
"home_score": 2,
"home_shoot": 5,
"game_id": "16390",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/10/26 16:03",
"referee": "岡　宏道"
},
{
"teams": [
"大分トリニータ",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "武田　洋平,土岐田　洸平,高木　和道,安川　有,松本　怜,ダニエル,キム　ジョンヒョン,末吉　隼也,為田　大貴,風間　宏矢,林　容平",
"away_shoot": 9,
"home_director": "田坂　和昭",
"away_team": "ファジアーノ岡山",
"weather": "晴のち曇",
"series_number": 38,
"temperature": 22.8,
"away_score": 0,
"away_start_member": "中林　洋次,久木田　紳吾,竹田　忠嗣,後藤　圭太,澤口　雅彦,島田　譲,上田　康太,田所　諒,清水　慎太郎,関戸　健二,久保　裕一",
"home_score": 1,
"home_shoot": 12,
"game_id": "16392",
"home_team": "大分トリニータ",
"game_start_at": "2014/10/26 16:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"ヴィッセル神戸",
"大宮アルディージャ"
],
"away_director": "渋谷　洋樹",
"home_start_member": "徳重　健太,奥井　諒,河本　裕之,増川　隆洋,相馬　崇人,チョン　ウヨン,シンプリシオ,森岡　亮太,ペドロ　ジュニオール,小川　慶治朗,マルキーニョス",
"away_shoot": 9,
"home_director": "安達　亮",
"away_team": "大宮アルディージャ",
"weather": "晴",
"series_number": 30,
"temperature": 23.6,
"away_score": 1,
"away_start_member": "北野　貴之,今井　智基,横山　知伸,高橋　祥平,和田　拓也,カルリーニョス,増田　誓志,家長　昭博,泉澤　仁,ズラタン,ムルジャ",
"home_score": 2,
"home_shoot": 8,
"game_id": "15933",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/10/26 16:04",
"referee": "東城　穣"
},
{
"teams": [
"サガン鳥栖",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,高橋　義希,岡本　知剛,金　民友,池田　圭,豊田　陽平",
"away_shoot": 7,
"home_director": "吉田　恵",
"away_team": "アルビレックス新潟",
"weather": "曇",
"series_number": 30,
"temperature": 24.1,
"away_score": 2,
"away_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,川口　尚紀,レオ　シルバ,小泉　慶,田中　亜土夢,山本　康裕,鈴木　武蔵,指宿　洋史",
"home_score": 0,
"home_shoot": 9,
"game_id": "15935",
"home_team": "サガン鳥栖",
"game_start_at": "2014/10/26 16:04",
"referee": "池内　明彦"
},
{
"teams": [
"鹿島アントラーズ",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,赤﨑　秀平",
"away_shoot": 10,
"home_director": "トニーニョ　セレーゾ",
"away_team": "浦和レッズ",
"weather": "曇",
"series_number": 30,
"temperature": 21,
"away_score": 1,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,関根　貴大,阿部　勇樹,青木　拓矢,宇賀神　友弥,柏木　陽介,マルシオ　リシャルデス,興梠　慎三",
"home_score": 1,
"home_shoot": 14,
"game_id": "15931",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/10/26 19:04",
"referee": "飯田　淳平"
},
{
"teams": [
"ガンバ大阪",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "東口　順昭,米倉　恒貴,丹羽　大輝,金　正也,オ　ジェソク,今野　泰幸,遠藤　保仁,倉田　秋,大森　晃太郎,宇佐美　貴史,パトリック",
"away_shoot": 7,
"home_director": "長谷川　健太",
"away_team": "ＦＣ東京",
"weather": "晴",
"series_number": 30,
"temperature": 19.8,
"away_score": 1,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,カニーニ,太田　宏介,高橋　秀人,米本　拓司,三田　啓貴,河野　広貴,渡邉　千真,武藤　嘉紀",
"home_score": 2,
"home_shoot": 16,
"game_id": "15932",
"home_team": "ガンバ大阪",
"game_start_at": "2014/10/26 19:04",
"referee": "家本　政明"
},
{
"teams": [
"徳島ヴォルティス",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "長谷川　徹,村松　大輔,福元　洋平,橋内　優也,アレックス,エステバン,濱田　武,佐々木　一輝,衛藤　裕,アドリアーノ,高崎　寛之",
"away_shoot": 10,
"home_director": "小林　伸二",
"away_team": "名古屋グランパス",
"weather": "晴",
"series_number": 30,
"temperature": 21.9,
"away_score": 2,
"away_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,田鍋　陵太,ダニルソン,田口　泰士,矢田　旭,松田　力,川又　堅碁",
"home_score": 0,
"home_shoot": 4,
"game_id": "15934",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/10/26 19:04",
"referee": "扇谷　健司"
},
{
"teams": [
"横浜Ｆ・マリノス",
"セレッソ大阪"
],
"away_director": "大熊　裕司",
"home_start_member": "榎本　哲也,小林　祐三,中澤　佑二,ファビオ,下平　匠,兵藤　慎剛,佐藤　優平,藤本　淳吾,中村　俊輔,齋藤　学,伊藤　翔",
"away_shoot": 6,
"home_director": "樋口　靖洋",
"away_team": "セレッソ大阪",
"weather": "晴",
"series_number": 30,
"temperature": 21.2,
"away_score": 0,
"away_start_member": "キム　ジンヒョン,藤本　康太,丸橋　祐介,酒本　憲幸,山下　達也,扇原　貴宏,長谷川　アーリアジャスール,南野　拓実,キム　ソンジュン,杉本　健勇,カカウ",
"home_score": 0,
"home_shoot": 11,
"game_id": "15936",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/10/26 19:04",
"referee": "吉田　寿光"
},
{
"teams": [
"ヴァンフォーレ甲府",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "荻　晃太,松橋　優,山本　英臣,佐々木　翔,ジウシーニョ,新井　涼平,マルキーニョス　パラナ,阿部　翔平,石原　克哉,阿部　拓馬,盛田　剛平",
"away_shoot": 10,
"home_director": "城福　浩",
"away_team": "川崎フロンターレ",
"weather": "曇",
"series_number": 30,
"temperature": 18.3,
"away_score": 1,
"away_start_member": "杉山　力裕,田中　裕介,實藤　友紀,谷口　彰悟,登里　享平,山本　真希,大島　僚太,森谷　賢太郎,レナト,小林　悠,大久保　嘉人",
"home_score": 2,
"home_shoot": 7,
"game_id": "15937",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/10/26 19:04",
"referee": "村上　伸次"
},
{
"teams": [
"清水エスパルス",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "櫛引　政敏,ヤコヴィッチ,平岡　康裕,吉田　豊,河井　陽介,藤田　息吹,本田　拓也,六平　光成,石毛　秀樹,大前　元紀,ノヴァコヴィッチ",
"away_shoot": 17,
"home_director": "大榎　克己",
"away_team": "サンフレッチェ広島",
"weather": "雨時々曇",
"series_number": 30,
"temperature": 18.9,
"away_score": 3,
"away_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,柏　好文,青山　敏弘,柴﨑　晃誠,山岸　智,石原　直樹,野津田　岳人,佐藤　寿人",
"home_score": 1,
"home_shoot": 14,
"game_id": "15938",
"home_team": "清水エスパルス",
"game_start_at": "2014/10/26 19:04",
"referee": "高山　啓義"
},
{
"teams": [
"水戸ホーリーホック",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "笠原　昂史,新里　亮,金　聖基,尾本　敬,内田　航平,中里　崇宏,船谷　圭祐,田中　雄大,吉田　眞紀人,鈴木　雄斗,山村　佑樹",
"away_shoot": 11,
"home_director": "柱谷　哲二",
"away_team": "横浜ＦＣ",
"weather": "雨",
"series_number": 39,
"temperature": 17.8,
"away_score": 2,
"away_start_member": "南　雄太,市村　篤司,野上　結貴,ドウグラス,永田　拓也,松下　裕樹,安　英学,寺田　紳一,松下　年宏,小池　純輝,黒津　勝",
"home_score": 2,
"home_shoot": 9,
"game_id": "16393",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/11/01 13:03",
"referee": "前田　拓哉"
},
{
"teams": [
"東京ヴェルディ",
"コンサドーレ札幌"
],
"away_director": "バルバリッチ",
"home_start_member": "佐藤　優也,安西　幸輝,金　鐘必,井林　章,安在　和樹,田村　直也,中後　雅喜,ニウド,澤井　直人,常盤　聡,平本　一樹",
"away_shoot": 9,
"home_director": "冨樫　剛一",
"away_team": "コンサドーレ札幌",
"weather": "雨",
"series_number": 39,
"temperature": 15.9,
"away_score": 0,
"away_start_member": "李　昊乗,パウロン,奈良　竜樹,櫛引　一紀,荒野　拓馬,宮澤　裕樹,上里　一将,石井　謙伍,前田　俊介,中原　彰吾,都倉　賢",
"home_score": 0,
"home_shoot": 14,
"game_id": "16395",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/11/01 13:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"カマタマーレ讃岐",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "瀬口　拓弥,武田　有祐,岡村　和哉,藤井　航大,小澤　雄希,沼田　圭悟,山本　翔平,高木　和正,アンドレア,高橋　泰,古田　寛幸",
"away_shoot": 7,
"home_director": "北野　誠",
"away_team": "ギラヴァンツ北九州",
"weather": "曇時々晴",
"series_number": 39,
"temperature": 22.9,
"away_score": 1,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,八角　剛史,風間　宏希,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"home_score": 1,
"home_shoot": 15,
"game_id": "16400",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/11/01 13:03",
"referee": "窪田　陽輔"
},
{
"teams": [
"ファジアーノ岡山",
"京都サンガF.C."
],
"away_director": "川勝　良一",
"home_start_member": "中林　洋次,久木田　紳吾,竹田　忠嗣,後藤　圭太,澤口　雅彦,千明　聖典,上田　康太,田所　諒,関戸　健二,押谷　祐樹,清水　慎太郎",
"away_shoot": 12,
"home_director": "影山　雅永",
"away_team": "京都サンガF.C.",
"weather": "曇",
"series_number": 39,
"temperature": 19.5,
"away_score": 3,
"away_start_member": "オ　スンフン,石櫃　洋祐,内野　貴志,バヤリッツァ,福村　貴幸,田中　英雄,駒井　善成,山瀬　功治,工藤　浩平,ドウグラス,大黒　将志",
"home_score": 2,
"home_shoot": 10,
"game_id": "16399",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/11/01 13:04",
"referee": "吉田　寿光"
},
{
"teams": [
"カターレ富山",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "飯田　健巳,高　准翼,秋本　倫孝,パク　テホン,大西　容平,前　貴之,井澤　惇,白崎　凌兵,内田　健太,宮吉　拓実,苔口　卓也",
"away_shoot": 14,
"home_director": "安間　貴義",
"away_team": "栃木ＳＣ",
"weather": "曇",
"series_number": 39,
"temperature": 22.1,
"away_score": 0,
"away_start_member": "鈴木　智幸,山形　辰徳,岡根　直哉,中野　洋司,荒堀　謙次,西澤　代志也,本間　勲,中美　慶哉,廣瀬　浩二,近藤　祐介,大久保　哲哉",
"home_score": 1,
"home_shoot": 14,
"game_id": "16397",
"home_team": "カターレ富山",
"game_start_at": "2014/11/01 14:04",
"referee": "森川　浩次"
},
{
"teams": [
"ＦＣ岐阜",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "川口　能活,益山　司,ヘニキ,阿部　正紀,森　勇介,水野　泰輔,宮沢　正史,比嘉　諒人,髙地　系治,遠藤　純輝,ナザリト",
"away_shoot": 8,
"home_director": "ラモス　瑠偉",
"away_team": "大分トリニータ",
"weather": "雨",
"series_number": 39,
"temperature": 17.3,
"away_score": 3,
"away_start_member": "武田　洋平,土岐田　洸平,高木　和道,ダニエル,松本　怜,末吉　隼也,キム　ジョンヒョン,西　弘則,為田　大貴,風間　宏矢,林　容平",
"home_score": 2,
"home_shoot": 6,
"game_id": "16398",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/11/01 14:05",
"referee": "吉田　哲朗"
},
{
"teams": [
"愛媛ＦＣ",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "児玉　剛,ハン　ヒフン,村上　佑介,林堂　眞,浦田　延尚,三原　向平,吉村　圭司,原川　力,堀米　勇輝,西田　剛,河原　和寿",
"away_shoot": 14,
"home_director": "石丸　清隆",
"away_team": "Ｖ・ファーレン長崎",
"weather": "雨",
"series_number": 39,
"temperature": 19.3,
"away_score": 3,
"away_start_member": "植草　裕樹,岡本　拓也,髙杉　亮太,古部　健太,神崎　大輔,黒木　聖仁,三原　雅俊,石神　直哉,奥埜　博亮,東　浩史,イ　ヨンジェ",
"home_score": 0,
"home_shoot": 5,
"game_id": "16401",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/11/01 15:04",
"referee": "野田　祐樹"
},
{
"teams": [
"ジェフユナイテッド千葉",
"ジュビロ磐田"
],
"away_director": "名波　浩",
"home_start_member": "高木　駿,山口　慶,キム　ヒョヌン,山口　智,中村　太亮,佐藤　勇人,兵働　昭弘,幸野　志有人,町田　也真人,谷澤　達也,森本　貴幸",
"away_shoot": 14,
"home_director": "関塚　隆",
"away_team": "ジュビロ磐田",
"weather": "雨",
"series_number": 39,
"temperature": 17.2,
"away_score": 2,
"away_start_member": "八田　直樹,小川　大貴,伊野波　雅彦,森下　俊,駒野　友一,藤田　義明,宮崎　智彦,松浦　拓弥,小林　祐希,松井　大輔,前田　遼一",
"home_score": 2,
"home_shoot": 15,
"game_id": "16394",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/11/01 19:03",
"referee": "岡部　拓人"
},
{
"teams": [
"ロアッソ熊本",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "畑　実,篠原　弘次郎,園田　拓也,橋本　拳人,キム　ビョンヨン,中山　雄登,養父　雄仁,髙柳　一誠,嶋田　慎太郎,澤田　崇,齊藤　和樹",
"away_shoot": 14,
"home_director": "小野　剛",
"away_team": "モンテディオ山形",
"weather": "曇",
"series_number": 39,
"temperature": 20.2,
"away_score": 3,
"away_start_member": "山岸　範宏,山田　拓巳,イ　ジュヨン,石井　秀典,當間　建文,松岡　亮輔,宮阪　政樹,伊東　俊,山﨑　雅人,ディエゴ,川西　翔太",
"home_score": 1,
"home_shoot": 13,
"game_id": "16403",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/11/01 19:03",
"referee": "塚田　健太"
},
{
"teams": [
"湘南ベルマーレ",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,宇佐美　宏和,熊谷　アンドリュー,永木　亮太,菊池　大介,大竹　洋平,ウェリントン,武富　孝介",
"away_shoot": 9,
"home_director": "曺　貴裁",
"away_team": "ザスパクサツ群馬",
"weather": "雨",
"series_number": 39,
"temperature": 17.5,
"away_score": 0,
"away_start_member": "富居　大樹,久富　良輔,有薗　真吾,クォン　ハンジン,小柳　達司,小林　竜樹,永田　亮太,黄　誠秀,宮崎　泰右,平繁　龍一,ダニエル　ロビーニョ",
"home_score": 1,
"home_shoot": 18,
"game_id": "16396",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/11/01 19:04",
"referee": "小屋　幸栄"
},
{
"teams": [
"アビスパ福岡",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "神山　竜一,阿部　巧,パク　ゴン,イ　グァンソン,古賀　正紘,堤　俊輔,中原　秀人,酒井　宣福,金森　健志,城後　寿,平井　将生",
"away_shoot": 11,
"home_director": "マリヤン　プシュニク",
"away_team": "松本山雅ＦＣ",
"weather": "雨",
"series_number": 39,
"temperature": 19.4,
"away_score": 2,
"away_start_member": "村山　智彦,田中　隼磨,大久保　裕樹,飯田　真輝,犬飼　智也,岩沼　俊介,岩間　雄大,岩上　祐三,喜山　康平,船山　貴之,山本　大貴",
"home_score": 1,
"home_shoot": 9,
"game_id": "16402",
"home_team": "アビスパ福岡",
"game_start_at": "2014/11/01 19:04",
"referee": "飯田　淳平"
},
{
"teams": [
"ガンバ大阪",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "東口　順昭,米倉　恒貴,丹羽　大輝,岩下　敬輔,オ　ジェソク,今野　泰幸,遠藤　保仁,阿部　浩之,大森　晃太郎,宇佐美　貴史,パトリック",
"away_shoot": 9,
"home_director": "長谷川　健太",
"away_team": "ベガルタ仙台",
"weather": "曇一時雨",
"series_number": 31,
"temperature": 21.3,
"away_score": 1,
"away_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,梁　勇基,野沢　拓也,赤嶺　真吾,武藤　雄樹",
"home_score": 1,
"home_shoot": 10,
"game_id": "15942",
"home_team": "ガンバ大阪",
"game_start_at": "2014/11/02 13:03",
"referee": "高山　啓義"
},
{
"teams": [
"名古屋グランパス",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,田鍋　陵太,磯村　亮太,矢田　旭,永井　謙佑,松田　力,川又　堅碁",
"away_shoot": 10,
"home_director": "西野　朗",
"away_team": "ＦＣ東京",
"weather": "曇",
"series_number": 31,
"temperature": 20.3,
"away_score": 2,
"away_start_member": "塩田　仁史,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,渡邉　千真,エドゥー,武藤　嘉紀",
"home_score": 2,
"home_shoot": 17,
"game_id": "15941",
"home_team": "名古屋グランパス",
"game_start_at": "2014/11/02 13:04",
"referee": "今村　義朗"
},
{
"teams": [
"セレッソ大阪",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "キム　ジンヒョン,藤本　康太,丸橋　祐介,酒本　憲幸,山下　達也,扇原　貴宏,長谷川　アーリアジャスール,キム　ソンジュン,南野　拓実,杉本　健勇,カカウ",
"away_shoot": 10,
"home_director": "大熊　裕司",
"away_team": "ヴァンフォーレ甲府",
"weather": "雨のち曇",
"series_number": 31,
"temperature": 21.3,
"away_score": 3,
"away_start_member": "荻　晃太,畑尾　大翔,山本　英臣,佐々木　翔,松橋　優,新井　涼平,マルキーニョス　パラナ,阿部　翔平,石原　克哉,阿部　拓馬,盛田　剛平",
"home_score": 1,
"home_shoot": 6,
"game_id": "15945",
"home_team": "セレッソ大阪",
"game_start_at": "2014/11/02 13:05",
"referee": "家本　政明"
},
{
"teams": [
"柏レイソル",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "桐畑　和繁,高山　薫,中谷　進之介,増嶋　竜也,橋本　和,太田　徹郎,栗澤　僚一,大谷　秀和,秋野　央樹,レアンドロ,ドゥドゥ",
"away_shoot": 6,
"home_director": "ネルシーニョ",
"away_team": "徳島ヴォルティス",
"weather": "曇",
"series_number": 31,
"temperature": 20.9,
"away_score": 0,
"away_start_member": "長谷川　徹,村松　大輔,藤原　広太朗,橋内　優也,アレックス,エステバン,濱田　武,佐々木　一輝,宮崎　光平,アドリアーノ,高崎　寛之",
"home_score": 2,
"home_shoot": 17,
"game_id": "15939",
"home_team": "柏レイソル",
"game_start_at": "2014/11/02 16:03",
"referee": "上田　益也"
},
{
"teams": [
"アルビレックス新潟",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "守田　達弥,松原　健,舞行龍ジェームズ,大井　健太郎,小泉　慶,レオ　シルバ,小林　裕紀,田中　亜土夢,山本　康裕,指宿　洋史,鈴木　武蔵",
"away_shoot": 12,
"home_director": "柳下　正明",
"away_team": "鹿島アントラーズ",
"weather": "雨",
"series_number": 31,
"temperature": 18.9,
"away_score": 2,
"away_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,前野　貴徳,柴崎　岳,小笠原　満男,遠藤　康,豊川　雄太,土居　聖真,赤﨑　秀平",
"home_score": 1,
"home_shoot": 11,
"game_id": "15940",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/11/02 16:04",
"referee": "東城　穣"
},
{
"teams": [
"川崎フロンターレ",
"清水エスパルス"
],
"away_director": "大榎　克己",
"home_start_member": "杉山　力裕,小宮山　尊信,井川　祐輔,谷口　彰悟,福森　晃斗,山本　真希,大島　僚太,中村　憲剛,小林　悠,レナト,大久保　嘉人",
"away_shoot": 16,
"home_director": "風間　八宏",
"away_team": "清水エスパルス",
"weather": "曇",
"series_number": 31,
"temperature": 22.6,
"away_score": 3,
"away_start_member": "櫛引　政敏,河井　陽介,ヤコヴィッチ,平岡　康裕,吉田　豊,本田　拓也,六平　光成,竹内　涼,高木　俊幸,大前　元紀,ノヴァコヴィッチ",
"home_score": 2,
"home_shoot": 15,
"game_id": "15944",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/11/02 16:04",
"referee": "扇谷　健司"
},
{
"teams": [
"サンフレッチェ広島",
"大宮アルディージャ"
],
"away_director": "渋谷　洋樹",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,柏　好文,青山　敏弘,柴﨑　晃誠,山岸　智,石原　直樹,髙萩　洋次郎,佐藤　寿人",
"away_shoot": 3,
"home_director": "森保　一",
"away_team": "大宮アルディージャ",
"weather": "曇",
"series_number": 31,
"temperature": 18.3,
"away_score": 1,
"away_start_member": "北野　貴之,今井　智基,菊地　光将,高橋　祥平,和田　拓也,横山　知伸,増田　誓志,渡邉　大剛,橋本　晃司,家長　昭博,ズラタン",
"home_score": 1,
"home_shoot": 14,
"game_id": "15947",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/11/02 16:04",
"referee": "山本　雄大"
},
{
"teams": [
"サガン鳥栖",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,高橋　義希,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 7,
"home_director": "吉田　恵",
"away_team": "ヴィッセル神戸",
"weather": "晴",
"series_number": 31,
"temperature": 15.8,
"away_score": 1,
"away_start_member": "徳重　健太,奥井　諒,河本　裕之,増川　隆洋,相馬　崇人,チョン　ウヨン,橋本　英郎,森岡　亮太,小川　慶治朗,ペドロ　ジュニオール,マルキーニョス",
"home_score": 2,
"home_shoot": 15,
"game_id": "15943",
"home_team": "サガン鳥栖",
"game_start_at": "2014/11/02 19:04",
"referee": "榎本　一慶"
},
{
"teams": [
"横浜Ｆ・マリノス",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,兵藤　慎剛,ファビオ,佐藤　優平,中村　俊輔,齋藤　学,伊藤　翔",
"away_shoot": 8,
"home_director": "樋口　靖洋",
"away_team": "浦和レッズ",
"weather": "晴",
"series_number": 31,
"temperature": 17.9,
"away_score": 1,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,鈴木　啓太,宇賀神　友弥,柏木　陽介,梅崎　司,李　忠成",
"home_score": 0,
"home_shoot": 12,
"game_id": "15946",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/11/03 17:04",
"referee": "松尾　一"
},
{
"teams": [
"コンサドーレ札幌",
"カマタマーレ讃岐"
],
"away_director": "北野　誠",
"home_start_member": "李　昊乗,パウロン,奈良　竜樹,櫛引　一紀,日高　拓磨,宮澤　裕樹,上里　一将,石井　謙伍,前田　俊介,荒野　拓馬,都倉　賢",
"away_shoot": 12,
"home_director": "バルバリッチ",
"away_team": "カマタマーレ讃岐",
"weather": "屋内",
"series_number": 40,
"temperature": 21.2,
"away_score": 1,
"away_start_member": "瀬口　拓弥,武田　有祐,エブソン,藤井　航大,小澤　雄希,沼田　圭悟,山本　翔平,岡村　和哉,高木　和正,我那覇　和樹,アンドレア",
"home_score": 1,
"home_shoot": 14,
"game_id": "16404",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/11/09 13:03",
"referee": "木村　博之"
},
{
"teams": [
"栃木ＳＣ",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "榎本　達也,山形　辰徳,チャ　ヨンファン,岡根　直哉,荒堀　謙次,廣瀬　浩二,小野寺　達也,本間　勲,近藤　祐介,西川　優大,杉本　真",
"away_shoot": 8,
"home_director": "阪倉　裕二",
"away_team": "ＦＣ岐阜",
"weather": "雨",
"series_number": 40,
"temperature": 14,
"away_score": 0,
"away_start_member": "太田　岳志,益山　司,深谷　友基,木谷　公亮,野垣内　俊,ヘニキ,宮沢　正史,比嘉　諒人,髙地　系治,遠藤　純輝,ナザリト",
"home_score": 3,
"home_shoot": 12,
"game_id": "16406",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/11/09 13:03",
"referee": "井上　知大"
},
{
"teams": [
"横浜ＦＣ",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "南　雄太,西嶋　弘之,野上　結貴,ドウグラス,永田　拓也,寺田　紳一,松下　裕樹,内田　智也,松下　年宏,黒津　勝,小池　純輝",
"away_shoot": 6,
"home_director": "山口　素弘",
"away_team": "ファジアーノ岡山",
"weather": "晴のち曇",
"series_number": 40,
"temperature": 17.4,
"away_score": 2,
"away_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,近藤　徹志,澤口　雅彦,千明　聖典,上田　康太,田所　諒,妹尾　隆佑,押谷　祐樹,清水　慎太郎",
"home_score": 0,
"home_shoot": 17,
"game_id": "16408",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/11/09 13:03",
"referee": "東城　穣"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"東京ヴェルディ"
],
"away_director": "冨樫　剛一",
"home_start_member": "植草　裕樹,岡本　拓也,山口　貴弘,古部　健太,神崎　大輔,前田　悠佑,三原　雅俊,石神　直哉,奥埜　博亮,東　浩史,イ　ヨンジェ",
"away_shoot": 5,
"home_director": "高木　琢也",
"away_team": "東京ヴェルディ",
"weather": "曇",
"series_number": 40,
"temperature": 19.8,
"away_score": 0,
"away_start_member": "佐藤　優也,安西　幸輝,金　鐘必,井林　章,安在　和樹,ニウド,中後　雅喜,高木　大輔,澤井　直人,前田　直輝,平本　一樹",
"home_score": 0,
"home_shoot": 11,
"game_id": "16412",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/11/09 13:03",
"referee": "三上　正一郎"
},
{
"teams": [
"ザスパクサツ群馬",
"ジュビロ磐田"
],
"away_director": "名波　浩",
"home_start_member": "富居　大樹,久富　良輔,有薗　真吾,青木　良太,小柳　達司,小林　竜樹,金沢　浄,加藤　弘堅,黄　誠秀,大津　耀誠,ダニエル　ロビーニョ",
"away_shoot": 10,
"home_director": "秋葉　忠宏",
"away_team": "ジュビロ磐田",
"weather": "雨",
"series_number": 40,
"temperature": 13.8,
"away_score": 1,
"away_start_member": "八田　直樹,小川　大貴,伊野波　雅彦,森下　俊,駒野　友一,宮崎　智彦,藤田　義明,松浦　拓弥,小林　祐希,松井　大輔,前田　遼一",
"home_score": 1,
"home_shoot": 5,
"game_id": "16407",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/11/09 13:04",
"referee": "飯田　淳平"
},
{
"teams": [
"松本山雅ＦＣ",
"ジェフユナイテッド千葉"
],
"away_director": "関塚　隆",
"home_start_member": "村山　智彦,犬飼　智也,飯田　真輝,大久保　裕樹,岩沼　俊介,岩間　雄大,岩上　祐三,喜山　康平,飯尾　竜太朗,山本　大貴,船山　貴之",
"away_shoot": 18,
"home_director": "反町　康治",
"away_team": "ジェフユナイテッド千葉",
"weather": "曇",
"series_number": 40,
"temperature": 12.6,
"away_score": 1,
"away_start_member": "高木　駿,キム　ヒョヌン,山口　智,大岩　一貴,谷澤　達也,佐藤　勇人,佐藤　健太郎,中村　太亮,幸野　志有人,町田　也真人,森本　貴幸",
"home_score": 2,
"home_shoot": 13,
"game_id": "16409",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/11/09 13:04",
"referee": "扇谷　健司"
},
{
"teams": [
"京都サンガF.C.",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "オ　スンフン,石櫃　洋祐,酒井　隆介,バヤリッツァ,福村　貴幸,駒井　善成,田森　大己,伊藤　優汰,工藤　浩平,ドウグラス,大黒　将志",
"away_shoot": 2,
"home_director": "川勝　良一",
"away_team": "カターレ富山",
"weather": "曇のち雨",
"series_number": 40,
"temperature": 17.8,
"away_score": 1,
"away_start_member": "飯田　健巳,平出　涼,秋本　倫孝,パク　テホン,大西　容平,前　貴之,井澤　惇,白崎　凌兵,内田　健太,木本　敬介,苔口　卓也",
"home_score": 1,
"home_shoot": 19,
"game_id": "16410",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/11/09 13:04",
"referee": "河合　英治"
},
{
"teams": [
"ロアッソ熊本",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "金井　大樹,藏川　洋平,園田　拓也,橋本　拳人,片山　奨典,中山　雄登,養父　雄仁,髙柳　一誠,澤田　崇,嶋田　慎太郎,齊藤　和樹",
"away_shoot": 12,
"home_director": "小野　剛",
"away_team": "愛媛ＦＣ",
"weather": "曇",
"series_number": 40,
"temperature": 20.6,
"away_score": 1,
"away_start_member": "児玉　剛,ハン　ヒフン,村上　佑介,林堂　眞,浦田　延尚,三原　向平,吉村　圭司,原川　力,堀米　勇輝,西田　剛,河原　和寿",
"home_score": 3,
"home_shoot": 14,
"game_id": "16413",
"home_team": "ロアッソ熊本",
"game_start_at": "2014/11/09 14:03",
"referee": "福島　孝一郎"
},
{
"teams": [
"ギラヴァンツ北九州",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,下村　東美,風間　宏希,小手川　宏基,内藤　洋平,渡　大生,池元　友樹",
"away_shoot": 17,
"home_director": "柱谷　幸一",
"away_team": "湘南ベルマーレ",
"weather": "曇",
"series_number": 40,
"temperature": 17.5,
"away_score": 4,
"away_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,石川　俊輝,永木　亮太,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"home_score": 0,
"home_shoot": 5,
"game_id": "16411",
"home_team": "ギラヴァンツ北九州",
"game_start_at": "2014/11/09 16:03",
"referee": "池内　明彦"
},
{
"teams": [
"大分トリニータ",
"水戸ホーリーホック"
],
"away_director": "柱谷　哲二",
"home_start_member": "武田　洋平,土岐田　洸平,高木　和道,若狭　大志,松本　怜,ダニエル,キム　ジョンヒョン,末吉　隼也,為田　大貴,風間　宏矢,林　容平",
"away_shoot": 6,
"home_director": "田坂　和昭",
"away_team": "水戸ホーリーホック",
"weather": "曇",
"series_number": 40,
"temperature": 18.5,
"away_score": 3,
"away_start_member": "笠原　昂史,新里　亮,金　聖基,尾本　敬,田中　雄大,中里　崇宏,船谷　圭祐,内田　航平,小谷野　顕治,吉田　眞紀人,山村　佑樹",
"home_score": 2,
"home_shoot": 16,
"game_id": "16414",
"home_team": "大分トリニータ",
"game_start_at": "2014/11/09 16:03",
"referee": "野田　祐樹"
},
{
"teams": [
"モンテディオ山形",
"アビスパ福岡"
],
"away_director": "マリヤン　プシュニク",
"home_start_member": "山岸　範宏,山田　拓巳,イ　ジュヨン,石井　秀典,當間　建文,松岡　亮輔,宮阪　政樹,キム　ボムヨン,山﨑　雅人,ディエゴ,川西　翔太",
"away_shoot": 11,
"home_director": "石﨑　信弘",
"away_team": "アビスパ福岡",
"weather": "雨",
"series_number": 40,
"temperature": 10.5,
"away_score": 1,
"away_start_member": "神山　竜一,パク　ゴン,山口　和樹,オ　チャンヒョン,イ　グァンソン,堤　俊輔,中原　秀人,武田　英二郎,平井　将生,城後　寿,坂田　大輔",
"home_score": 2,
"home_shoot": 18,
"game_id": "16405",
"home_team": "モンテディオ山形",
"game_start_at": "2014/11/09 16:04",
"referee": "長谷　拓"
},
{
"teams": [
"東京ヴェルディ",
"ザスパクサツ群馬"
],
"away_director": "秋葉　忠宏",
"home_start_member": "佐藤　優也,畠中　槙之輔,井林　章,福井　諒司,中後　雅喜,ニウド,安西　幸輝,澤井　直人,前田　直輝,高木　大輔,平本　一樹",
"away_shoot": 13,
"home_director": "冨樫　剛一",
"away_team": "ザスパクサツ群馬",
"weather": "晴",
"series_number": 41,
"temperature": 16.1,
"away_score": 1,
"away_start_member": "富居　大樹,黄　誠秀,クォン　ハンジン,青木　良太,久富　良輔,金沢　浄,小林　竜樹,青木　孝太,夛田　凌輔,平繁　龍一,ダニエル　ロビーニョ",
"home_score": 1,
"home_shoot": 17,
"game_id": "16417",
"home_team": "東京ヴェルディ",
"game_start_at": "2014/11/15 13:03",
"referee": "吉田　哲朗"
},
{
"teams": [
"カマタマーレ讃岐",
"大分トリニータ"
],
"away_director": "田坂　和昭",
"home_start_member": "瀬口　拓弥,武田　有祐,エブソン,藤井　航大,小澤　雄希,沼田　圭悟,山本　翔平,岡村　和哉,高木　和正,高橋　泰,アンドレア",
"away_shoot": 15,
"home_director": "北野　誠",
"away_team": "大分トリニータ",
"weather": "晴",
"series_number": 41,
"temperature": 16.3,
"away_score": 1,
"away_start_member": "武田　洋平,土岐田　洸平,ダニエル,高木　和道,西　弘則,松本　怜,キム　ジョンヒョン,末吉　隼也,為田　大貴,風間　宏矢,林　容平",
"home_score": 0,
"home_shoot": 8,
"game_id": "16422",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/11/15 13:03",
"referee": "上田　益也"
},
{
"teams": [
"アビスパ福岡",
"コンサドーレ札幌"
],
"away_director": "バルバリッチ",
"home_start_member": "神山　竜一,武田　英二郎,パク　ゴン,イ　グァンソン,堤　俊輔,中原　秀人,オ　チャンヒョン,金森　健志,平井　将生,城後　寿,坂田　大輔",
"away_shoot": 11,
"home_director": "マリヤン　プシュニク",
"away_team": "コンサドーレ札幌",
"weather": "晴",
"series_number": 41,
"temperature": 14.5,
"away_score": 2,
"away_start_member": "李　昊乗,パウロン,奈良　竜樹,櫛引　一紀,日高　拓磨,宮澤　裕樹,上里　一将,荒野　拓馬,内村　圭宏,中原　彰吾,都倉　賢",
"home_score": 2,
"home_shoot": 17,
"game_id": "16424",
"home_team": "アビスパ福岡",
"game_start_at": "2014/11/15 14:03",
"referee": "榎本　一慶"
},
{
"teams": [
"水戸ホーリーホック",
"栃木ＳＣ"
],
"away_director": "阪倉　裕二",
"home_start_member": "本間　幸司,新里　亮,金　聖基,細川　淳矢,中里　崇宏,船谷　圭祐,内田　航平,田中　雄大,吉田　眞紀人,馬場　賢治,小谷野　顕治",
"away_shoot": 9,
"home_director": "柱谷　哲二",
"away_team": "栃木ＳＣ",
"weather": "晴",
"series_number": 41,
"temperature": 15.7,
"away_score": 2,
"away_start_member": "榎本　達也,山形　辰徳,岡根　直哉,チャ　ヨンファン,荒堀　謙次,廣瀬　浩二,小野寺　達也,本間　勲,近藤　祐介,杉本　真,西川　優大",
"home_score": 1,
"home_shoot": 9,
"game_id": "16415",
"home_team": "水戸ホーリーホック",
"game_start_at": "2014/11/15 14:04",
"referee": "塚田　健太"
},
{
"teams": [
"ファジアーノ岡山",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,近藤　徹志,澤口　雅彦,千明　聖典,上田　康太,三村　真,妹尾　隆佑,押谷　祐樹,清水　慎太郎",
"away_shoot": 12,
"home_director": "影山　雅永",
"away_team": "ロアッソ熊本",
"weather": "晴",
"series_number": 41,
"temperature": 15.8,
"away_score": 1,
"away_start_member": "金井　大樹,園田　拓也,篠原　弘次郎,橋本　拳人,片山　奨典,嶋田　慎太郎,養父　雄仁,髙柳　一誠,仲間　隼斗,アンデルソン,齊藤　和樹",
"home_score": 1,
"home_shoot": 13,
"game_id": "16421",
"home_team": "ファジアーノ岡山",
"game_start_at": "2014/11/15 14:04",
"referee": "西村　雄一"
},
{
"teams": [
"Ｖ・ファーレン長崎",
"京都サンガF.C."
],
"away_director": "川勝　良一",
"home_start_member": "植草　裕樹,山口　貴弘,髙杉　亮太,武内　大,古部　健太,井上　裕大,三原　雅俊,奥埜　博亮,石神　直哉,小松　塁,佐藤　洸一",
"away_shoot": 5,
"home_director": "高木　琢也",
"away_team": "京都サンガF.C.",
"weather": "晴",
"series_number": 41,
"temperature": 15,
"away_score": 1,
"away_start_member": "杉本　大地,石櫃　洋祐,バヤリッツァ,酒井　隆介,福村　貴幸,田森　大己,駒井　善成,伊藤　優汰,工藤　浩平,ドウグラス,大黒　将志",
"home_score": 0,
"home_shoot": 7,
"game_id": "16425",
"home_team": "Ｖ・ファーレン長崎",
"game_start_at": "2014/11/15 14:04",
"referee": "岡部　拓人"
},
{
"teams": [
"ジュビロ磐田",
"モンテディオ山形"
],
"away_director": "石﨑　信弘",
"home_start_member": "八田　直樹,小川　大貴,伊野波　雅彦,森下　俊,駒野　友一,フェルジナンド,宮崎　智彦,松浦　拓弥,小林　祐希,松井　大輔,前田　遼一",
"away_shoot": 4,
"home_director": "名波　浩",
"away_team": "モンテディオ山形",
"weather": "晴",
"series_number": 41,
"temperature": 14.6,
"away_score": 2,
"away_start_member": "山岸　範宏,山田　拓巳,石川　竜也,石井　秀典,當間　建文,松岡　亮輔,宮阪　政樹,キム　ボムヨン,山﨑　雅人,ディエゴ,川西　翔太",
"home_score": 0,
"home_shoot": 10,
"game_id": "16419",
"home_team": "ジュビロ磐田",
"game_start_at": "2014/11/15 14:05",
"referee": "吉田　寿光"
},
{
"teams": [
"ＦＣ岐阜",
"松本山雅ＦＣ"
],
"away_director": "反町　康治",
"home_start_member": "川口　能活,木谷　公亮,深谷　友基,関田　寛士,ヘニキ,水野　泰輔,益山　司,髙地　系治,三都主　アレサンドロ,難波　宏明,ナザリト",
"away_shoot": 8,
"home_director": "ラモス　瑠偉",
"away_team": "松本山雅ＦＣ",
"weather": "晴",
"series_number": 41,
"temperature": 13,
"away_score": 1,
"away_start_member": "村山　智彦,鐡戸　裕史,飯田　真輝,大久保　裕樹,犬飼　智也,ユン　ソンヨル,岩上　祐三,椎名　伸志,喜山　康平,山本　大貴,船山　貴之",
"home_score": 3,
"home_shoot": 9,
"game_id": "16420",
"home_team": "ＦＣ岐阜",
"game_start_at": "2014/11/15 14:05",
"referee": "東城　穣"
},
{
"teams": [
"ジェフユナイテッド千葉",
"カターレ富山"
],
"away_director": "安間　貴義",
"home_start_member": "高木　駿,山口　慶,キム　ヒョヌン,山口　智,中村　太亮,兵働　昭弘,佐藤　健太郎,井出　遥也,町田　也真人,谷澤　達也,森本　貴幸",
"away_shoot": 8,
"home_director": "関塚　隆",
"away_team": "カターレ富山",
"weather": "晴",
"series_number": 41,
"temperature": 15.4,
"away_score": 1,
"away_start_member": "飯田　健巳,平出　涼,秋本　倫孝,パク　テホン,大西　容平,前　貴之,森　泰次郎,白崎　凌兵,内田　健太,キム　ヨングン,宮吉　拓実",
"home_score": 2,
"home_shoot": 16,
"game_id": "16416",
"home_team": "ジェフユナイテッド千葉",
"game_start_at": "2014/11/15 16:03",
"referee": "小屋　幸栄"
},
{
"teams": [
"湘南ベルマーレ",
"横浜ＦＣ"
],
"away_director": "山口　素弘",
"home_start_member": "秋元　陽太,遠藤　航,丸山　祐市,三竿　雄斗,藤田　征也,石川　俊輝,永木　亮太,菊池　大介,岡田　翔平,ウェリントン,武富　孝介",
"away_shoot": 5,
"home_director": "曺　貴裁",
"away_team": "横浜ＦＣ",
"weather": "晴",
"series_number": 41,
"temperature": 12.6,
"away_score": 1,
"away_start_member": "南　雄太,西嶋　弘之,野上　結貴,ドウグラス,永田　拓也,松下　裕樹,寺田　紳一,松下　年宏,小池　純輝,黒津　勝,小野瀬　康介",
"home_score": 4,
"home_shoot": 15,
"game_id": "16418",
"home_team": "湘南ベルマーレ",
"game_start_at": "2014/11/15 16:04",
"referee": "河合　英治"
},
{
"teams": [
"愛媛ＦＣ",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "児玉　剛,村上　佑介,林堂　眞,西岡　大輝,三原　向平,渡邊　一仁,吉村　圭司,藤　直也,堀米　勇輝,西田　剛,河原　和寿",
"away_shoot": 8,
"home_director": "石丸　清隆",
"away_team": "ギラヴァンツ北九州",
"weather": "晴",
"series_number": 41,
"temperature": 8.8,
"away_score": 1,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,冨士　祐樹,下村　東美,八角　剛史,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"home_score": 2,
"home_shoot": 7,
"game_id": "16423",
"home_team": "愛媛ＦＣ",
"game_start_at": "2014/11/15 17:04",
"referee": "今村　義朗"
},
{
"teams": [
"鹿島アントラーズ",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "曽ヶ端　準,西　大伍,青木　剛,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,赤﨑　秀平",
"away_shoot": 12,
"home_director": "トニーニョ　セレーゾ",
"away_team": "川崎フロンターレ",
"weather": "晴",
"series_number": 32,
"temperature": 16.8,
"away_score": 1,
"away_start_member": "西部　洋平,武岡　優斗,實藤　友紀,谷口　彰悟,福森　晃斗,山本　真希,大島　僚太,レナト,登里　享平,森島　康仁,大久保　嘉人",
"home_score": 2,
"home_shoot": 17,
"game_id": "15949",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/11/22 14:04",
"referee": "木村　博之"
},
{
"teams": [
"浦和レッズ",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,青木　拓矢,宇賀神　友弥,柏木　陽介,梅崎　司,李　忠成",
"away_shoot": 12,
"home_director": "ペトロヴィッチ",
"away_team": "ガンバ大阪",
"weather": "晴",
"series_number": 32,
"temperature": 17.4,
"away_score": 2,
"away_start_member": "東口　順昭,米倉　恒貴,丹羽　大輝,岩下　敬輔,オ　ジェソク,今野　泰幸,遠藤　保仁,阿部　浩之,大森　晃太郎,宇佐美　貴史,パトリック",
"home_score": 0,
"home_shoot": 8,
"game_id": "15950",
"home_team": "浦和レッズ",
"game_start_at": "2014/11/22 14:04",
"referee": "吉田　寿光"
},
{
"teams": [
"ヴァンフォーレ甲府",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "荻　晃太,畑尾　大翔,山本　英臣,佐々木　翔,松橋　優,新井　涼平,マルキーニョス　パラナ,阿部　翔平,石原　克哉,阿部　拓馬,盛田　剛平",
"away_shoot": 7,
"home_director": "城福　浩",
"away_team": "サンフレッチェ広島",
"weather": "晴",
"series_number": 32,
"temperature": 19,
"away_score": 0,
"away_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,清水　航平,青山　敏弘,森﨑　和幸,柏　好文,石原　直樹,野津田　岳人,佐藤　寿人",
"home_score": 2,
"home_shoot": 7,
"game_id": "15953",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/11/22 14:04",
"referee": "扇谷　健司"
},
{
"teams": [
"ヴィッセル神戸",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "徳重　健太,高橋　峻希,河本　裕之,増川　隆洋,相馬　崇人,橋本　英郎,チョン　ウヨン,森岡　亮太,小川　慶治朗,ペドロ　ジュニオール,マルキーニョス",
"away_shoot": 10,
"home_director": "安達　亮",
"away_team": "横浜Ｆ・マリノス",
"weather": "晴",
"series_number": 32,
"temperature": 18.5,
"away_score": 2,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,下平　匠,兵藤　慎剛,ファビオ,佐藤　優平,藤本　淳吾,齋藤　学,伊藤　翔",
"home_score": 1,
"home_shoot": 12,
"game_id": "15955",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/11/22 14:04",
"referee": "池内　明彦"
},
{
"teams": [
"徳島ヴォルティス",
"サガン鳥栖"
],
"away_director": "吉田　恵",
"home_start_member": "長谷川　徹,村松　大輔,福元　洋平,橋内　優也,藤原　広太朗,アレックス,斉藤　大介,濱田　武,大﨑　淳矢,廣瀬　智靖,キム　ジョンミン",
"away_shoot": 12,
"home_director": "小林　伸二",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 32,
"temperature": 18.3,
"away_score": 1,
"away_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,岡本　知剛,藤田　直之,金　民友,池田　圭,豊田　陽平",
"home_score": 0,
"home_shoot": 6,
"game_id": "15956",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/11/22 14:04",
"referee": "廣瀬　格"
},
{
"teams": [
"ベガルタ仙台",
"セレッソ大阪"
],
"away_director": "大熊　裕司",
"home_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,上本　大海,石川　直樹,太田　吉彰,富田　晋伍,梁　勇基,野沢　拓也,赤嶺　真吾,ウイルソン",
"away_shoot": 14,
"home_director": "渡邉　晋",
"away_team": "セレッソ大阪",
"weather": "晴",
"series_number": 32,
"temperature": 11.1,
"away_score": 3,
"away_start_member": "キム　ジンヒョン,染谷　悠太,丸橋　祐介,酒本　憲幸,山下　達也,扇原　貴宏,長谷川　アーリアジャスール,楠神　順平,杉本　健勇,永井　龍,南野　拓実",
"home_score": 3,
"home_shoot": 14,
"game_id": "15948",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/11/22 17:04",
"referee": "村上　伸次"
},
{
"teams": [
"大宮アルディージャ",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "清水　慶記,今井　智基,片岡　洋介,高橋　祥平,渡部　大輔,カルリーニョス,金澤　慎,家長　昭博,橋本　晃司,ズラタン,ムルジャ",
"away_shoot": 11,
"home_director": "渋谷　洋樹",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 32,
"temperature": 13.1,
"away_score": 2,
"away_start_member": "桐畑　和繁,渡部　博文,中谷　進之介,鈴木　大輔,橋本　和,高山　薫,茨田　陽生,大谷　秀和,太田　徹郎,レアンドロ,ドゥドゥ",
"home_score": 1,
"home_shoot": 4,
"game_id": "15951",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/11/22 17:04",
"referee": "家本　政明"
},
{
"teams": [
"ＦＣ東京",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,羽生　直剛,河野　広貴,エドゥー,武藤　嘉紀",
"away_shoot": 17,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "アルビレックス新潟",
"weather": "晴",
"series_number": 32,
"temperature": 13.8,
"away_score": 3,
"away_start_member": "守田　達弥,小泉　慶,大井　健太郎,大野　和成,川口　尚紀,レオ　シルバ,小林　裕紀,田中　亜土夢,山本　康裕,田中　達也,指宿　洋史",
"home_score": 1,
"home_shoot": 10,
"game_id": "15952",
"home_team": "ＦＣ東京",
"game_start_at": "2014/11/22 17:04",
"referee": "飯田　淳平"
},
{
"teams": [
"清水エスパルス",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "櫛引　政敏,河井　陽介,ヤコヴィッチ,平岡　康裕,吉田　豊,本田　拓也,六平　光成,竹内　涼,大前　元紀,ノヴァコヴィッチ,高木　俊幸",
"away_shoot": 7,
"home_director": "大榎　克己",
"away_team": "名古屋グランパス",
"weather": "晴",
"series_number": 32,
"temperature": 13.1,
"away_score": 2,
"away_start_member": "楢﨑　正剛,磯村　亮太,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,田鍋　陵太,ダニルソン,田口　泰士,矢田　旭,川又　堅碁,永井　謙佑",
"home_score": 2,
"home_shoot": 9,
"game_id": "15954",
"home_team": "清水エスパルス",
"game_start_at": "2014/11/22 17:04",
"referee": "中村　太"
},
{
"teams": [
"コンサドーレ札幌",
"ジュビロ磐田"
],
"away_director": "名波　浩",
"home_start_member": "金山　隼樹,パウロン,奈良　竜樹,櫛引　一紀,日高　拓磨,宮澤　裕樹,上里　一将,中原　彰吾,荒野　拓馬,前田　俊介,都倉　賢",
"away_shoot": 17,
"home_director": "バルバリッチ",
"away_team": "ジュビロ磐田",
"weather": "屋内",
"series_number": 42,
"temperature": 22.6,
"away_score": 1,
"away_start_member": "八田　直樹,駒野　友一,伊野波　雅彦,森下　俊,岡田　隆,藤田　義明,宮崎　智彦,松井　大輔,小林　祐希,松浦　拓弥,前田　遼一",
"home_score": 1,
"home_shoot": 10,
"game_id": "16426",
"home_team": "コンサドーレ札幌",
"game_start_at": "2014/11/23 14:03",
"referee": "佐藤　隆治"
},
{
"teams": [
"栃木ＳＣ",
"Ｖ・ファーレン長崎"
],
"away_director": "高木　琢也",
"home_start_member": "榎本　達也,山形　辰徳,岡根　直哉,チャ　ヨンファン,中野　洋司,廣瀬　浩二,小野寺　達也,本間　勲,荒堀　謙次,杉本　真,西川　優大",
"away_shoot": 8,
"home_director": "阪倉　裕二",
"away_team": "Ｖ・ファーレン長崎",
"weather": "晴",
"series_number": 42,
"temperature": 16.6,
"away_score": 0,
"away_start_member": "植草　裕樹,岡本　拓也,髙杉　亮太,古部　健太,神崎　大輔,井上　裕大,三原　雅俊,石神　直哉,奥埜　博亮,小松　塁,佐藤　洸一",
"home_score": 1,
"home_shoot": 10,
"game_id": "16428",
"home_team": "栃木ＳＣ",
"game_start_at": "2014/11/23 14:03",
"referee": "岡　宏道"
},
{
"teams": [
"横浜ＦＣ",
"ギラヴァンツ北九州"
],
"away_director": "柱谷　幸一",
"home_start_member": "南　雄太,小池　純輝,野上　結貴,西嶋　弘之,中島　崇典,渡辺　匠,寺田　紳一,内田　智也,野崎　陽介,野村　直輝,黒津　勝",
"away_shoot": 10,
"home_director": "山口　素弘",
"away_team": "ギラヴァンツ北九州",
"weather": "晴",
"series_number": 42,
"temperature": 18.6,
"away_score": 0,
"away_start_member": "大谷　幸輝,星原　健太,渡邉　将基,前田　和哉,多田　高行,八角　剛史,新井　純平,小手川　宏基,内藤　洋平,原　一樹,池元　友樹",
"home_score": 1,
"home_shoot": 8,
"game_id": "16430",
"home_team": "横浜ＦＣ",
"game_start_at": "2014/11/23 14:03",
"referee": "井上　知大"
},
{
"teams": [
"松本山雅ＦＣ",
"水戸ホーリーホック"
],
"away_director": "73' 退席 水戸 河野　高宏 （ＧＫコーチ）",
"home_start_member": "野澤　洋輔,犬飼　智也,大久保　裕樹,飯田　真輝,飯尾　竜太朗,岩上　祐三,岩沼　俊介,喜山　康平,岩間　雄大,船山　貴之,山本　大貴",
"away_shoot": 6,
"home_director": "柱谷　哲二",
"away_team": "水戸ホーリーホック",
"weather": "晴",
"series_number": 42,
"temperature": 11.7,
"away_score": 0,
"away_start_member": "笠原　昂史,新里　亮,金　聖基,細川　淳矢,田中　雄大,西岡　謙太,船谷　圭祐,内田　航平,吉田　眞紀人,三島　康平,馬場　賢治",
"home_score": 3,
"home_shoot": 15,
"game_id": "16431",
"home_team": "松本山雅ＦＣ",
"game_start_at": "2014/11/23 14:03",
"referee": "榎本　一慶"
},
{
"teams": [
"カマタマーレ讃岐",
"ジェフユナイテッド千葉"
],
"away_director": "28' 怪我人搬送のため30分中断",
"home_start_member": "瀬口　拓弥,持留　新作,西野　泰正,藤井　航大,小澤　雄希,古田　寛幸,山本　翔平,高木　和正,岡村　和哉,木島　良輔,アンドレア",
"away_shoot": 8,
"home_director": "関塚　隆",
"away_team": "ジェフユナイテッド千葉",
"weather": "晴",
"series_number": 42,
"temperature": 23,
"away_score": 1,
"away_start_member": "高木　駿,山口　慶,キム　ヒョヌン,山口　智,中村　太亮,佐藤　勇人,佐藤　健太郎,幸野　志有人,町田　也真人,谷澤　達也,森本　貴幸",
"home_score": 0,
"home_shoot": 9,
"game_id": "16434",
"home_team": "カマタマーレ讃岐",
"game_start_at": "2014/11/23 14:03",
"referee": "高山　啓義"
},
{
"teams": [
"大分トリニータ",
"湘南ベルマーレ"
],
"away_director": "曺　貴裁",
"home_start_member": "武田　洋平,若狭　大志,ダニエル,高木　和道,西　弘則,松本　怜,土岐田　洸平,キム　ジョンヒョン,為田　大貴,風間　宏矢,林　容平",
"away_shoot": 15,
"home_director": "田坂　和昭",
"away_team": "湘南ベルマーレ",
"weather": "晴",
"series_number": 42,
"temperature": 18.8,
"away_score": 3,
"away_start_member": "秋元　陽太,島村　毅,丸山　祐市,亀川　諒史,宇佐美　宏和,石川　俊輝,永木　亮太,菊池　大介,大竹　洋平,ウェリントン,岡田　翔平",
"home_score": 2,
"home_shoot": 16,
"game_id": "16436",
"home_team": "大分トリニータ",
"game_start_at": "2014/11/23 14:03",
"referee": "西村　雄一"
},
{
"teams": [
"モンテディオ山形",
"東京ヴェルディ"
],
"away_director": "冨樫　剛一",
"home_start_member": "山岸　範宏,山田　拓巳,當間　建文,石井　秀典,石川　竜也,松岡　亮輔,宮阪　政樹,キム　ボムヨン,山﨑　雅人,ディエゴ,川西　翔太",
"away_shoot": 7,
"home_director": "石﨑　信弘",
"away_team": "東京ヴェルディ",
"weather": "晴",
"series_number": 42,
"temperature": 11.1,
"away_score": 2,
"away_start_member": "柴崎　貴広,安西　幸輝,井林　章,田村　直也,福井　諒司,中後　雅喜,澤井　直人,前田　直輝,南　秀仁,平本　一樹,菅嶋　弘希",
"home_score": 1,
"home_shoot": 16,
"game_id": "16427",
"home_team": "モンテディオ山形",
"game_start_at": "2014/11/23 14:04",
"referee": "窪田　陽輔"
},
{
"teams": [
"ザスパクサツ群馬",
"愛媛ＦＣ"
],
"away_director": "石丸　清隆",
"home_start_member": "富居　大樹,久富　良輔,クォン　ハンジン,小柳　達司,瀬川　和樹,宮崎　泰右,金沢　浄,黄　誠秀,小林　竜樹,平繁　龍一,ダニエル　ロビーニョ",
"away_shoot": 13,
"home_director": "秋葉　忠宏",
"away_team": "愛媛ＦＣ",
"weather": "晴",
"series_number": 42,
"temperature": 17.3,
"away_score": 2,
"away_start_member": "児玉　剛,ハン　ヒフン,代　健司,林堂　眞,西岡　大輝,三原　向平,渡邊　一仁,吉村　圭司,原川　力,堀米　勇輝,河原　和寿",
"home_score": 3,
"home_shoot": 16,
"game_id": "16429",
"home_team": "ザスパクサツ群馬",
"game_start_at": "2014/11/23 14:04",
"referee": "森川　浩次"
},
{
"teams": [
"カターレ富山",
"ファジアーノ岡山"
],
"away_director": "影山　雅永",
"home_start_member": "飯田　健巳,平出　涼,秋本　倫孝,パク　テホン,大西　容平,前　貴之,森　泰次郎,白崎　凌兵,内田　健太,キム　ヨングン,宮吉　拓実",
"away_shoot": 12,
"home_director": "安間　貴義",
"away_team": "ファジアーノ岡山",
"weather": "曇",
"series_number": 42,
"temperature": 13.3,
"away_score": 3,
"away_start_member": "中林　洋次,久木田　紳吾,後藤　圭太,近藤　徹志,田中　奏一,島田　譲,上田　康太,三村　真,片山　瑛一,押谷　祐樹,清水　慎太郎",
"home_score": 0,
"home_shoot": 8,
"game_id": "16432",
"home_team": "カターレ富山",
"game_start_at": "2014/11/23 14:04",
"referee": "長谷　拓"
},
{
"teams": [
"京都サンガF.C.",
"ＦＣ岐阜"
],
"away_director": "ラモス　瑠偉",
"home_start_member": "杉本　大地,石櫃　洋祐,酒井　隆介,バヤリッツァ,比嘉　祐介,駒井　善成,田森　大己,伊藤　優汰,工藤　浩平,ドウグラス,大黒　将志",
"away_shoot": 10,
"home_director": "川勝　良一",
"away_team": "ＦＣ岐阜",
"weather": "晴",
"series_number": 42,
"temperature": 17.4,
"away_score": 0,
"away_start_member": "川口　能活,益山　司,木谷　公亮,関田　寛士,森　勇介,ヘニキ,宮沢　正史,比嘉　諒人,髙地　系治,難波　宏明,ナザリト",
"home_score": 0,
"home_shoot": 9,
"game_id": "16433",
"home_team": "京都サンガF.C.",
"game_start_at": "2014/11/23 14:04",
"referee": "松尾　一"
},
{
"teams": [
"アビスパ福岡",
"ロアッソ熊本"
],
"away_director": "小野　剛",
"home_start_member": "神山　竜一,パク　ゴン,オ　チャンヒョン,イ　グァンソン,堤　俊輔,武田　英二郎,中原　秀人,金森　健志,坂田　大輔,城後　寿,平井　将生",
"away_shoot": 11,
"home_director": "マリヤン　プシュニク",
"away_team": "ロアッソ熊本",
"weather": "晴",
"series_number": 42,
"temperature": 19.5,
"away_score": 3,
"away_start_member": "金井　大樹,藏川　洋平,野田　裕喜,橋本　拳人,園田　拓也,嶋田　慎太郎,養父　雄仁,髙柳　一誠,澤田　崇,齊藤　和樹,アンデルソン",
"home_score": 1,
"home_shoot": 7,
"game_id": "16435",
"home_team": "アビスパ福岡",
"game_start_at": "2014/11/23 14:04",
"referee": "三上　正一郎"
},
{
"teams": [
"ガンバ大阪",
"ヴィッセル神戸"
],
"away_director": "安達　亮",
"home_start_member": "東口　順昭,オ　ジェソク,丹羽　大輝,岩下　敬輔,藤春　廣輝,今野　泰幸,遠藤　保仁,阿部　浩之,大森　晃太郎,宇佐美　貴史,パトリック",
"away_shoot": 7,
"home_director": "長谷川　健太",
"away_team": "ヴィッセル神戸",
"weather": "晴",
"series_number": 33,
"temperature": 19,
"away_score": 1,
"away_start_member": "徳重　健太,高橋　峻希,北本　久仁衛,増川　隆洋,相馬　崇人,チョン　ウヨン,大屋　翼,小川　慶治朗,森岡　亮太,マルキーニョス,田代　有三",
"home_score": 3,
"home_shoot": 12,
"game_id": "15963",
"home_team": "ガンバ大阪",
"game_start_at": "2014/11/29 14:03",
"referee": "山本　雄大"
},
{
"teams": [
"柏レイソル",
"清水エスパルス"
],
"away_director": "大榎　克己",
"home_start_member": "桐畑　和繁,キム　チャンス,鈴木　大輔,中谷　進之介,渡部　博文,太田　徹郎,栗澤　僚一,大谷　秀和,橋本　和,レアンドロ,ドゥドゥ",
"away_shoot": 14,
"home_director": "ネルシーニョ",
"away_team": "清水エスパルス",
"weather": "曇",
"series_number": 33,
"temperature": 13.4,
"away_score": 1,
"away_start_member": "櫛引　政敏,河井　陽介,三浦　弦太,平岡　康裕,吉田　豊,本田　拓也,六平　光成,大前　元紀,竹内　涼,高木　俊幸,ノヴァコヴィッチ",
"home_score": 3,
"home_shoot": 18,
"game_id": "15958",
"home_team": "柏レイソル",
"game_start_at": "2014/11/29 14:04",
"referee": "村上　伸次"
},
{
"teams": [
"川崎フロンターレ",
"サンフレッチェ広島"
],
"away_director": "森保　一",
"home_start_member": "西部　洋平,武岡　優斗,谷口　彰悟,車屋　紳太郎,小宮山　尊信,稲本　潤一,山本　真希,大島　僚太,森谷　賢太郎,レナト,大久保　嘉人",
"away_shoot": 18,
"home_director": "風間　八宏",
"away_team": "サンフレッチェ広島",
"weather": "雨のち曇",
"series_number": 33,
"temperature": 13.9,
"away_score": 1,
"away_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,清水　航平,青山　敏弘,森﨑　和幸,柏　好文,浅野　拓磨,野津田　岳人,皆川　佑介",
"home_score": 1,
"home_shoot": 11,
"game_id": "15959",
"home_team": "川崎フロンターレ",
"game_start_at": "2014/11/29 14:04",
"referee": "佐藤　隆治"
},
{
"teams": [
"セレッソ大阪",
"鹿島アントラーズ"
],
"away_director": "トニーニョ　セレーゾ",
"home_start_member": "キム　ジンヒョン,染谷　悠太,丸橋　祐介,酒本　憲幸,山下　達也,扇原　貴宏,長谷川　アーリアジャスール,楠神　順平,杉本　健勇,永井　龍,南野　拓実",
"away_shoot": 16,
"home_director": "大熊　裕司",
"away_team": "鹿島アントラーズ",
"weather": "曇",
"series_number": 33,
"temperature": 19.3,
"away_score": 4,
"away_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,カイオ,土居　聖真,赤﨑　秀平",
"home_score": 1,
"home_shoot": 11,
"game_id": "15964",
"home_team": "セレッソ大阪",
"game_start_at": "2014/11/29 14:04",
"referee": "松尾　一"
},
{
"teams": [
"サガン鳥栖",
"浦和レッズ"
],
"away_director": "ペトロヴィッチ",
"home_start_member": "林　彰洋,丹羽　竜平,菊地　直哉,キム　ミンヒョク,安田　理大,水沼　宏太,岡本　知剛,藤田　直之,金　民友,池田　圭,豊田　陽平",
"away_shoot": 10,
"home_director": "吉田　恵",
"away_team": "浦和レッズ",
"weather": "晴",
"series_number": 33,
"temperature": 23.9,
"away_score": 1,
"away_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,青木　拓矢,宇賀神　友弥,柏木　陽介,梅崎　司,李　忠成",
"home_score": 1,
"home_shoot": 8,
"game_id": "15965",
"home_team": "サガン鳥栖",
"game_start_at": "2014/11/29 14:04",
"referee": "扇谷　健司"
},
{
"teams": [
"ベガルタ仙台",
"徳島ヴォルティス"
],
"away_director": "小林　伸二",
"home_start_member": "関　憲太郎,菅井　直樹,鎌田　次郎,角田　誠,石川　直樹,太田　吉彰,富田　晋伍,梁　勇基,野沢　拓也,赤嶺　真吾,武藤　雄樹",
"away_shoot": 5,
"home_director": "渡邉　晋",
"away_team": "徳島ヴォルティス",
"weather": "雨のち曇",
"series_number": 33,
"temperature": 11.6,
"away_score": 1,
"away_start_member": "長谷川　徹,村松　大輔,福元　洋平,橋内　優也,藤原　広太朗,那須川　将大,斉藤　大介,濱田　武,大﨑　淳矢,廣瀬　智靖,キム　ジョンミン",
"home_score": 2,
"home_shoot": 14,
"game_id": "15957",
"home_team": "ベガルタ仙台",
"game_start_at": "2014/11/29 17:04",
"referee": "吉田　寿光"
},
{
"teams": [
"横浜Ｆ・マリノス",
"アルビレックス新潟"
],
"away_director": "柳下　正明",
"home_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,奈良輪　雄太,兵藤　慎剛,ファビオ,佐藤　優平,藤本　淳吾,齋藤　学,伊藤　翔",
"away_shoot": 18,
"home_director": "樋口　靖洋",
"away_team": "アルビレックス新潟",
"weather": "曇",
"series_number": 33,
"temperature": 13.8,
"away_score": 0,
"away_start_member": "守田　達弥,小泉　慶,大井　健太郎,大野　和成,川口　尚紀,レオ　シルバ,小林　裕紀,田中　亜土夢,山本　康裕,田中　達也,指宿　洋史",
"home_score": 1,
"home_shoot": 11,
"game_id": "15960",
"home_team": "横浜Ｆ・マリノス",
"game_start_at": "2014/11/29 17:04",
"referee": "今村　義朗"
},
{
"teams": [
"ヴァンフォーレ甲府",
"ＦＣ東京"
],
"away_director": "マッシモ　フィッカデンティ",
"home_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,水野　晃樹,マルキーニョス　パラナ,新井　涼平,阿部　翔平,石原　克哉,阿部　拓馬,盛田　剛平",
"away_shoot": 3,
"home_director": "城福　浩",
"away_team": "ＦＣ東京",
"weather": "晴",
"series_number": 33,
"temperature": 13.5,
"away_score": 0,
"away_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,梶山　陽平,米本　拓司,東　慶悟,河野　広貴,武藤　嘉紀,中島　翔哉",
"home_score": 0,
"home_shoot": 10,
"game_id": "15961",
"home_team": "ヴァンフォーレ甲府",
"game_start_at": "2014/11/29 17:04",
"referee": "西村　雄一"
},
{
"teams": [
"名古屋グランパス",
"大宮アルディージャ"
],
"away_director": "渋谷　洋樹",
"home_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,ダニルソン,田鍋　陵太,田口　泰士,矢田　旭,永井　謙佑,玉田　圭司,川又　堅碁",
"away_shoot": 8,
"home_director": "西野　朗",
"away_team": "大宮アルディージャ",
"weather": "屋内",
"series_number": 33,
"temperature": 17.6,
"away_score": 1,
"away_start_member": "清水　慶記,中村　北斗,横山　知伸,高橋　祥平,和田　拓也,金澤　慎,増田　誓志,家長　昭博,橋本　晃司,ムルジャ,ズラタン",
"home_score": 2,
"home_shoot": 8,
"game_id": "15962",
"home_team": "名古屋グランパス",
"game_start_at": "2014/11/29 17:04",
"referee": "岡部　拓人"
},
{
"teams": [
"鹿島アントラーズ",
"サガン鳥栖"
],
"away_director": "吉田　恵",
"home_start_member": "曽ヶ端　準,西　大伍,植田　直通,昌子　源,山本　脩斗,柴崎　岳,小笠原　満男,遠藤　康,豊川　雄太,土居　聖真,赤﨑　秀平",
"away_shoot": 10,
"home_director": "トニーニョ　セレーゾ",
"away_team": "サガン鳥栖",
"weather": "晴",
"series_number": 34,
"temperature": 6.3,
"away_score": 1,
"away_start_member": "林　彰洋,崔　誠根,小林　久晃,キム　ミンヒョク,安田　理大,水沼　宏太,高橋　義希,金井　貢史,金　民友,池田　圭,豊田　陽平",
"home_score": 0,
"home_shoot": 10,
"game_id": "15966",
"home_team": "鹿島アントラーズ",
"game_start_at": "2014/12/06 15:33",
"referee": "家本　政明"
},
{
"teams": [
"大宮アルディージャ",
"セレッソ大阪"
],
"away_director": "大熊　裕司",
"home_start_member": "清水　慶記,今井　智基,横山　知伸,高橋　祥平,中村　北斗,金澤　慎,和田　拓也,家長　昭博,橋本　晃司,ムルジャ,ズラタン",
"away_shoot": 11,
"home_director": "渋谷　洋樹",
"away_team": "セレッソ大阪",
"weather": "晴のち曇",
"series_number": 34,
"temperature": 7.1,
"away_score": 0,
"away_start_member": "キム　ジンヒョン,染谷　悠太,丸橋　祐介,安藤　淳,山下　達也,長谷川　アーリアジャスール,楠神　順平,杉本　健勇,キム　ソンジュン,永井　龍,南野　拓実",
"home_score": 2,
"home_shoot": 10,
"game_id": "15968",
"home_team": "大宮アルディージャ",
"game_start_at": "2014/12/06 15:33",
"referee": "飯田　淳平"
},
{
"teams": [
"浦和レッズ",
"名古屋グランパス"
],
"away_director": "西野　朗",
"home_start_member": "西川　周作,森脇　良太,那須　大亮,槙野　智章,平川　忠亮,阿部　勇樹,青木　拓矢,宇賀神　友弥,柏木　陽介,梅崎　司,李　忠成",
"away_shoot": 11,
"home_director": "ペトロヴィッチ",
"away_team": "名古屋グランパス",
"weather": "晴",
"series_number": 34,
"temperature": 8.2,
"away_score": 2,
"away_start_member": "楢﨑　正剛,矢野　貴章,牟田　雄祐,田中　マルクス闘莉王,本多　勇喜,小川　佳純,田口　泰士,ダニルソン,矢田　旭,川又　堅碁,永井　謙佑",
"home_score": 1,
"home_shoot": 13,
"game_id": "15967",
"home_team": "浦和レッズ",
"game_start_at": "2014/12/06 15:34",
"referee": "西村　雄一"
},
{
"teams": [
"ＦＣ東京",
"横浜Ｆ・マリノス"
],
"away_director": "樋口　靖洋",
"home_start_member": "権田　修一,徳永　悠平,森重　真人,吉本　一謙,太田　宏介,高橋　秀人,米本　拓司,東　慶悟,梶山　陽平,エドゥー,河野　広貴",
"away_shoot": 5,
"home_director": "マッシモ　フィッカデンティ",
"away_team": "横浜Ｆ・マリノス",
"weather": "晴",
"series_number": 34,
"temperature": 5.8,
"away_score": 1,
"away_start_member": "榎本　哲也,小林　祐三,栗原　勇蔵,中澤　佑二,奈良輪　雄太,兵藤　慎剛,富澤　清太郎,佐藤　優平,藤本　淳吾,齋藤　学,伊藤　翔",
"home_score": 1,
"home_shoot": 11,
"game_id": "15969",
"home_team": "ＦＣ東京",
"game_start_at": "2014/12/06 15:34",
"referee": "中村　太"
},
{
"teams": [
"清水エスパルス",
"ヴァンフォーレ甲府"
],
"away_director": "城福　浩",
"home_start_member": "櫛引　政敏,河井　陽介,ヤコヴィッチ,平岡　康裕,吉田　豊,本田　拓也,竹内　涼,大前　元紀,石毛　秀樹,ノヴァコヴィッチ,高木　俊幸",
"away_shoot": 9,
"home_director": "大榎　克己",
"away_team": "ヴァンフォーレ甲府",
"weather": "晴",
"series_number": 34,
"temperature": 7.8,
"away_score": 0,
"away_start_member": "荻　晃太,青山　直晃,山本　英臣,佐々木　翔,水野　晃樹,マルキーニョス　パラナ,新井　涼平,阿部　翔平,石原　克哉,阿部　拓馬,キリノ",
"home_score": 0,
"home_shoot": 5,
"game_id": "15971",
"home_team": "清水エスパルス",
"game_start_at": "2014/12/06 15:34",
"referee": "吉田　寿光"
},
{
"teams": [
"ヴィッセル神戸",
"川崎フロンターレ"
],
"away_director": "風間　八宏",
"home_start_member": "徳重　健太,高橋　峻希,岩波　拓也,増川　隆洋,相馬　崇人,大屋　翼,チョン　ウヨン,森岡　亮太,ペドロ　ジュニオール,小川　慶治朗,マルキーニョス",
"away_shoot": 17,
"home_director": "安達　亮",
"away_team": "川崎フロンターレ",
"weather": "晴",
"series_number": 34,
"temperature": 9,
"away_score": 2,
"away_start_member": "西部　洋平,武岡　優斗,谷口　彰悟,車屋　紳太郎,福森　晃斗,山本　真希,大島　僚太,森谷　賢太郎,登里　享平,レナト,大久保　嘉人",
"home_score": 1,
"home_shoot": 12,
"game_id": "15972",
"home_team": "ヴィッセル神戸",
"game_start_at": "2014/12/06 15:34",
"referee": "高山　啓義"
},
{
"teams": [
"徳島ヴォルティス",
"ガンバ大阪"
],
"away_director": "長谷川　健太",
"home_start_member": "長谷川　徹,那須川　将大,福元　洋平,橋内　優也,藤原　広太朗,エステバン,斉藤　大介,濱田　武,大﨑　淳矢,衛藤　裕,キム　ジョンミン",
"away_shoot": 11,
"home_director": "小林　伸二",
"away_team": "ガンバ大阪",
"weather": "晴",
"series_number": 34,
"temperature": 4.5,
"away_score": 0,
"away_start_member": "東口　順昭,米倉　恒貴,丹羽　大輝,岩下　敬輔,オ　ジェソク,今野　泰幸,遠藤　保仁,阿部　浩之,大森　晃太郎,宇佐美　貴史,パトリック",
"home_score": 0,
"home_shoot": 7,
"game_id": "15974",
"home_team": "徳島ヴォルティス",
"game_start_at": "2014/12/06 15:34",
"referee": "木村　博之"
},
{
"teams": [
"サンフレッチェ広島",
"ベガルタ仙台"
],
"away_director": "渡邉　晋",
"home_start_member": "林　卓人,塩谷　司,千葉　和彦,水本　裕貴,清水　航平,青山　敏弘,森﨑　和幸,柏　好文,森﨑　浩司,髙萩　洋次郎,石原　直樹",
"away_shoot": 9,
"home_director": "森保　一",
"away_team": "ベガルタ仙台",
"weather": "晴のち雪",
"series_number": 34,
"temperature": 1.3,
"away_score": 0,
"away_start_member": "関　憲太郎,蜂須賀　孝治,鎌田　次郎,上本　大海,村上　和弘,太田　吉彰,富田　晋伍,角田　誠,野沢　拓也,赤嶺　真吾,武藤　雄樹",
"home_score": 2,
"home_shoot": 15,
"game_id": "15973",
"home_team": "サンフレッチェ広島",
"game_start_at": "2014/12/06 15:35",
"referee": "東城　穣"
},
{
"teams": [
"アルビレックス新潟",
"柏レイソル"
],
"away_director": "ネルシーニョ",
"home_start_member": "守田　達弥,舞行龍ジェームズ,大井　健太郎,大野　和成,川口　尚紀,レオ　シルバ,小林　裕紀,田中　亜土夢,山本　康裕,指宿　洋史,鈴木　武蔵",
"away_shoot": 14,
"home_director": "柳下　正明",
"away_team": "柏レイソル",
"weather": "晴",
"series_number": 34,
"temperature": 7,
"away_score": 2,
"away_start_member": "桐畑　和繁,鈴木　大輔,中谷　進之介,渡部　博文,橋本　和,高山　薫,小林　祐介,大谷　秀和,太田　徹郎,レアンドロ,ドゥドゥ",
"home_score": 0,
"home_shoot": 12,
"game_id": "15970",
"home_team": "アルビレックス新潟",
"game_start_at": "2014/12/08 19:03",
"referee": "岡部　拓人"
}
]
'''