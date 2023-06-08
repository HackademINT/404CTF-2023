const express = require("express");
const { query, validationResult, body } = require("express-validator");

const PORT = process.env.PORT || 3000;

const app = express();

// middleware
app.use(express.static("public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// view engine
app.set("view engine", "ejs");

// routes
app.get("/", (req, res) => {
  res.render("home");
});

app.get("/scene", (req, res) => {
  res.render("scene");
});

app.post(
  "/scene",
  body("url")
    .notEmpty()
    .isURL({ protocols: ["http", "https"] }),
  (req, res) => {
    console.log(req.body);
    const result = validationResult(req);
    if (result.isEmpty()) {
      return res.render("scene", req.body);
    }

    return res.send({
      msg: "req.body.url is not a proper URL",
      errors: result.array(),
    });
  }
);

app.use(function (req, res) {
  res.status(404).render("error404");
});

app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});
