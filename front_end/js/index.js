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
        host,
        recent_post: [],
    },

    mounted: function(){
	    this.get_recent_post();
    },

    methods: {

        get_recent_post: function(){
            // 获取最近更新文章列表
            axios.get(this.host + 'recent_posts/', {
                responseType: 'json',
            }).then(response=>{
                this.recent_post = response.data;
            }).catch(error=>{
                console.log("request recent posts failed")
            })
        },

    }
});


// get Home page list data
var vm2 = new Vue({
    el: "#index",
    delimiters: ['[[', ']]'],
    data: {
        host,
        posts_list: [],
    },

    mounted: function(){
	    this.get_index_list();
    },

    methods: {
        get_index_list: function(){
            // 获取首页文章列表
            axios.get(this.host + 'posts/', {
                responseType: 'json',
            }).then(response=>{
                this.posts_list = response.data;
            }).catch(error=>{
                console.log("request index posts failed")
            })
        },

    }
});


// get Technology & Life list data
var vm3 = new Vue({
    el: "#technology",
    delimiters: ['[[', ']]'],
    data: {
        host,
        tech_list: [],
        life_list: []
    },

    mounted: function(){
	    this.get_tech_list();
	    this.get_life_list();
    },

    methods: {
        get_tech_list: function(){
            // 获取首页文章列表
            axios.get(this.host + 'technologies/', {
                responseType: 'json',
            }).then(response=>{
                this.tech_list = response.data;
            }).catch(error=>{
                console.log("request failed")
            })
        },
        get_life_list: function(){
            // 获取首页文章列表
            axios.get(this.host + 'life/', {
                responseType: 'json',
            }).then(response=>{
                this.life_list = response.data;
            }).catch(error=>{
                console.log("request failed")
            })
        },

    }
});

// side bar function
var vm4 = new Vue({
    el: "#side",
    delimiters: ['[[', ']]'],
    data: {
        host,
        email: "",
        email_message: "",
        message_style: "",
        popular_post_list: [],
        recent_posts_list: [],
        check: true,
    },
    mounted: function(){
        this.get_popular_post_list();
        this.get_recent_posts();
    },
    methods: {
        check_email: function(){
            var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
            if (!this.email) {
                this.email_message = "请输入Email地址!";
                this.message_style = "red";
                this.check = false;
                return;
            }else if( !re.test(this.email)){
                this.email_message = "Email格式不正确！";
                this.message_style = "red";
                this.check = false;
                return;
            }
            this.check = true;
        },
        doSubmit: function(e){
            e.preventDefault();
            this.check_email();
            if (this.check){
                axios.post(this.host + "subscribe/", {
                email: this.email
                },{
                    responseType: 'json'
                },).then(response=>{
                    this.email_message = "订阅成功！";
                    this.message_style = "green";
                }).catch(error=>{
                    this.email_message = "您已订阅过本站，无需重复订阅";
                    this.message_style = "red";
                })
            }
        },

        get_popular_post_list: function(){
            // 获取最受欢迎文章列表
            axios.get(this.host + 'popular_post/', {
                responseType: 'json',
            }).then(response=>{
                this.popular_post_list = response.data;
            }).catch(error=>{
                console.log("request failed")
            })
        },

        get_recent_posts: function(){
            // 获取最近更新文章列表
            axios.get(this.host + 'recent_posts/', {
                responseType: 'json',
            }).then(response=>{
                this.recent_posts_list = response.data;
            }).catch(error=>{
                console.log("request failed")
            })
        },
    }
});


// get home page main pic
var vm5 = new Vue({
    el: "#slider",
    delimiters: ['[[', ']]'],
    data: {
        host,
        pic_list: [],
    },

    mounted: function(){
	    this.get_pic_list();
    },

    methods: {
        get_pic_list: function(){
            // 获取首页文章列表
            axios.get(this.host + 'main_pic/', {
                responseType: 'json',
            }).then(response=>{
                this.pic_list = response.data;
            }).catch(error=>{
                console.log("request failed")
            })
        },

    }
});

