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
