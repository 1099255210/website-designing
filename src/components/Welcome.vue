<template>
  <h1>欢迎来到电子商务海报智能设计平台</h1>

  <v-carousel
    height="800"
  >
    <v-carousel-item
      v-for="i in img_list"
      :src="i"
      cover
    ></v-carousel-item>
  </v-carousel>
</template>

<style scoped>

div {
  margin: 10px;
}

</style>

<script>
import img_1 from '@/assets/images/l1.jpg'
import img_2 from '@/assets/images/l2.jpg'
import img_3 from '@/assets/images/l3.jpg'
import img_4 from '@/assets/images/l4.jpg'

export default {
  data() {
    return {
      img_list: [img_1, img_2, img_3, img_4],
    };
  }
};
</script>