<script setup>
import {onMounted, ref} from 'vue'
import {NDynamicInput, NDatePicker, NTreeSelect, NInputNumber, NSwitch} from 'naive-ui'

const credentialCount = ref(0)
const keywords = ref(["丁真"])
const dateRange = ref([1293872260000, Date.now()])
const cityCode = ref(null);
const region = ref(0)

const regionData = ref()
const res = ref(null)
const autoSave = ref(false)

onMounted(() => {
  fetch('/api/credentials')
      .then(response => response.json())
      .then(data => {
        credentialCount.value = data.count
      })

  fetch('/region.json')
      .then(response => response.json())
      .then(data => {
        regionData.value = data
      })

  fetch('/city.json')
      .then(response => response.json())
      .then(data => {
        cityCode.value = data
      })
})

const posting = ref(false)
const expectedInterval = ref(2000)

const f1 = (val) => {
  // 对keywords的每一项再包裹一层数组，若原字符串带有+号，以+号分割到数组中
  return val.map(item => item.split('+'))
}

const f2 = (val) => {
  // Date.now()换转为xxxx-xx-xx格式
  return new Date(val).toISOString().split('T')[0]
}

const post = () => {
  posting.value = true
  fetch('/api/crawl', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      keywords: f1(keywords.value),
      startDate: f2(dateRange.value[0]),
      endDate: f2(dateRange.value[1]),
      regionCode: region.value,
      expectedInterval: expectedInterval.value,
      autoSave: autoSave.value
    })
  })
      .then(response => response.json())
      .then(data => {
        // 若为400，说明请求参数有误
        if (data.code === 400) {
          alert(data.message)
          posting.value = false
          return
        }
        console.log(data.data)
        res.value = data.data
        posting.value = false
      })
}
</script>

<template>
  <div>
    <span class="a">已登陆账号: {{ credentialCount }}</span>
  </div>
  <div style="display: flex; gap:40px;">
    <div style="flex: 1; background: #fbfbff; padding: 20px; border-radius: 10px;" class="c">
      <h4><strong>Keywords(Max: 5)</strong></h4>
      <div class="min">填词, 一组最多5格，超过5格会分组发送，中间间隔时间。词内用+号可以连接最多三个词语查询其总和</div>
      <NDynamicInput v-model:value="keywords"
                     :min="1"
                     :placeholder="'Enter a keyword or a key word group'"
      />

      <h4><strong>Date Range</strong></h4>
      <div class="min">最早 2011 年（要确保查询整年数据的话，起始日期就应该是1月1日）</div>
      <n-date-picker v-model:value="dateRange" type="daterange" clearable/>

      <h4>Region Choose</h4>
      <div class="min">Global, Province or a city</div>

      <n-tree-select :options="regionData" @update-value="(val,e)=>{region=val}"/>

      <h4>Expected Interval</h4>
      <div class="min">发送api请求的间隔时间，单位毫秒</div>
      <n-input-number v-model:value="expectedInterval" :min="1000" :max="10000" :step="1000"/>

      <h4>Auto Save</h4>
      <div class="min" style="margin-bottom: 0">自动保存查询结果到根目录的output文件夹下，无需导出</div>

      <n-switch v-model:value="autoSave"/>

      <button class="b" @click="post">{{ posting ? "Posting..." : "Get" }}</button>

    </div>
    <div style="flex: 2; background: #fbfbff; padding: 20px; border-radius: 10px;" class="c">
      <div v-for="(entries, key) in res" :key="key">
        <div style="margin-bottom: 5px;">{{cityCode[key]}}</div>
        <div v-for="(entry, index) in entries" :key="entry">
          <div style="margin-bottom: 5px;">{{keywords[index]}}</div>
            <table border="1">
              <thead>
              <tr>
                <th>Year</th>
                <th>Average</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="item in entry" :key="item.Year">
                <td>{{ item.Year }}</td>
                <td>{{ item.Average }}</td>
              </tr>
              </tbody>
            </table>
          </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.a {
  display: inline-block;
  padding: 10px 20px;
  border-radius: 5px;
  background-color: #238604;
  color: white;
  margin-bottom: 20px;
}

.min {
  font-size: 12px;
  color: #666;
  margin-bottom: 10px;
}

.c {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.b {
  display: block;
  padding: 10px 20px;
  border-radius: 5px;
  background-color: #238604;
  color: white;
  margin-top: 20px;
  cursor: pointer;
}
</style>
