const Dotenv = require("dotenv-webpack");

module.exports = {
    entry: "./src/index.js", // Entry point of your application
    output: {
        path: __dirname + "/dist", // Output directory for bundled files
        filename: "bundle.js", // Output JavaScript filename
    },
    module: {
        rules: [
            {
                test: /\.js$/, // Use the loader for JavaScript files
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader", // Example: Using Babel for JavaScript
                },
            },
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            },
        ],
    },
    plugins: [
        new Dotenv({
            path: "./.env.prod",
            systemvars: true,
        }),
    ],
    mode: "development",
};
