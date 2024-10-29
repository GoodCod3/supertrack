const webpack = require("webpack");
const path = require("path");
const process = require("process");
const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  mode: process.env.MODE || "production",
  entry: "./statics/dashboard/js/index.tsx",
  output: {
    path: path.resolve(__dirname, "statics", "dashboard", "builds"),
    filename: "bundle.js",
  },
  devtool: "source-map",
  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: "webpack-stats.json",
    }),
    new webpack.DefinePlugin({
      "process.env": JSON.stringify({
        API_ENDPOINT_URL: "http://localhost:8080",
      }),
    }),
  ],
  
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: { presets: ["@babel/preset-env"] },
        },
      },
      {
        test: /\.(ts|tsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: [
              "@babel/preset-env",
              "@babel/preset-react",
              "@babel/preset-typescript",
            ],
          },
        },
      },
    ],
  },
  resolve: {
    extensions: [".tsx", ".ts", ".js", ".jsx"],
    alias: {
        "@src": path.resolve(__dirname, "statics/dashboard/js/"),
        "@components": path.resolve(__dirname, "statics/dashboard/js/components"),
      },
  },
};
