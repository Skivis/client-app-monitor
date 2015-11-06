% rebase('base.tpl', title=data["client_id"])

    <section class="content">
      <h2 class="title"><a href="/clients">Clients</a> <span>/</span> {{data["client_id"]}}</h2>
      <a class="btn logs" href="/logs/{{data["client_id"]}}">View logs</a>
    </section>
    <table>
      <thead>
        <tr>
          <th>Client Id</th>
          <th>Node</th>
          <th>System</th>
          <th>Platform</th>
          <th>Processor</th>
          <th>Cores</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{data["client_id"]}}</td>
          <td>{{data["node"]}}</td>
          <td>{{data["system"]}}</td>
          <td>{{data["platform"]}}</td>
          <td>{{data["processor"]}}</td>
          <td>{{data["cpu_count"]}}</td>
        </tr>
      </tbody>
    </table>
