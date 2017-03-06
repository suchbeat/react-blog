import React, { Component } from 'react';

import style from './clean-blog.css';


import { get_posts } from '../../utils/http_functions'

export class Posts extends Component {

    constructor(props) {
        super(props);
        this.state = {
            posts: [],
            loading: true
        }
    }

    formatDate(date) {
        var hours = date.getHours();
        var minutes = date.getMinutes();
        var ampm = hours >= 12 ? 'pm' : 'am';
        hours = hours % 12;
        hours = hours ? hours : 12; // the hour '0' should be '12'
        minutes = minutes < 10 ? '0'+minutes : minutes;
        var strTime = hours + ':' + minutes + ' ' + ampm;
        return date.getMonth()+1 + "/" + date.getDate() + "/" + date.getFullYear() + "  " + strTime;
    }

    componentDidMount() {
        setTimeout(() => {
            get_posts()
                .then((response) => {

                        let posts = response.data.data;

                        //change from string into string date objects
                        for (var i = 0; i < posts.length; i++) {
                            posts[i].pub_date = new Date(posts[i].pub_date);
                            posts[i].pub_date = this.formatDate(posts[i].pub_date);
                            posts[i].content = {__html: posts[i].content};
                        }

                        this.setState({
                            posts: posts,
                            loading: false
                        })
                    }
                );
        }, 500);

    }

    render() {
        return (
            <div>
                {this.state.loading ? <div className="loader">Loading...</div> :
                    <div className="container" style={style}>
                        <div className="container centered">
                            <h2><b>Blog Posts</b></h2>
                        </div>
                        <div className="row">
                            <div className="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                                <div className="post-preview">
                                    {
                                        this.state.posts.map((post, index) =>
                                            <div key={index}>
                                                <a href={"#/post/" + post.id}>
                                                    <h2 className="post-title">
                                                        {post.title}
                                                    </h2>
                                                </a>

                                                <p dangerouslySetInnerHTML={post.content}></p>

                                                <p className="post-meta">Posted on {post.pub_date}</p>
                                                <hr/>
                                            </div>
                                        )
                                    }
                                </div>
                            </div>
                        </div>
                    </div>
                }
            </div>

        )
    }


}
