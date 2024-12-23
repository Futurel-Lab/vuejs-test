<template>
  <div class="border p-3 m-3">
    <div class="container">
      <!-- Bootswatch CDN -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@5.3.3/dist/sketchy/bootstrap.min.css"
      />
      <div class="row">
        <div class="col-sm-12">
          <!-- prettier-ignore -->
          <h1 style="border-radius: 30px;" class="text-center bg-info text-white">🎮Gaming Library🎮</h1>
          <hr />
          <br />
          <!-- Alert Message -->
          <!-- prettier-ignore -->
          <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#addGameModal">
            Add Game
          </button>
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
              <tr v-for="(game, index) in games" :key="index">
                <td>{{ game.title }}</td>
                <td>{{ game.genre }}</td>
                <td>
                  <span v-if="game.played">✅</span>
                  <span v-else>⛔</span>
                </td>
                <td>${{ game.price }}</td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info btn-sm">
                      <img src="../assets/editing.png" width="16" height="16" />
                    </button>
                    <button type="button" class="btn btn-danger btn-sm">
                      <img src="../assets/trash.png" width="16" height="16" />
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer class="bg-primary text-white text-center">
            Copyright &copy; All Rights Reserved 2025
          </footer>
        </div>
      </div>
      <!-- First Modal -->
      <!-- prettier-ignore -->
      <div class="modal fade" id="addGameModal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="addGameModalTitle">Add New Game</h1>
              <button class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
              <form @submit="onSubmit" id="addGameForm">
                <div class="mb-3">
                  <!-- <label for="gameTitle" class="form-label">Game Title</label> -->
                  <input required type="text" id="gameTitle" v-model="addGameForm.title" class="form-control" placeholder="Game Title">
                </div>
                <div class="mb-3">
                  <input required type="text" id="gameGenre" v-model="addGameForm.genre" class="form-control" placeholder="Game Genre">
                </div>
                <div class="mb-3">
                  <input required type="number" id="gamePrice" step="00.01" v-model="addGameForm.price" class="form-control" placeholder="Game Price">
                </div>
                <div class="mb-3 form-check">
                  <label for="gamePlayed" class="form-check-label">Played?</label>
                  <input type="checkbox" id="gamePlayed" v-model="addGameForm.played" class="form-check-label">
                </div>
                <button class="btn btn-primary">Add Game</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gamesScript from "./js/GamesLibrary.js";

export default {
  ...gamesScript,
};
</script>
