<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Client Monitoring</title>
    <style>
      table {
        table-layout:auto; font:11px/24px Verdana,Arial,sans-serif; border-collapse:collapse; width:720px }
      th {
        padding:0 .5em; text-align:left }
      td {
        border-bottom: 1px solid #CCC; padding:0 .5em }
      thead tr {
        border-top:1px solid #FB7A31; border-bottom:1px solid #FB7A31; background:#FFC }
      td+td {
        border-left:1px solid #CCC; text-align:left }
  </style>
  </head>
  <body>
    <h1>All Logs</h1>
    <table>
      <thead>
        <tr>
          <th>Level</th>
          <th>Time</th>
          <th>Client Id</th>
          <th>CPU (%)</th>
          <th>Memory (%)</th>
          <th>Threads Count</th>
        </tr>
      </thead>
      <tbody>
        %for item in logs:
        <tr>
          <td>{{item["time"]}}</td>
          <td>{{item["level"]}}</td>
          <td><a href="/clients/{{item["client_id"]}}">{{item["client_id"]}}</a></td>
          <td>{{item["cpu_percent"]}}</td>
          <td>{{item["memory_percent"]}}</td>
          <td>{{item["num_threads"]}}</td>
        </tr>
        %end
      </tbody>
    </table>
  </body>
</html>
