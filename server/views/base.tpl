<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>{{title or 'No title'}}</title>
    <style>
      html { background-color: #eee; }
      a, a:visited { color: #4078c0; text-decoration: none; }
      a:hover { text-decoration: underline; }
      body { font: 13px/1.4 Arial, Verdana, sans-serif; background-color: #fff; border: 1px solid #ddd; margin: 45px; min-width: 980px; }
      nav { background-color: #f5f5f5; border-bottom: 1px soild #e5e5e5; margin: 0; overflow: hidden; }
      nav ul{ margin: 0; padding: 0; }
      nav ul li { display: inline-block; list-style-type: none; }
      nav>ul>li>a, nav>ul>li>a:visited { color: #333; font-weight: bold; display: block; line-height: 2em; padding: 0.5em 1em; text-decoration: none; }
      nav>ul>li>a:hover, nav>ul>li > a:focus { color: #4078c0; text-decoration: none; }
      section.wrapper { margin: 10px 0 0; }
      section.wrapper section.content { padding-right: 1em; padding-left: 1em; }
      h2.title { font-size: 1.4em; }
      h2.title span { font-weight: normal; }
      table { table-layout: auto; font-size: 12px; line-height: 28px; border-collapse:collapse; width:100%; color: #888; }
      th {padding:0 .5em; text-align:left }
      td { border-top: 1px solid #eee; padding: 6px 10px; line-height: 20px; }
      thead tr { border-top: 1px solid #c1dce8; border-bottom: 1px solid #c1dce8; background:#e6f1f6; color: #555; }
      thead tr th { padding: 10px; }
      th.id, td.id { max-width: 70px; }
      td+td {  text-align:left }
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
