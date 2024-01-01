<script>
import axios from 'axios'


export default {
    mounted(){
        axios.get('http://127.0.0.1:8000/api/books')
        .then(response => {
            console.log(response.data)
        })
        .catch(error => {
            console.error('Error fetching data: ', error)
        })
    },
}


</script>

<template>
<form action="" method="post" class="form-storing">
    <label for="title">Book Title</label>
    <input type="text" name="" id="">
    <label for="summary">Book Summary</label>
    <input type="text" name="" id="">
    <label for="">Book Published Date</label>
    <input type="datetime" name="" id="">
    <label for="">Author:</label>
    <select name="" id=""></select>
    <label for="Genre">Genre</label>
    <select name="" id=""></select>
    <input type="file" accept="image/">
    <button @click.prevent='addBook'>Add Book</button>
</form>
</template>

<style scoped>




</style>