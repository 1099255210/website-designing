<template>
  <v-row>
    <v-col cols="2">
      留白
    </v-col>
  </v-row>
  <v-row>
    <v-col cols="3">
      <v-card class="mx-auto" max-width="344" variant="outlined">
        <v-card-item>
          <div class="text-overline mb-1">Recommend</div>
          <div class="text-h6 mb-1">推荐布局</div>
        </v-card-item>
      </v-card>
      <v-divider class="my-10"></v-divider>
      <v-card class="mx-auto" max-width="344" variant="outlined">
        <v-card-item>
          <div>
            <div class="text-overline mb-1">
              商品信息
            </div>

            <div class="text-h6 mb-1">商品名称</div>
            <div class="text-caption">{{ childMsg.productName }}</div>

            <div class="text-h6 mb-1">商品类型</div>
            <div class="text-caption">{{ childMsg.productType }}</div>

            <div class="text-h6 mb-1">商品主图</div>
            <div class="align-center">
              <v-img :src="childMsg.productImg"></v-img>
            </div>
            
            <div class="text-h6 mb-1">商品宣传语</div>
            <div v-for="(text, index) in childMsg.promote" :key="index" class="text-caption">{{ text }}</div>

            <v-btn variant="outlined" :loading="loading" @click="loading = !loading">
              开始设计
              <!-- <template v-slot:loader>
                <v-progress-linear indeterminate></v-progress-linear>
              </template> -->
            </v-btn>
          </div>

        </v-card-item>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import axios from "axios"

export default ({
  data() {
    return {
      imgList: [],
      loading: false,
      propCopy: this.childMsg
    }
  },
  props: {
    childMsg: {
      productName: "",
      productType: "",
      productImg: "",
      promote: []
    }
  },
  watch: {
    loading (val) {
      if (!val) return
      this.propCopy.productImg = this.propCopy.productImg.currentSrc
      console.log(this.propCopy)
      axios.post('/api/inference', this.propCopy)
      .then(response => {
        const jsonData = response.data
        this.$emit('sendlayout', jsonData)
      })
    },
  },
  emits: ['sendlayout'],
})
</script>