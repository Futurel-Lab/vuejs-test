<template>
  <div class="border p-3 m-3">
    <div class="container">
      <!-- Bootswatch CDN -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@5.3.3/dist/quartz/bootstrap.min.css"
      />
      <div class="row">
        <div class="col-sm-12">
          <p>Gaming Library</p>
          <hr />
          <br />
          <!-- Alert Message -->

          <button type="button" class="btn btn-success">Add Game</button>
          <br />
          <br />
          <table class="table table-hover">
            <!-- Table Head -->
            <thead>
              <tr>
                <!-- Table header cells -->
                <th scope="col">Title</th>
                <th scope="col">Genre</th>
                <th scope="col">Played?</th>
                <th scope="col">Price</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Tit</td>
                <td>Gen</td>
                <td>Pla</td>
                <td>Pri</td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info btn-sm">
                      Update
                    </button>
                    <button type="button" class="btn btn-danger btn-sm">
                      Remove
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
