/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

//odoo.isReady.then(() => {
$(document).ready(function () {
    const OriginalWidget = publicWidget.registry.blog_posts;

    if (!OriginalWidget) {
        console.warn("⚠️ blog_posts widget introuvable au moment du chargement.");
        return;
    }

    if (OriginalWidget.prototype._isExtendedWithTagFilter) {
        return;
    }

    const Extended = OriginalWidget.extend({
        _isExtendedWithTagFilter: true,

        _getSearchDomain() {
            const domain = this._super(...arguments);
            const tagId = parseInt(this.el.dataset.filterByBlogTagId);
            if (!isNaN(tagId) && tagId >= 0) {
                domain.push(["tag_ids", "in", tagId]);
            }
            return domain;
        },
    });

    publicWidget.registry.blog_posts = Extended;
});
