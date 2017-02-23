import React from 'react';
import { Route } from 'react-router';

/* containers */
import { App } from 'containers/App';
import { BlogView } from 'containers/BlogView'
import { EachPostView } from 'containers/EachPostView'
import { EditorContainer } from 'containers/EditorContainer'


export default (
    <Route path="/" component={App}>
        <Route path="blog" component={BlogView} />
        <Route path="post/:id" component={EachPostView} />
        <Route path="editor" component={EditorContainer} />
    </Route>
);
