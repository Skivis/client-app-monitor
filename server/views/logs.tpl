% rebase('base.tpl', title='All Logs - ')

    <section class="content">
      <h2 class="title">Logs</h2>
    </section>
    <table class="logs">
      <thead>
        <tr>
          <th class="id">ID</th>
          <th>Time</th>
          <th>Level</th>
          <th>Client Id</th>
          <th class="cpu">CPU (%)</th>
          <th>Memory (%)</th>
          <th>Threads</th>
        </tr>
      </thead>
      <tbody>
        %for item in logs:
        <tr class="{{item["level"].lower()}}">
          <td class="id">{{item["id"]}}</td>
          <td>{{item["time"]}}</td>
          <td>{{item["level"]}}</td>
          <td><a href="/logs/{{item["client_id"]}}">{{item["client_id"]}}</a></td>
          <td class="cpu">{{item["cpu_percent"]}}%</td>
          <td>{{item["memory_percent"]}}%</td>
          <td>{{item["num_threads"]}}</td>
        </tr>
        %end
      </tbody>
    </table>
