/** @odoo-module **/

//console.log("blog_tag_selector.js chargé !");

import options from "@web_editor/js/editor/snippets.options";
import dynamicSnippetOptions from "@website/snippets/s_dynamic_snippet/options";
import wUtils from "@website/js/utils";

const DynamicSnippetBlogPosts = options.registry.dynamic_snippet_blog_posts;

const BlogTagSelector = DynamicSnippetBlogPosts.extend({
    init: function () {
//	console.log("blog_tag_selector.js init !");
        this._super.apply(this, arguments);
        this.tags = {}; // Liste de tags vide initialement
    },

    _fetchTags() {
        return this.orm.searchRead("blog.tag", [], ["id", "name"]); // Pas de filtre
    },

    _renderCustomXML: async function (uiFragment) {
//        console.log("✅ _renderCustomXML déclenché");
        await this._super.apply(this, arguments);
        await this._renderTagSelector(uiFragment);
    },

    _renderTagSelector: async function (uiFragment) {
        // Si les tags ne sont pas déjà chargés
        if (!Object.keys(this.tags).length) {
            const tagsList = await this._fetchTags();
            this.tags = {};
            for (let index in tagsList) {
                this.tags[tagsList[index].id] = tagsList[index]; // Remplir l'objet des tags
            }
        }

        // Recherche de l'élément dans le DOM où le sélecteur sera injecté
        const tagSelectorEl = uiFragment.querySelector('[data-name="tag_opt"]');
        return this._renderSelectUserValueWidgetButtons(tagSelectorEl, this.tags); // Injection des options
    },

    _setOptionsDefaultValues: function () {
        this._super.apply(this, arguments);
        this._setOptionValue('filterByBlogTagId', -1); // Valeur par défaut pour "Tous les tags"
    },
});

// Enregistrement de la nouvelle classe étendue dans le registre des options
options.registry.dynamic_snippet_blog_posts = BlogTagSelector;

export default BlogTagSelector;
