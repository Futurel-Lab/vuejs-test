import { Modal } from "bootstrap";
import axios from "axios";
const modalElement = document.getElementById("addGameModal");
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
          this.getGames(); // Refresh the games list
          this.message = "Game added successfully!";
          this.showMessage = true;

          if (modalElement) {
            // Check if the modal instance exists, if not, create a new instance
            let modalInstance = Modal.getInstance(modalElement);
            if (!modalInstance) {
              modalInstance = new Modal(modalElement);
            }

            // Hide the modal
            modalInstance.hide();

            // Remove any existing modal backdrops after the modal is hidden
            modalElement.addEventListener(
              "hidden.bs.modal",
              () => {
                // Remove all modal backdrops manually
                document
                  .querySelectorAll(".modal-backdrop")
                  .forEach((backdrop) => backdrop.remove());
              },
              { once: true }
            );
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
    initForm() {
      this.addGameForm.title = "";
      this.addGameForm.genre = "";
      this.addGameForm.price = "";
      this.addGameForm.played = null;
    },
    onSubmit(e) {
      e.preventDefault();

      console.log(this.addGameForm);
      const payload = {
        title: this.addGameForm.title,
        genre: this.addGameForm.genre,
        price: this.addGameForm.price,
        played: this.addGameForm.played,
      };
      this.addGame(payload);
      this.initForm();
    },
  },
  created() {
    this.getGames();
  },
};
