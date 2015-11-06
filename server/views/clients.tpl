% rebase('base.tpl', title='All Clients')

    <section class="content">
      <h2 class="title">Clients</h2>
    </section>
    <table id="logs">
      <thead>
        <tr>
          <th class="id">ID</th>
          <th>Client Id</th>
          <th>Node</th>
          <th>System</th>
          <th>Processor</th>
        </tr>
      </thead>
      <tbody>
        %for client in clients:
        <tr>
          <td class="id">{{client["id"]}}</td>
          <td><a href="/clients/{{client["client_id"]}}">{{client["client_id"]}}</a></td>
          <td>{{client["node"]}}</td>
          <td>{{client["system"]}}</td>
          <td>{{client["processor"]}}</td>
        </tr>
        %end
      </tbody>
    </table>
