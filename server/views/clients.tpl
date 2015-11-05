% rebase('base.tpl', title='All Clients')

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
          <td><a href="/clients/{{host["client_id"]}}">{{host["client_id"]}}</a></td>
          <td>{{host["platform"]}}</td>
        </tr>
        %end
      </tbody>
    </table>
