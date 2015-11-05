% rebase('base.tpl', title='Clients')

    <section class="content">
      <h2 class="title">Clients</h2>
    </section>
    <table id="logs">
      <thead>
        <tr>
          <th class="id">ID</th>
          <th>Client Id</th>
          <th>Platform</th>
        </tr>
      </thead>
      <tbody>
        %for host in clients:
        <tr>
          <td class="id">{{host["id"]}}</td>
          <td><a href="/clients/{{host["client_id"]}}">{{host["client_id"]}}</a></td>
          <td>{{host["platform"]}}</td>
        </tr>
        %end
      </tbody>
    </table>
