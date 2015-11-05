<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Client Monitoring</title>
    <style>
      table {
        table-layout:auto; font:11px/24px Verdana,Arial,sans-serif; border-collapse:collapse; width:620px }
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
    <h1>Clients</h1>
    <table id="logs">
      <thead>
        <tr>
          <th>Id</th>
          <th>Client Id</th>
          <th>Platform</th>
        </tr>
      </thead>
      <tbody>
        %for host in clients:
        <tr>
          <td>{{host["id"]}}</td>
          <td>{{host["client_id"]}}</td>
          <td>{{host["platform"]}}</td>
        </tr>
        %end
      </tbody>
    </table>
  </body>
</html>
