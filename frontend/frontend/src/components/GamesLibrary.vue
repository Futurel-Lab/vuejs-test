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
          <h1 style="border-radius: 30px;" class="text-center bg-primary text-white">🎮Gaming Library🎮</h1>
          <hr />
          <br />
          <!-- Alert Message -->

          <button type="button" class="btn btn-success" v-b-model.game-modal>
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
      <b-modal
        ref="addGameModal"
        id="game-modal"
        title="Add New Game"
        hide-backdrop
        hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">

          <b-form-group id="form-title-group"
          label="Title: "
          label-for="form-title-input">
          
          <b-form-input
            required
            id="form-title-input"
            type="text"
            v-model="addGameForm.title"
            placeholder="Enter Game title">

        </b-form-input>
        </b-form-group>

        <b-form-group id="form-genre-group"
          label="Genre: "
          label-for="form-title-input">
          
          <b-form-input
            required
            id="form-title-input"
            type="text"
            v-model="addGameForm.genre"
            placeholder="Enter Game genre">

          </b-form-input>
        </b-form-group>

        <b-form-group id="form-price-group"
          label="Price: "
          label-for="form-title-input">
          
          <b-form-input
            required
            id="form-title-input"
            type="text"
            v-model="addGameForm.price"
            placeholder="Enter Game price">

          </b-form-input>
        </b-form-group>
<!-- Checkbox form input -->
        <b-form-group id="form-played-group">

          <b-form-checkbox-group v-model="addGameForm.played">
            <b-form-checkbox value="true">Played</b-form-checkbox>
          </b-form-checkbox-group>
<!-- Submit/Reset Buttons -->
          <button type="submit" variant="primary">Submit</button>
          <button type="reset" variant="primary">Reset</button>

        </b-form-group>



        </b-form>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      games: [],
      addGameForm: {
        title: "",
        genre: "",
        price: "",
        played: [],
      },
    };
  },
  methods: {
    //Get function
    getGames() {
      const path = "http://localhost:5000/games";
      axios
        .get(path)
        .then((res) => {
          this.games = res.data.games;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    //Post function
    addGame(payload) {
      const path = "http://localhost:5000/games";
      axios
        .post(path, payload)
        .then(() => {
          this.getGames();
          this.message = "Game added successfully!";
          this.showMessage = true;
        })
        .catch((err) => {
          console.error(err);
          this.getGames();
        });
    },
    initForm() {
      this.addGameForm.title = "";
      this.addGameForm.genre = "";
      this.addGameForm.price = "";
      this.addGameForm.played = [];
    },
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addGameModal.hide();
      let played = false;
      const payload = {
        title: this.addGameForm.title,
        genre: this.addGameForm.genre,
        price: this.addGameForm.price,
        played,
      };
      this.addGame(payload);
      this.initForm();
    },
  },
  created() {
    this.getGames();
  },
};
</script>
