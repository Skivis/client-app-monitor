% rebase('base.tpl', title='Logs for ' + client + ' - ')

    <section class="content">
      <h2 class="title"><a href="/logs">Logs</a> <span>/</span> <a href="/clients/{{client}}">{{client}}</a></h2>
    </section>
    <table>
      <thead>
        <tr>
          <th class="id">ID</th>
          <th>Time</th>
          <th>Level</th>
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
          <td class="{{item["level"].lower()}}">{{item["level"]}}</td>
          <td class="cpu">{{item["cpu_percent"]}}%</td>
          <td>{{item["memory_percent"]}}</td>
          <td>{{item["num_threads"]}}</td>
        </tr>
        %end
      </tbody>
    </table>
