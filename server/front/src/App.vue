<template>
  <MapExample></MapExample>
  <index></index>
  <input-product></input-product>
</template>

<script>
import MapExample from './components/MapExample'
import index from './components/indexOne'
import inputProduct from './components/inputProduct';
export default {
  name: 'App',
  components: {
    MapExample,
    index,
    inputProduct,
  },

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
