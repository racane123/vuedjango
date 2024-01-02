<template>
    <div>
      <ul>
        <li v-for="genre in data" :key="genre.id">
          <h3>{{ genre.genre_name }}</h3>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Content',
    data() {
      return {
        data: [],
      };
    },
    created() {
      this.fetchData();
    },
    methods: {
      fetchData() {
        axios.get('http://127.0.0.1:8000/api/genres')
          .then(response => {
            this.data = response.data;
          })
          .catch(error => {
            console.error('Error fetching the data:', error);
          });
      },
    },
  };
  </script>
  
  <style scoped>

  </style>
  