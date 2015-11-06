<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>{{title or 'Client Monitoring'}}</title>
    <style>
      html { background-color: #eee; }
      a { color: #4078c0; text-decoration: none; }
      a:hover { text-decoration: underline; }
      body { font: 13px/1.4 Arial, Verdana, sans-serif; background-color: #fff; border: 1px solid #ddd; margin: 45px auto; width: 90%; min-width: 980px }
      nav { background-color: #f5f5f5; border-bottom: 1px solid #e5e5e5; margin: 0; overflow: hidden; }
      nav ul { margin: 0; padding: 0; }
      nav ul li { display: inline-block; list-style-type: none; }
      nav>ul>li>a, nav>ul>li>a:visited { color: #333; font-weight: bold; display: block; line-height: 2em; padding: 0.5em 0 0.5em 1em; text-decoration: none; }
      nav>ul>li>a:hover, nav>ul>li > a:focus { color: #4078c0; text-decoration: none; }
      section.wrapper { margin: 0; }
      section.wrapper section.content { padding-right: 1em; padding-left: 1em; }
      section.content.empty { background-color: #fafafa; text-align: center; padding:70px 50px; border-top: 1px solid #e5e5e5; box-shadow: inset 0 0 10px rgba(0,0,0,0.05); }
      section.content.empty p { font-size: 16px; }
      h2 { font-size: 1.5em; display: inline-block; }
      h2 span { font-weight: normal; }
      table { table-layout: auto; font-size: 12px; line-height: 28px; border-collapse:collapse; width:100%; color: #888; }
      th { padding: 0 .5em; text-align: left }
      td { padding: 6px 10px; line-height: 20px; }
      thead tr { border-top: 1px solid #c1dce8; border-bottom: 1px solid #c1dce8; background:#e6f1f6; color: #333; }
      thead tr th { padding: 10px; }
      thead tr th:last-child { text-align: right; }
      tbody tr { border-top: 1px solid #eee; }
      tbody tr:first { border-top: none; }
      thead th.id, td.id { max-width: 70px; }
      thead th.cpu, td.cpu { text-align: right }
      tbody tr.warning { background-color: #ffecec; }
      tbody tr.critical { background-color: #ffdddd; }
      tbody tr td:last-child { text-align: right; }
      td+td {  text-align: left }
      .content .btn.logs { float: right; margin-top: 12px; }
      .btn { font-family: inherit; font-size: 100%; font-weight: bold; padding: .5em 1em; color: rgba(0,0,0,.8); border: 1px solid #ccc; background-color: #E6E6E6; text-decoration: none; border-radius: 2px; }
      .btn { display: inline-block; zoom: 1; line-height: normal; white-space: nowrap; vertical-align: middle; text-align: center; cursor: pointer; -webkit-user-drag: none; -webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none; -webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; }
      .btn:hover { text-decoration: none; }
      .btn:active { border-color: #999; }
  </style>
  </head>
  <body>
    <nav>
      <ul>
        <li><a href="/clients">Clients</a></li>
        <li><a href="/logs">Logs</a></li>
      </ul>
    </nav>
    <section class="wrapper">
      {{!base}}
    </section>
  </body>
</html>
