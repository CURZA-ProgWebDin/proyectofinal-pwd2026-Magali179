<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()
function submit(){
    console.log('datos guardados')
    router.push({name:'Categorias'})
}


</script>

<template>
    <h1>Categorias Crear</h1>
     <button @click.prevent="submit">guardar categoria</button>

</template>