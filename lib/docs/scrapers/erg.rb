module Docs
  class Erg < UrlScraper
    self.name = 'ERG Guidance'
    self.slug = 'erg_guidance'
    self.type = 'simple'
    self.base_url = 'https://daringfireball.net/projects/markdown/syntax'

    html_filters.push 'markdown/clean_html', 'markdown/entries'

    options[:container] = '.article'
    options[:skip_links] = true

    options[:attribution] = <<-HTML
      &copy; 2004 John Gruber<br>
      Licensed under the BSD License.
    HTML

    def get_latest_version(opts)
      '1.0.0'
    end
  end
end
