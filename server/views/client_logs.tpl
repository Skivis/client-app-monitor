% rebase('base.tpl', title=client)

    <section class="content">
      <h2 class="title"><a href="/logs">Logs</a> <span>/</span> <a href="/clients/{{client}}">{{client}}</a></h2>
    </section>
    %if not logs:
    <section class="content empty">
      <h2>No logs at the moment...?</h2>
      <p>Finally, it seems, we found ourselves a client that's actually doing ok!<p>
    </section>
    %else:
    <table>
      <thead>
        <tr>
          <th class="id">ID</th>
          <th>Time</th>
          <th>Level</th>
          <th class="cpu">CPU (%)</th>
          <th>Memory (%)</th>
          <th>System CPU</th>
          <th>Threads</th>
        </tr>
      </thead>
      <tbody>
        %for log in logs:
        <tr class="{{log["level"].lower()}}">
          <td class="id">{{log["id"]}}</td>
          <td>{{log["time"]}}</td>
          <td class="{{log["level"].lower()}}">{{log["level"]}}</td>
          <td class="cpu">{{log["cpu_percent"]}}%</td>
          <td>{{log["memory_percent"]}}</td>
          <td>{{log["system_cpu"]}}</td>
          <td>{{log["num_threads"]}}</td>
        </tr>
        %end
      </tbody>
    </table>
    %end
