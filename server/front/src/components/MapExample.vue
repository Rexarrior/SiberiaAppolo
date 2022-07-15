<template>
  <h3>This is Map</h3>
  <yandex-map :settings="settings" :coords="coords" class="map-elem">
    <ymap-marker marker-id="123" :coords="coords" :balloon-template="balloonTemplate"></ymap-marker>
    <!--Markers-->
  </yandex-map>
</template>

<script>
import { yandexMap, ymapMarker } from 'vue-yandex-maps'

export default {
  name: 'MapExample',
  components: {
    yandexMap,
    ymapMarker
  },
  data: () => {
    return {
      settings: {
        apiKey: '0bc612ef-d8aa-4eba-946a-fbe66723d23c',
        lang: 'ru_RU',
        coordorder: 'latlong',
        enterprise: false,
        version: '2.1'
      },
      coords: [54, 39],
    }
  },
  computed: {
    balloonTemplate() {
      return `
        <h1 class="red">Hi, everyone!</h1>
        <p>I am here: ${this.coords}</p>
        <img src="http://via.placeholder.com/350x150">
      `
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.map-elem {
  width: 600px;
  height: 600px;
  margin-left: auto;
  margin-right: auto;
}
</style>
