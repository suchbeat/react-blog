import React, { Component } from 'react';
import DocumentMeta from 'react-document-meta';
import { connect } from 'react-redux';

/* components */
import { Posts } from '../../components/Posts';

@connect(
    state => {
        return {state: state}
    }
)
export class BlogView extends Component {
    render() {
        return (
            <section>
                <Posts/>
            </section>
        );
    }
}
