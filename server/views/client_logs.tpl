% rebase('base.tpl', title='All Logs')

    <section class="content">
      <h2 class="title"><a href="/logs">Logs</a> <span>/</span> <a href="/clients/{{client}}">{{client}}</a></h2>
    </section>
    <table>
      <thead>
        <tr>
          <th class="id">ID</th>
          <th>Time</th>
          <th>Level</th>
          <th>CPU (%)</th>
          <th>Memory (%)</th>
          <th>Threads Count</th>
        </tr>
      </thead>
      <tbody>
        %for item in logs:
        <tr>
          <td class="id">{{item["id"]}}</td>
          <td>{{item["time"]}}</td>
          <td>{{item["level"]}}</td>
          <td>{{item["cpu_percent"]}}</td>
          <td>{{item["memory_percent"]}}</td>
          <td>{{item["num_threads"]}}</td>
        </tr>
        %end
      </tbody>
    </table>
