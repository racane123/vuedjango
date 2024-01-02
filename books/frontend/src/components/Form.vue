<template>
    <div>
      <form @submit.prevent="submitForm">
        <label for="title">Title:</label>
        <input v-model="newBook.genre_name" type="text" id="title" required>
  
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Content',
    data() {
      return {
        newBook: {
          genre_name: '',
        },
      };
    },
    methods: {
      submitForm() {
        // Send a POST request to your Django API endpoint
        axios.post('http://127.0.0.1:8000/api/genres/', this.newBook)
          .then(response => {
            console.log('Book added successfully:', response.data);
            // Optionally, you can reset the form or perform other actions
            this.resetForm();
          })
          .catch(error => {
            console.error('Error adding book:', error);
          });
      },
      resetForm() {
        // Reset the form fields
        this.newBook = {
          genre_name: '',

        };
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your component-specific styles here */
  </style>
  