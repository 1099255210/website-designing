<script setup>
import axios from 'axios'
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
</script>

<template>
  <div class="contain">
    <canvas id="main_canvas" width="500" height="500" background="grey"></canvas>
  </div>
  <button @click="draw">draw</button>
</template>

<script>
export default {
  data () {
    return {
      message: '',
    }
  },
  methods: {
    async sub(credentials) {
      const res = await axios.post('/api/login', credentials)
      console.log(res['data'])
      this.message = res['data']
    },
    draw() {
      var canvas = new fabric.Canvas('main_canvas')
      console.log(canvas)
      var rect = new fabric.Rect({
        top: 50,
        left: 50,
        width: 100,
        height: 100,
        fill: 'red'
      })
      canvas.add(rect)
    }
  }
}
</script>
