// 格式化时间输出
Vue.filter('Date',function(value){
    var d = new Date(value);
       var year = d.getFullYear();
       var month = d.getMonth() + 1;
       var day = d.getDate() <10 ? '0' + d.getDate() : '' + d.getDate();
       var hour = d.getHours();
       var minutes = d.getMinutes();
       var seconds = d.getSeconds();
       var eng_month = ""
       if(month==1){
           eng_month = "Jan"
       }else if(month==2){
           eng_month = "Feb"
       }else if(month==3){
           eng_month = "Mar"
       }else if(month==4){
           eng_month = "Apr"
       }else if(month==5){
           eng_month = "May"
       }else if(month==6){
           eng_month = "Jun"
       }else if(month==7){
           eng_month = "Jul"
       }else if(month==8){
           eng_month = "Aug"
       }else if(month==9){
           eng_month = "Sep"
       }else if(month==10){
           eng_month = "Oct"
       }else if(month==11){
           eng_month = "Nov"
       }else if(month==12){
           eng_month = "Dec"
       }
       return  eng_month + ' ' + day + ', ' + year;
});


// BreakingNews Bar Data
var vm = new Vue({
    el: "#breaking",
    delimiters: ['[[', ']]'],
    data: {
        recent_post: [],
        posts_list: [],
    },

    mounted: function(){
	    this.get_recent_post();
	    this.get_index_list();
    },

    methods: {

        get_recent_post: function(){
            // 获取最近更新文章列表
            axios.get('http://127.0.0.1:8000/recent_posts/', {
                responseType: 'json',
            }).then(response=>{
                this.recent_post = response.data;
            }).catch(error=>{
                console.log("最近更新加载失败！")
            })
        },
        get_index_list: function(){
            // 获取首页文章列表
            axios.get('http://127.0.0.1:8000/posts/', {
                responseType: 'json',
            }).then(response=>{
                this.posts_list = response.data;
            }).catch(error=>{
                alert("网络连接超时，请稍后再试~")
            })
        },

    }
});


// get Home page list data
var vm2 = new Vue({
    el: "#index",
    delimiters: ['[[', ']]'],
    data: {
        posts_list: [],
    },

    mounted: function(){
	    this.get_index_list();
    },

    methods: {
        get_index_list: function(){
            // 获取首页文章列表
            axios.get('http://127.0.0.1:8000/posts/', {
                responseType: 'json',
            }).then(response=>{
                this.posts_list = response.data;
            }).catch(error=>{
                alert("网络连接超时，请稍后再试~")
            })
        },

    }
});
