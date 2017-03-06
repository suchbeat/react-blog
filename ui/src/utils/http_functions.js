import axios from 'axios'

var instance = axios.create({
  baseURL: 'http://0.0.0.0:5000',
  timeout: 1000
});

export function get_posts() {
    return instance.get('/posts')
}

export function get_single_post(post) {
    return instance.get('/posts/' + post)
}

export function create_post(title, body) {
    return instance.post('/posts', {
            title: title,
            content: body
        }
    )
}