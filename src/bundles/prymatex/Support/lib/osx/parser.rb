#--###########################################################
# Copyright 2006, Ben Bleything <ben@bleything.net> and      #
# Patrick May <patrick@hexane.org>                           #
#                                                            #
# Distributed under the MIT license.                         #
##############################################################
#++
# Plist parses Mac OS X xml property list files into ruby data structures.
#
# === Load a plist file
# This is the main point of the library:
#
#   r = OSX::PropertyList::load( filename_or_xml )
module OSX
 module PropertyList
# Note that I don't use these two elements much:
#
#  + Date elements are returned as DateTime objects.
#  + Data elements are implemented as Tempfiles
#
# OSX::PropertyList::load will blow up if it encounters a data element.
# If you encounter such an error, or if you have a Date element which
# can't be parsed into a Time object, please send your plist file to
# plist@hexane.org so that I can implement the proper support.
  def PropertyList::load( filename_or_xml, return_type = false )
    listener = Listener.new
    #parser = REXML::Parsers::StreamParser.new(File.new(filename), listener)
    parser = StreamParser.new(filename_or_xml, listener)
    parser.parse
    return_type ? [listener.result, :xml1] : listener.result
  end

  class Listener
    #include REXML::StreamListener

    attr_accessor :result, :open

    def initialize
      @result = nil
      @open   = Array.new
    end


    def tag_start(name, attributes)
      @open.push PTag::mappings[name].new
    end

    def text( contents )
      @open.last.text = contents if @open.last
    end

    def tag_end(name)
      last = @open.pop
      if @open.empty?
        @result = last.to_ruby
      else
        @open.last.children.push last
      end
    end
  end

  class StreamParser
    def initialize( filename_or_xml, listener )
      @filename_or_xml = filename_or_xml
      @listener = listener
    end

    TEXT       = /([^<]+)/
    XMLDECL_PATTERN = /<\?xml\s+(.*?)\?>*/um
    DOCTYPE_PATTERN = /\s*<!DOCTYPE\s+(.*?)(\[|>)/um
    COMMENT_START = /\A<!--/u
    COMMENT_END = /.*?-->/um


    def parse
      plist_tags = PTag::mappings.keys.join('|')
      start_tag  = /<(#{plist_tags})([^>]*)>/i
      end_tag    = /<\/(#{plist_tags})[^>]*>/i

      require 'strscan'

      contents = (
        if (!@filename_or_xml)
          nil
        elsif (@filename_or_xml.respond_to?(:read))
          @filename_or_xml.read
        elsif (File.exists? @filename_or_xml)
          File.open(@filename_or_xml) {|f| f.read}
        else
          @filename_or_xml
        end
      )

      @scanner = StringScanner.new( contents )
      until @scanner.eos?
        if @scanner.scan(COMMENT_START)
          @scanner.scan(COMMENT_END)
        elsif @scanner.scan(XMLDECL_PATTERN)
        elsif @scanner.scan(DOCTYPE_PATTERN)
        elsif @scanner.scan(start_tag)
          @listener.tag_start(@scanner[1], nil)
          if (@scanner[2] =~ /\/$/)
            @listener.tag_end(@scanner[1])
          end
        elsif @scanner.scan(TEXT)
          @listener.text(@scanner[1])
        elsif @scanner.scan(end_tag)
          @listener.tag_end(@scanner[1])
        else
          raise "Unimplemented element"
        end
      end
    end
  end

  class PTag
    @@mappings = { }
    def PTag::mappings
      @@mappings
    end

    def PTag::inherited( sub_class )
      key = sub_class.to_s.downcase
      key.gsub!(/^osx::propertylist::/, '' )
      key.gsub!(/^p/, '')  unless key == "plist"

      @@mappings[key] = sub_class
    end

    attr_accessor :text, :children
    def initialize
      @children = Array.new
    end

    def to_ruby
      raise "Unimplemented: " + self.class.to_s + "#to_ruby on #{self.inspect}"
    end
  end

  class PList < PTag
    def to_ruby
      children.first.to_ruby if children.first
    end
  end

  class PDict < PTag
    def to_ruby
      dict = Hash.new
      key = nil

      children.each do |c|
        if key.nil?
          key = c.to_ruby
        else
          dict[key] = c.to_ruby
          key = nil
        end
      end

      dict
    end
  end

  class PKey < PTag
    def to_ruby
      CGI::unescapeHTML(text || '')
    end
  end

  class PString < PTag
    def to_ruby
      CGI::unescapeHTML(text || '')
    end
  end

  class PArray < PTag
    def to_ruby
      children.collect do |c|
        c.to_ruby
      end
    end
  end

  class PInteger < PTag
    def to_ruby
      text.to_i
    end
  end

  class PTrue < PTag
    def to_ruby
      true
    end
  end

  class PFalse < PTag
    def to_ruby
      false
    end
  end

  class PReal < PTag
    def to_ruby
      text.to_f
    end
  end

  require 'date'
  class PDate < PTag
    def to_ruby
      DateTime.parse(text)
    end
  end

  require 'base64'
  class PData < PTag
    def to_ruby
      data = Base64.decode64(text.gsub(/\s+/, ''))

      begin
        return Marshal.load(data)
      rescue Exception => e
        io = StringIO.new
        io.write data
        io.rewind
        return io
      end
    end
  end
 end
end
