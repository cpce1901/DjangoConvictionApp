/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    '../apps/users/forms.py',
    '../apps/graphics/forms.py'
  ],
  theme: {
    extend: {
      backgroundImage:{
        "login": "url('/static/img/energia.jpg')",
        "proceso": "url('/static/img/proceso.jpg')",
      },
      fontFamily: {
        "exo": ['"exo 2"'],
        "rale": ['"Raleway"'],
      },
    },
  },
  plugins: [],
}

