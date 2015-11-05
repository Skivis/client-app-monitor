% rebase('base.tpl', title='All Logs')

    <h1>All Logs</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Time</th>
          <th>Level</th>
          <th>Client Id</th>
          <th>CPU (%)</th>
          <th>Memory (%)</th>
          <th>Threads Count</th>
        </tr>
      </thead>
      <tbody>
        %for item in logs:
        <tr>
          <td>{{item["id"]}}</td>
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
