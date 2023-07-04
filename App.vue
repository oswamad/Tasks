<script >
import axios from 'axios'
export default {
  name: "App",
  data(){
    return{
      posts : [],
      down_r: '',
      up_r: '',
      funtion_sym: '',

      chart: null,
      xVal: 0,
      options: {
        exportEnabled: true,
        title:{
          text: "Api Chart",
        },
        data: [{
          type: "line",
          dataPoints: []
        }]
      },
      styleOptions: {
        width: "600px",
        height: "500px",
        
      }

      
    }
  },
  methods: {
    getPosts(){
        axios.get('http://192.168.100.14:8000/func-api/'+this.down_r+'/'+this.up_r+'/'+this.funtion_sym)
        .then(response => this.updateChart(response.data))
    
    },

    updateChart(data) {
      this.posts = data
      this.options.data[0].dataPoints =[];
      for (var i = 0; i < this.posts.interval.length; i++) {
        this.options.data[0].dataPoints.push({
          x: this.posts.interval[i],
          y: this.posts.valuesfunc[i]
        });
      }
      this.chart.render();
    },

    chartInstance(chart) {
      this.chart = chart;
      this.options.data[0].dataPoints.push({
          x: 0,
          y: 0
        });
      this.chart.render();
    }

  }
}
</script>

<template>

  <h1>Evaluation Task</h1>
  <article>

    <div>
      <p id="from">From</p>
      <p id="to">To</p>
      <input type="text" id="text1" name="r1" v-model="down_r"> 
      <input type="text" id="text3" name="r2" v-model="up_r">
      <p id="fun">Function in terms of x</p>
      <input type="text" id="text2" name="r3" v-model="funtion_sym"> <br>
      <button @click="getPosts">Go</button><br>
    </div>
    
    <div>
      <CanvasJSChart :options="options" :style="styleOptions" @chart-ref="chartInstance"/>
    </div>
  </article>
  
  
</template>

<style scoped>
button {
  background-color: #4CAF50;
  color: white;
  font-size: 14px;
}
</style>
