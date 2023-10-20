/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
module.exports = {
  content: ["./src/**/*.{html,tsx, js}"],
  theme: {
    extend: {
      colors: {
        bg_color: '#ffe1bc'
      }
    },
  },
  plugins: [],
}

