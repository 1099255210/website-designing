<script>
import Prepare from '../components/Prepare.vue'
import Recommend from '../components/Recommend.vue'
import Modify from '../components/Modify.vue'

export default {
  components: {
    Prepare,
    Recommend,
    Modify,
  },
  data() {
    return {
      currentStep: 'a',
      stepList: ['a', 'b', 'c'],
      productInfo: {
        productName: "",
        productType: "",
        productImg: "",
        promote: []
      },
      layoutInfo: {}
    };
  },
  methods: {
    dealinfo(data) {
      this.productInfo = data
      this.moveToNext()
      console.log(this.productInfo)
    },
    setlayout(data) {
      this.layoutInfo = data
      this.layoutInfo['data']['img'] = this.productInfo.productImg
      this.moveToNext()
      console.log(this.layoutInfo)
    },
    hasStep(step, direction) {
      var index = this.stepList.indexOf(step)
      if (direction === 'next' && index + 1 < this.stepList.length) {
        return this.stepList[index + 1]
      }
      if (direction === 'prev' && index > 0) {
        return this.stepList[index - 1]
      }
      return false
    },
    changeStep(nextStep) {
      this.currentStep = nextStep;
    },
    moveToNext() {
      var nextStep = this.hasStep(this.currentStep, 'next')
      if (nextStep) {
        this.changeStep(nextStep)
      }
    },
    moveToPrev() {
      var prevStep = this.hasStep(this.currentStep, 'prev')
      if (prevStep) {
        this.changeStep(prevStep)
      }
    },
  },
  computed: {
    havenext() {
      return this.hasStep(this.currentStep, 'next')
    },
    haveprev() {
      return this.hasStep(this.currentStep, 'prev')
    },
  },
};
</script>

<template>
  <div>
    <v-btn v-if="haveprev" variant="outlined" @click="moveToPrev()" class="mx-3">返回</v-btn>
    <v-btn v-if="havenext" variant="outlined" @click="moveToNext()" class="mx-3">下一步</v-btn>
    <v-divider class="my-5"></v-divider>
    <div v-if="currentStep === 'a'">
      <Prepare @sendinfo="dealinfo"></Prepare>
    </div>
    <div v-else-if="currentStep === 'b'">
      <Recommend :childMsg="productInfo" @sendlayout="setlayout" />
    </div>
    <div v-else-if="currentStep === 'c'">
      <Modify :preset="layoutInfo" />
    </div>
  </div>
</template>